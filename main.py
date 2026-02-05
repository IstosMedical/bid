import json
from playwright.sync_api import sync_playwright

def fetch_bids():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # set to False so you can see the browser
        page = browser.new_page()
        page.goto("https://bidplus.gem.gov.in/all-bids", timeout=60000)
        
        # Wait for the page body to load instead of a specific div
        page.wait_for_selector("body", timeout=60000)

        # Try a broader selector for bid cards
        blocks = page.query_selector_all("div.block_list, div.block, div.border")

        bids = []
        for block in blocks:
            bids.append(block.inner_text())
        browser.close()
        return bids

def main():
    bids = fetch_bids()
    with open("bids_raw.json", "w", encoding="utf-8") as f:
        json.dump(bids, f, indent=4, ensure_ascii=False)
    print(f"Saved {len(bids)} raw bids to bids_raw.json")

if __name__ == "__main__":
    main()
