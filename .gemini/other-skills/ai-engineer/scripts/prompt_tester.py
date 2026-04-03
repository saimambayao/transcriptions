#!/usr/bin/env python3
"""
Prompt Testing Utility for AI Features

Test prompts with different inputs, models, and parameters to optimize before production.

Usage:
    python prompt_tester.py --prompt-file prompts/assessment_summary.txt --test-cases test_cases.json
    python prompt_tester.py --interactive
    python prompt_tester.py --batch-test prompts/
"""

import anthropic
import openai
import json
import time
import argparse
from pathlib import Path
from typing import List, Dict, Any
import os

class PromptTester:
    def __init__(self, anthropic_key=None, openai_key=None):
        self.anthropic_key = anthropic_key or os.getenv('ANTHROPIC_API_KEY')
        self.openai_key = openai_key or os.getenv('OPENAI_API_KEY')

        if self.anthropic_key:
            self.anthropic_client = anthropic.Anthropic(api_key=self.anthropic_key)
        if self.openai_key:
            self.openai_client = openai.OpenAI(api_key=self.openai_key)

    def test_prompt(self, prompt: str, model: str = "claude-sonnet-4-20250514",
                    max_tokens: int = 1024) -> Dict[str, Any]:
        """Test a single prompt and return results with metrics."""
        start_time = time.time()

        try:
            if model.startswith("claude"):
                response = self.anthropic_client.messages.create(
                    model=model,
                    max_tokens=max_tokens,
                    messages=[{"role": "user", "content": prompt}]
                )
                output = response.content[0].text
                input_tokens = response.usage.input_tokens
                output_tokens = response.usage.output_tokens

            elif model.startswith("gpt"):
                response = self.openai_client.chat.completions.create(
                    model=model,
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=max_tokens
                )
                output = response.choices[0].message.content
                input_tokens = response.usage.prompt_tokens
                output_tokens = response.usage.completion_tokens

            else:
                raise ValueError(f"Unknown model: {model}")

            latency = time.time() - start_time

            return {
                'success': True,
                'output': output,
                'model': model,
                'input_tokens': input_tokens,
                'output_tokens': output_tokens,
                'latency_seconds': round(latency, 2),
                'cost_estimate': self.estimate_cost(model, input_tokens, output_tokens),
            }

        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'model': model,
            }

    def estimate_cost(self, model: str, input_tokens: int, output_tokens: int) -> float:
        """Estimate cost based on model and token usage (2025 pricing)."""
        pricing = {
            'claude-haiku-4-20250514': {'input': 0.80, 'output': 4.00},
            'claude-sonnet-4-20250514': {'input': 3.00, 'output': 15.00},
            'claude-opus-4-20250514': {'input': 15.00, 'output': 75.00},
            'gpt-4o': {'input': 5.00, 'output': 15.00},
            'gpt-4o-mini': {'input': 0.15, 'output': 0.60},
        }

        if model not in pricing:
            return 0.0

        cost = (
            (input_tokens / 1_000_000) * pricing[model]['input'] +
            (output_tokens / 1_000_000) * pricing[model]['output']
        )
        return round(cost, 6)

    def test_with_variations(self, base_prompt: str, test_cases: List[Dict],
                            models: List[str] = None) -> List[Dict]:
        """Test prompt with multiple input variations and models."""
        if models is None:
            models = ["claude-sonnet-4-20250514"]

        results = []

        for i, test_case in enumerate(test_cases):
            # Substitute variables in prompt
            prompt = base_prompt
            for key, value in test_case.items():
                prompt = prompt.replace(f"{{{key}}}", str(value))

            print(f"\n--- Test Case {i+1}/{len(test_cases)} ---")
            print(f"Input: {test_case}")

            for model in models:
                print(f"Testing with {model}...")
                result = self.test_prompt(prompt, model=model)
                result['test_case'] = test_case
                results.append(result)

                if result['success']:
                    print(f"✓ Success - Latency: {result['latency_seconds']}s, Cost: ${result['cost_estimate']}")
                    print(f"Output preview: {result['output'][:100]}...")
                else:
                    print(f"✗ Failed - {result['error']}")

        return results

    def interactive_mode(self):
        """Interactive prompt testing."""
        print("=== Prompt Tester Interactive Mode ===\n")

        model = input("Model (claude-sonnet-4-20250514): ").strip() or "claude-sonnet-4-20250514"

        print("\nEnter your prompt (type END on a new line to finish):")
        lines = []
        while True:
            line = input()
            if line == "END":
                break
            lines.append(line)

        prompt = "\n".join(lines)

        print("\nTesting prompt...")
        result = self.test_prompt(prompt, model=model)

        print("\n=== Results ===")
        print(json.dumps(result, indent=2))

        if result['success']:
            print(f"\n--- Generated Output ---\n{result['output']}")

    def batch_test(self, prompt_dir: Path, output_file: Path = None):
        """Test all prompts in a directory."""
        prompt_files = list(prompt_dir.glob("*.txt"))

        print(f"Found {len(prompt_files)} prompt files in {prompt_dir}")

        all_results = []

        for prompt_file in prompt_files:
            print(f"\n=== Testing {prompt_file.name} ===")

            with open(prompt_file) as f:
                prompt = f.read()

            # Check for test cases file
            test_cases_file = prompt_file.with_suffix('.json')
            if test_cases_file.exists():
                with open(test_cases_file) as f:
                    test_cases = json.load(f)
                results = self.test_with_variations(prompt, test_cases)
            else:
                result = self.test_prompt(prompt)
                results = [result]

            all_results.extend(results)

        # Save results
        if output_file:
            with open(output_file, 'w') as f:
                json.dump(all_results, f, indent=2)
            print(f"\nResults saved to {output_file}")

        # Summary
        successful = sum(1 for r in all_results if r.get('success'))
        total_cost = sum(r.get('cost_estimate', 0) for r in all_results)
        avg_latency = sum(r.get('latency_seconds', 0) for r in all_results if r.get('success')) / max(successful, 1)

        print(f"\n=== Summary ===")
        print(f"Total tests: {len(all_results)}")
        print(f"Successful: {successful}/{len(all_results)}")
        print(f"Total estimated cost: ${total_cost:.4f}")
        print(f"Average latency: {avg_latency:.2f}s")


def main():
    parser = argparse.ArgumentParser(description="Test AI prompts before production")
    parser.add_argument('--prompt-file', type=Path, help="Path to prompt file")
    parser.add_argument('--test-cases', type=Path, help="Path to test cases JSON")
    parser.add_argument('--model', default="claude-sonnet-4-20250514", help="Model to use")
    parser.add_argument('--interactive', action='store_true', help="Interactive mode")
    parser.add_argument('--batch-test', type=Path, help="Test all prompts in directory")
    parser.add_argument('--output', type=Path, help="Output file for results")

    args = parser.parse_args()

    tester = PromptTester()

    if args.interactive:
        tester.interactive_mode()

    elif args.batch_test:
        tester.batch_test(args.batch_test, args.output)

    elif args.prompt_file:
        with open(args.prompt_file) as f:
            prompt = f.read()

        if args.test_cases:
            with open(args.test_cases) as f:
                test_cases = json.load(f)
            results = tester.test_with_variations(prompt, test_cases, models=[args.model])
        else:
            result = tester.test_prompt(prompt, model=args.model)
            results = [result]

        # Print results
        print("\n=== Results ===")
        print(json.dumps(results, indent=2))

        if args.output:
            with open(args.output, 'w') as f:
                json.dump(results, f, indent=2)
            print(f"\nResults saved to {args.output}")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
