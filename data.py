import requests
from bs4 import BeautifulSoup


linkki = "https://www.tuni.fi/sportuni/omasivu/?page=selection&lang=fi&type=3&area=2&week=0#&ui-state=dialog"


def scrape_data(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")

    slots = []

    for a in soup.select("li a"):
        teksti = a.get_text(strip=True)
        linkki = a["href"]
        slots.append((teksti, linkki))

    return slots



print(scrape_data(linkki))


base_url = "https://www.tuni.fi/sportuni/omasivu/"

full_url = base_url + linkki