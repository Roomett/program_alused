import csv
from datetime import datetime

tulemus = []

with open("hinnad.csv", newline="") as f:
    andmed = csv.DictReader(f, delimiter=";")
    for rida in andmed:
        hind = float(rida["hind_eur_mwh"])
        tulemus.append((hind, rida["aeg"]))

odavaim = sorted(tulemus)[0]                          # (hind, aeg)
kalleim = sorted(tulemus)[-1]

kuupaev = odavaim[1][:10]                             # "2026-10-27" (aja teksti esimesed 10 märki)

def salvesta(failinimi, paar):
    with open(failinimi, "w", newline="") as f:
        kirjutaja = csv.writer(f, delimiter=";")
        kirjutaja.writerow(["aeg", "hind_eur_mwh"])
        kirjutaja.writerow([paar[1], paar[0]])        # aeg enne, hind pärast

salvesta(f"odav_hind_{kuupaev}.csv", odavaim)
salvesta(f"kallis_hind_{kuupaev}.csv", kalleim)
    



