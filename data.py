import requests
from bs4 import BeautifulSoup



def scrape_data(sopivat_tunnit = [i for i in range(25)], week=0)-> list['Ma 29.9.20:00 Sulkapallo']: #0 = tämä viikko 1 = seuraava viikko
    
    url = f"https://www.tuni.fi/sportuni/omasivu/?page=selection&lang=fi&type=3&area=2&week={week}"

    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")

    date_link = []
    date_list = []
    suitable_hours = [] #sopivien tuntien lista

    for a in soup.select("li a"):
        teksti = a.get_text(strip=True)
        linkki = a["href"]


        if "Sulkapallo" in teksti:
            date_link.append((teksti, linkki))
            date_list.append(teksti)

    for date in date_list:
        viikonpäivä, aika, laji = date.split(" ")
        päivä_nr, kuukausi_nr, kellonaika = aika.split(".")
        tunnit, minuutit = kellonaika.split(":")

        if int(tunnit) in sopivat_tunnit:
            suitable_hours.append(date)


    return suitable_hours

#base_url = "https://www.tuni.fi/sportuni/omasivu/"
# full_url = base_url + linkki


print(scrape_data(sopivat_tunnit=[20]))