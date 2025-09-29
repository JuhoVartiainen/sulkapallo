import requests
from bs4 import BeautifulSoup



def scrape_data(sopivat_viikonpäivät= ["ma, ti, ke, to, pe, la, su"], sopivat_tunnit = [i for i in range(25)], week=0): #0 = tämä viikko 1 = seuraava viikko #-> list['Ma 29.9.20:00 Sulkapallo']
    
    url = f"https://www.tuni.fi/sportuni/omasivu/?page=selection&lang=fi&type=3&area=2&week={week}"

    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")

    date_link = []
    date_list = []
    suitable = [] #sopivien tuntien lista

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

        if int(tunnit) in sopivat_tunnit and viikonpäivä.lower() in sopivat_viikonpäivät:
            suitable.append(date)


    return suitable

#base_url = "https://www.tuni.fi/sportuni/omasivu/"
# full_url = base_url + linkki


print(scrape_data(sopivat_viikonpäivät=["ma", "ke", "pe"], sopivat_tunnit=[12]))