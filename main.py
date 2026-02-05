from scraper.gem_scraper import fetch_bids

def main():
    bids = fetch_bids()
    for b in bids:
        print(f"Title: {b['title']}")
        print(f"Location: {b['location']}")
        print(f"Deadline: {b['deadline']}")
        print("-" * 40)

if __name__ == "__main__":
    main()
