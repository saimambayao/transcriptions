import requests

url = "https://quran.com/api/proxy/content/api/qdc/hadith_references/by_ayah/2:255/hadiths?language=en&page=1&limit=4"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": "https://quran.com/2:255/hadith",
    "Accept": "application/json"
}

res = requests.get(url, headers=headers)
print(f"Status: {res.status_code}")
print(f"Content: {res.text[:200]}")
