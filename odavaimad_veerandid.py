import csv
from datetime import datetime

while True:    #kordab kuni oige
    tunde = float(input("Mitu tundi soovite voolu kasutada? (nt 1.5): "))
    if (tunde * 4) % 1 == 0:
        break                                         # korrektne, tsükkel lõpeb
    print("Sisesta aeg veerandtunni täpsusega (0.25, 0.5, 0.75, 1, ...)")

veerandeid = int(tunde * 4)
aken = input("Mis ajavahemikul olete kodus? (nt 18:35-23:21): ")

algus_tekst, lopp_tekst = aken.split("-")
algus = datetime.strptime(algus_tekst.strip(), "%H:%M").time()
lopp = datetime.strptime(lopp_tekst.strip(), "%H:%M").time()


tulemus = []                                          # paarid (hind, kellaaeg)


with open("hinnad.csv", newline="") as f:
    andmed = csv.DictReader(f, delimiter=";")
    for rida in andmed:
        hind = float(rida["hind_eur_mwh"])
        kellaaeg = datetime.strptime(rida["aeg"], "%Y-%m-%d %H:%M")
        if algus <= kellaaeg.time() < lopp:           # ainult akna seesimport csv


            tulemus.append((hind, kellaaeg))
odavad = sorted(tulemus)[:veerandeid]                         # sorteerib hinna järgi, võtab 20 odavamat
odavad_ajad = set(aeg for hind, aeg in odavad)        # võtab paaridest ainult aja

for hind, aeg in sorted(tulemus, key=lambda p: p[1]): # sorteerib aja järgi
    if aeg in odavad_ajad:
        print(aeg.strftime("%d.%m %H:%M"), hind, "EUR/MWh", "Kasuta")
    