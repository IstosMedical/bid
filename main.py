import json
from playwright.sync_api import sync_playwright

def fetch_bids():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # keep visible for debugging
        page = browser.new_page()
        page.goto("https://gem.gov.in/", timeout=60000)

        # Click login button
        page.click("text=Login")

        # Fill credentials (replace with your actual GeM username/password)
        page.fill("input[name='userId']", "YOUR_USERNAME")
        page.fill("input[name='password']", "YOUR_PASSWORD")
        page.click("button[type='submit']")

        # Navigate to All Bids page after login
        page.goto("https://bidplus.gem.gov.in/all-bids", timeout=60000)
        page.wait_for_selector("div.block_list", timeout=60000)

        blocks = page.query_selector_all("div.block_list")

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
