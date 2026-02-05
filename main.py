from scraper.gem_scraper import fetch_bids

def main():
    bids = fetch_bids()

    keywords = ["Cryostat Microtome", "Automated tissue processor", "Microtome blades", "Rotary Microtome"]
    state_filter = "Karnataka"

    for b in bids:
        if any(k.lower() in b['title'].lower() for k in keywords) and state_filter.lower() in b['location'].lower():
            print(f"Matched Bid: {b['title']} in {b['location']} (Deadline: {b['deadline']})")

if __name__ == "__main__":
    main()
