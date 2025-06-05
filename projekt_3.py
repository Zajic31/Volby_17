"""
projekt_3.py: Volby 2017

author: David Zajicek
email: davidzajicek07@gmail.com
discord: idk
"""

import requests
from bs4 import (BeautifulSoup)
import csv
import sys

# Zpracování argumentů
if len(sys.argv) != 3:
    print("Chyba: Zadej 2 argumenty – URL a název výstupního souboru (.csv)")
    exit()

input_url = sys.argv[1]
output_csv = sys.argv[2]

# Získání HTML stránky
response = requests.get(input_url)
soup = BeautifulSoup(response.text, 'html.parser')

# Najdi odkazy na jednotlivé obce
base_url = "https://volby.cz/pls/ps2017nss/"
obec_links = soup.find_all("a")
urls = [base_url + a["href"] for a in obec_links if "href" in a.attrs and "obec" in a["href"]]

# Připravíme CSV
with open(output_csv, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow([
        "kód obce", "název obce", "voliči v seznamu", "vydané obálky", "platné hlasy",
        "Občanská demokratická strana", "Česká str.sociálně demokrat.", "Komunistická str.Čech a Moravy",
        "ANO 2011", "SPD", "Piráti"
    ])

    # Projdeme každou obec
    for url in urls:
        res = requests.get(url)
        bs = BeautifulSoup(res.text, "html.parser")

        # Kód a název obce
        kod_obce = bs.select_one("h3").text.split(":")[0].split(" ")[-1]
        nazev_obce = bs.select_one("h3").text.split(":")[1].strip()

        # Základní čísla
        tds = bs.find_all("td", headers=["sa2", "sa3", "sa6"])
        volici = tds[0].text.replace("\xa0", "")
        obalky = tds[1].text.replace("\xa0", "")
        platne = tds[2].text.replace("\xa0", "")

        # Hlasy pro vybrané strany
        strany = ["Občanská demokratická strana", "Česká str.sociálně demokrat.",
                  "Komunistická str.Čech a Moravy", "ANO 2011", "SPD", "Piráti"]
        hlasu = []

        for strana in strany:
            td = bs.find("td", string=strana)
            if td:
                hlas = td.find_next_sibling("td").text.replace("\xa0", "")
            else:
                hlas = "0"
            hlasu.append(hlas)

        writer.writerow([kod_obce, nazev_obce, volici, obalky, platne] + hlasu)

print(f"Hotovo! Výsledky uloženy do {output_csv}")
