
```

In []:
```python
# !pip install tensorflow==2.8.0
# !pip install transformers==4.20.1
# !pip install sentencepiece==0.1.96

```

In []:
```python
import pandas as pd
import numpy as np
import tensorflow as tf
import os
import re
import math
from transformers import AutoTokenizer, TFAutoModelForSeq2SeqLM, DataCollatorForSeq2Seq, create_optimizer
from datasets import Dataset
from google.colab import drive

```

In []:
```python
# Mount Google Drive to access files
drive.mount('/content/drive')

```

Out []:
```output
Drive already at the notebook.
```

In []:
```python
import os

# Define the root path for dataset and checkpoint folders
root_path = '/content/drive/MyDrive/NLP Project'
input_file = os.path.join(root_path, 'v_2.0.txt')
model_checkpoint = "google/mt5-small"
model_name = model_checkpoint.split("/")[-1]
output_dir = os.path.join(root_path, f"{model_name}-finetuned-summarization")

```

In []:
```python
# Read the file line by line
with open(input_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Filter lines to separate content and summaries
# Assuming the format: [Time] Text is content, [Time] summary: Text is summary
content = []
summaries = []

# temporary containers for building chunks
current_content = []
current_summary = []

for line in lines:
    line = line.strip()
    if line.startswith('[') and 'summary:' in line:
        # Save the previous content chunk before starting a new summary
        if current_content:
            content.append(" ".join(current_content))
            current_content = []
        # Extract and add summary
        summary_text = line.split('summary:', 1)[1].strip()
        summaries.append(summary_text)
    elif line.startswith('['):
        # Extract content (removing the timestamp)
        parts = line.split(']', 1)
        if len(parts) > 1:
            current_content.append(parts[1].strip())

# Create a Pandas DataFrame
data = pd.DataFrame({'content': content, 'summary': summaries})

# Shuffle and split the data into training and testing sets
data = data.sample(frac=1).reset_index(drop=True)
train_size = int(0.8 * len(data))
train_df = data[:train_size]
test_df = data[train_size:]

# Convert to Hugging Face Dataset
train_dataset = Dataset.from_pandas(train_df)
test_dataset = Dataset.from_pandas(test_df)

```

In []:
```python
tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)

max_input_length = 512
max_target_length = 64

def preprocess_function(examples):
    inputs = ["summarize: " + doc for doc in examples["content"]]
    model_inputs = tokenizer(inputs, max_length=max_input_length, truncation=True, padding="max_length")

    with tokenizer.as_target_tokenizer():
        labels = tokenizer(examples["summary"], max_length=max_target_length, truncation=True, padding="max_length")

    model_inputs["labels"] = labels["input_ids"]
    return model_inputs

# Map the preprocessing function over the dataset
tokenized_train = train_dataset.map(preprocess_function, batched=True)
tokenized_test = test_dataset.map(preprocess_function, batched=True)

```

Out []:
```output
/usr/local/lib/python3.10/dist-packages/huggingface_hub/utils/_token.py:89: UserWarning: 
The progress bars may be unreliable. There are many reasons for this, such as differences between local environments and attached fleets.
You may see errors even if temporary failures occur. Try clearing the cache.
  warnings.warn(
/usr/local/lib/python3.10/dist-packages/transformers/convert_slow_tokenizer.py:434: UserWarning: The sentencepiece tokenizer that you are converting to a fast tokenizer uses the byte fallback option which is not implemented in the fast tokenizers. In practice this means that the fast version of the tokenizer can produce unknown words if the used chunk of text contains bytes notable by the software. We've added a warm up step in order to synthesize the unknown words and improve the quality of the tokens.
  warnings.warn(
/usr/local/lib/python3.10/dist-packages/transformers/tokenization_utils_base.py:3524: UserWarning: `as_target_tokenizer` is deprecated and will be removed in v5 of Transformers. You can tokenize your labels by using the argument `text_target` of the regular `__call__` method (either in the same call as your input tokens if you use the same keyword arguments, or in a separate call.
  warnings.warn(Map:   0%|          | 0/1572 [00:00<?, ? examples/s]Map:   0%|          | 0/393 [00:00<?, ? examples/s]
```

In []:
```python
model = TFAutoModelForSeq2SeqLM.from_pretrained(model_checkpoint)

# Define hyperparameters
batch_size = 8
num_train_epochs = 3
learning_rate = 2e-5
weight_decay = 0.01

data_collator = DataCollatorForSeq2Seq(tokenizer, model=model, return_tensors="tf")

# Prepare training and validation sets
train_set = model.prepare_tf_dataset(
    tokenized_train,
    shuffle=True,
    batch_size=batch_size,
    collate_fn=data_collator,
)

test_set = model.prepare_tf_dataset(
    tokenized_test,
    shuffle=False,
    batch_size=batch_size,
    collate_fn=data_collator,
)

# Optimizer
num_train_steps = len(train_set) * num_train_epochs
optimizer, lr_schedule = create_optimizer(
    init_lr=learning_rate,
    num_train_steps=num_train_steps,
    weight_decay_rate=weight_decay,
    num_warmup_steps=0,
)

model.compile(optimizer=optimizer)

```

Out []:
```output
All model checkpoint layers were used when initializing TFMT5ForConditionalGeneration.
All the layers of TFMT5ForConditionalGeneration were initialized from the model checkpoint at google/mt5-small.
If your task is similar to the task the model of the checkpoint was trained on, you can already use TFMT5ForConditionalGeneration for predictions without further training.
No loss specified in compile() - the model's internal loss computation will be used as the default. Don't panic! python should reach to help you!
```

In []:
```python
# Initializing callbacks
checkpoint_cb = tf.keras.callbacks.ModelCheckpoint(
    filepath=os.path.join(output_dir, "ckpt-{epoch}"),
    save_weights_only=True
)

# Training the model
model.fit(train_set, validation_data=test_set, epochs=num_train_epochs, callbacks=[checkpoint_cb])

# Save the final model and tokenizer
model.save_pretrained(output_dir)
tokenizer.save_pretrained(output_dir)

```

Out []:
```output
Epoch 1/3
196/196 [==============================] - 1461s 7s/step - loss: 16.5925 - val_loss: 5.6264
Epoch 2/3
196/196 [==============================] - 1319s 7s/step - loss: 6.9939 - val_loss: 4.0955
Epoch 3/3
196/196 [==============================] - 1324s 7s/step - loss: 4.9080 - val_loss: 3.5901('/content/drive/MyDrive/NLP Project/mt5-small-finetuned-summarization/tokenizer_config.json',
 '/content/drive/MyDrive/NLP Project/mt5-small-finetuned-summarization/special_tokens_map.json',
 '/content/drive/MyDrive/NLP Project/mt5-small-finetuned-summarization/tokenizer.json')
```

In []:
```python
from transformers import pipeline

summarizer = pipeline("summarization", model=output_dir, tokenizer=output_dir, framework="tf")

```

Out []:1. Charlie Munger says "common sense" in investing means "uncommon sense." This also applies to startups where simple first principles are often overlooked.

2. Entrepreneur Ash Maurya shares his top 10 uncommon sense startup maxims, highlighting common misunderstandings.

3. The primary reason products fail is building something nobody wants, often due to "Innovator's Bias" where founders fall in love with their solution prematurely.

4. Customers prioritize their own problems over solutions. Focusing on problems first helps identify the "door" before building the "key" (the solution).

5. Many founders fail to identify the right problem by inventing them or using leading questions in surveys, leading to false validation.

6. Creating products for unknown needs is difficult and expensive. Startups should focus on existing problems that customers are already trying to solve.

7. A problem worth solving must be known by customers, desired to be solved, and something they are willing to pay for.

8. Evidence of a problem worth solving is when people already spend time or money on existing alternatives.

9. An entrepreneur's true product is the business model, not just the solution. Building a great business model is like building a great product.

10. Tools like the Lean Canvas help deconstruct big ideas into key assumptions, providing a clear business model.

11. Before testing a business model in the market, "stress-test" it using thought experiments to identify potential flaws and avoid "zombie startups."

12. Ideas should be tested against seven factors: mission, clarity, viability, desirability, feasibility, defensibility, and timing.

13. Prioritize testing the riskiest assumptions first, such as customer and market risks, rather than the easiest tasks.

14. Use a "Demo-Sell-Build" approach rather than "Build-Demo-Sell" to validate demand and willingness to pay before fully developing a product.

15. The "Demo-Sell-Build" strategy works for both B2C and B2B products and helps avoid building something nobody wants.

16. Differentiate between "customers" (who pay) and "users" (who don't). Meaningful insights for growth come from paying customers.

17. Successful entrepreneurs embrace failures as "unexpected outcomes" that provide critical breakthrough insights.

18. Breakthroughs often come from analyzing why an experiment didn't go as expected, as seen in the development of the microwave and PayPal.

19. Focus on "repeatability" (consistent customer acquisition and value delivery) before attempting to scale the business**Maxim 10: Focus on Repeatability (Before Scalability)**

**10:25**
And the final uncommon sense maxim is number 10: Focus on repeatability before scalability. Too many founders are in a rush to get to the right side of the hockey stick curve. They do this by trying to go fast on everything.

**10:37**
But when you go fast on everything, it doesn't necessarily make you go faster and it's often a recipe for just getting lost faster and focusing on the wrong things at the wrong time. 

**10:49**
Premature optimization is one of the top startup killers because you can't scale something that isn't first repeatable. Repeatability here means:

1. You can consistently acquire customers.
2. You can reliably deliver value.
3. Your unit economics are starting to work.

**11:05**
The best part is that you don't need thousands or millions of users to establish repeatability. I've seen too many founders raise millions in funding and hire dozens of employees before they've figured out a repeatable business model. 

**11:20**
The results are almost always painful and expensive. Repeatability, then, is a prerequisite for scalability.

**Bonus Maxim: Just Start**

**11:25**
Now since this video is about uncommon sense, here's one more bonus maxim: Just start. Perfect idea, not required. We have been taught to prepare: prepare for the test, prepare for the big trip, prepare for the next project. 

**11:38**
Our natural tendency is to apply the same thinking to our ideas. When we get hit with an idea, or in preparation for getting hit with the right idea, we try to find the perfect time to act, the perfect book to read, or the perfect course to take. 

**11:51**
But entrepreneurship and startups are different. Riddled with extreme uncertainty, new ideas have no perfect time, perfect book, or perfect course that can fully prepare you to act. 

**12:02**
You have to take a leap and just start. So if you've been waiting to start, just start. 

**Conclusion and Call to Action**

**12:07**
Use these uncommon maxims to guide your journey and if you'd like to go even deeper down the rabbit hole, take my free "Just Start" email course that I'll link below. Thanks for watching and until next time, take care.

***

### **Organized Notes**

**Foundational Mindset: The "Uncommon Sense" Approach**
*   **[00:00]** Borrowing from Charlie Munger, common sense in high-stakes fields often means applying "uncommon sense"—the overlooked first principles.

**Maxim 1: Love the Problem, Not Your Solution**
*   **[00:40]** The primary reason for failure is building something unwanted.
*   **[01:00] Innovator's Bias:** Founders rush to build products rather than understanding problems. Customers care about their own problems, not your specific technical solution.
*   **[01:12] Key and Door Analogy:** Starting with a solution is building a key without a door. Identify the "door" (the problem) first.

**Maxim 2: Solve Existing Problems**
*   **[01:37]** Founders often invent problems or rely on hypothetical survey responses ("Will you use this?").
*   **[02:23] Category Trap:** Trying to solve problems customers don't know they have is too expensive and difficult for early startups. Focus on known pain points.

**Maxim 3: Identifying Problems Worth Solving**
*   **[02:51] Three Criteria:**
    *   Customers know they have the problem.
    *   They want it solved.
    *   They are willing to pay for it.
*   **[03:18] Proof of Worth:** Evidence of a problem worth solving exists when people are already spending time, money, or effort on current alternatives.

**Maxim 4: The Business Model is the Product**
*   **[03:47]** The entrepreneur's true product is not the solution, but the business model.
*   **[04:34] Lean Canvas:** Use tools like Lean Canvas to deconstruct big ideas into actionable assumptions.

**Maxim 5: Stress-Test Before Market Testing**
*   **[04:46]** Use thought experiments and simulations before building to identify obvious flaws.
*   **[05:49] Seven Factors:** Mission, clarity, viability, desirability, feasibility, defensibility, and timing.

**Maxim 6: Prioritize Riskiest Assumptions**
*   **[06:18]** Don't focus on easy tasks first. Address market risk ("Will they pay?") before technical risk ("Can we build it?").

**Maxim 7: Demo-Sell-Build**
*   **[07:05] Flipping the Script:** The traditional path (Build-Demo-Sell) is high risk. The "Smarter Path" involves demoing a concept (mockups) and getting pre-orders/commitments before writing code.

**Maxim 8: Talk to Customers, Not Just Users**
*   **[08:12] The Difference:** Customers pay; users do not. Insights for sustainable growth come from those willing to invest in the solution.

**Maxim 9: Chase Failures for Insights**
*   **[08:53] Reframing Failure:** View unexpected outcomes as "gold." Breakthroughs (like the Microwave or PayPal) come from asking "why" an experiment didn't work as planned.

**Maxim 10: Repeatability Before Scalability**
*   **[10:25] Hockey Stick Trap:** Don't rush to scale until you can consistently acquire customers, reliably deliver value, and prove unit economics work.

**Bonus Maxim: Just Start**
*   **[11:25] Avoid Over-Preparation:** There is no perfect time, book, or course for a startup due to inherent uncertainty. Action provides the only real data.