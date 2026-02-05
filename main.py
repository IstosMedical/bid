import requests
from bs4 import BeautifulSoup
import json

BASE_URL = "https://bidplus.gem.gov.in/all-bids"

def fetch_bids():
    response = requests.get(BASE_URL)
    soup = BeautifulSoup(response.text, "html.parser")

    bids = []
    for block in soup.find_all("div", class_="block"):
        bids.append(block.get_text(strip=True))

    return bids

def main():
    bids = fetch_bids()
    with open("bids_raw.json", "w", encoding="utf-8") as f:
        json.dump(bids, f, indent=4, ensure_ascii=False)
    print(f"Saved {len(bids)} raw bids to bids_raw.json")

if __name__ == "__main__":
    main()
