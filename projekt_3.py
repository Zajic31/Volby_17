"""
projekt_3.py: Volby 2017

author: David Zajíček
email: davidzajicek07@gmail.com
"""

import sys
import csv
import requests
from bs4 import BeautifulSoup

POZADOVANE_STRANY = {
    "Občanská demokratická strana": "ODS",
    "Česká str.sociálně demokrat.": "ČSSD",
    "Komunistická str.Čech a Moravy": "KSČM",
    "ANO 2011": "ANO 2011",
    "Svob.a př.dem.-T.Okamura (SPD)": "SPD",
    "Česká pirátská strana": "Piráti",
    "CESTA ODPOVĚDNÉ SPOLEČNOSTI": "COS",
    "Radostné Česko": "Rado. Č.",
    "STAROSTOVÉ A NEZÁVISLÍ": "STAN",
    "Strana zelených": "Zelený",
    "ROZUMNÍ-stop migraci,diktát.EU": "ROZUMNÍ",
    "Strana svobodných občanů": "SSO",
    "Blok proti islam.-Obran.domova": "BPI",
    "Občanská demokratická aliance": "ODA",
    "Referendum o Evropské unii": "EU referendum",
    "TOP 09": "TOP 09",
    "Dobrá volba 2016": "DB 2016",
    "SPR-Republ.str.Čsl. M.Sládka": "SPR",
    "Křesť.demokr.unie-Čs.str.lid.": "Křesťaní",
    "Česká strana národně sociální": "ČSNS",
    "REALISTÉ": "REALIST",
    "SPORTOVCI": "SPORT",
    "Dělnic.str.sociální spravedl.": "DSSS",
    "Strana Práv Občanů": "SPO"
}


def get_obce_info(main_url):
    base = "https://volby.cz/pls/ps2017nss/"
    r = requests.get(main_url)
    soup = BeautifulSoup(r.text, "html.parser")
    rows = soup.select("tr")

    obce = []
    for row in rows:
        cislo = row.select_one("td.cislo a")
        nazev = row.select_one("td.overflow_name")

        if cislo and nazev:
            kod_obce = cislo.text.strip()
            nazev_obce = nazev.text.strip()
            href = cislo["href"]
            url = base + href
            obce.append((kod_obce, nazev_obce, url))
    return obce


def parse_obec(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    volici = soup.find("td", headers="sa2").text.strip().replace("\xa0", "")
    obalky = soup.find("td", headers="sa3").text.strip().replace("\xa0", "")
    platne = soup.find("td", headers="sa6").text.strip().replace("\xa0", "")

    strany = soup.find_all("td", class_="overflow_name")
    hlasy = soup.find_all("td", headers=lambda h: h and "t1sa2" in h)

    vysledky = {zkr: "0" for zkr in POZADOVANE_STRANY.values()}
    for s, h in zip(strany, hlasy):
        nazev = s.text.strip()
        if nazev in POZADOVANE_STRANY:
            zkr = POZADOVANE_STRANY[nazev]
            pocet = h.text.strip().replace("\xa0", "")
            vysledky[zkr] = pocet

    return volici, obalky, platne, vysledky


def main():
    if len(sys.argv) != 3:
        print("Použití: python projekt_3.py <URL> <výstupní_soubor.csv>")
        exit(1)

    input_url = sys.argv[1]
    output_csv = sys.argv[2]

    print("Stahuju more seznam obcí more...")
    obce = get_obce_info(input_url)
    print(f"Nalezeno obcí: {len(obce)}")

    poradi = list(POZADOVANE_STRANY.values())
    vysledky_csv = []

    for kod, nazev, url in obce:
        volici, obalky, platne, hlasy = parse_obec(url)
        radek = [kod, nazev, volici, obalky, platne] + [hlasy[zkr] for zkr in poradi]
        vysledky_csv.append(radek)

    with open(output_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        hlavicka = ["kód obce", "název obce", "voliči v seznamu", "vydané obálky", "platné hlasy"] + poradi
        writer.writerow(hlavicka)
        writer.writerows(vysledky_csv)

    print(f"Výsledky: {output_csv}")


if __name__ == "__main__":
    main()
