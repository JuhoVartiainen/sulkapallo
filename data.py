import requests
from bs4 import BeautifulSoup




def scrape_data(week=1, tunnit = [i for i in range(25)]):
    #0 = tämä viikko 1 = seuraava viikko
    url = f"https://www.tuni.fi/sportuni/omasivu/?page=selection&lang=fi&type=3&area=2&week={week}"

    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")

    all_times = []

    for a in soup.select("li a"):
        teksti = a.get_text(strip=True)
        linkki = a["href"]
        if "Sulkapallo" in teksti:
            all_times.append((teksti, linkki))

    return all_times

 
print([n[0] for n in scrape_data()])
base_url = "https://www.tuni.fi/sportuni/omasivu/"

# full_url = base_url + linkki