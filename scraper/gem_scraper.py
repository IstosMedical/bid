import requests
from bs4 import BeautifulSoup

BASE_URL = "https://bidplus.gem.gov.in/all-bids"

def fetch_bids():
    response = requests.get(BASE_URL)
    if response.status_code != 200:
        print("Failed to fetch page:", response.status_code)
        return []

    soup = BeautifulSoup(response.text, "html.parser")

    bids = []
    # GeM uses divs with class 'block' for each bid card
    for bid in soup.find_all("div", class_="block"):
        title = bid.find("span", class_="bid_title")
        location = bid.find("span", class_="bid_location")
        deadline = bid.find("span", class_="bid_deadline")

        bids.append({
            "title": title.text.strip() if title else "N/A",
            "location": location.text.strip() if location else "N/A",
            "deadline": deadline.text.strip() if deadline else "N/A"
        })

    return bids
