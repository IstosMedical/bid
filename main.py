import json
from scraper.gem_scraper import fetch_bids

def main():
    bids = fetch_bids()

    # Filter for relevant instruments in Karnataka
    keywords = ["Microtome blades", "Cryostat Microtome", "Rotary Microtome", "Automated tissue processor"]
    state_filter = "Karnataka"

    filtered_bids = [
        b for b in bids
        if any(k.lower() in b['title'].lower() for k in keywords)
        and state_filter.lower() in b['location'].lower()
    ]

    # Save results to JSON file
    with open(r"C:\Users\ISTOS-ADMIN\bid\bids.json", "w", encoding="utf-8") as f:
        json.dump(filtered_bids, f, indent=4, ensure_ascii=False)

    print(f"Saved {len(filtered_bids)} bids to bids.json")

if __name__ == "__main__":
    main()
