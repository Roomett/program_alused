import requests
from datetime import datetime
from zoneinfo import ZoneInfo
url = "https://dashboard.elering.ee/api/nps/price?start=2026-10-05T16%3A00%3A00.000Z&end=2026-10-06T04%3A00%3A00.000Z"





andmed = requests.get(url, timeout=10).json()         #timeout on aeg kaua serverilt vastust oodatakse, et serveri maasoleku ajal ei jaadaks loputult ootama

tulemus = []                                          #[] on tyhi list mida ma taitma hakkan
for rida in andmed["data"]["ee"]:                     #votab andmetest data ja eesti andmed
    tulemus.append((rida["price"], rida["timestamp"]))#votab sealt siis hinna ja aja, lisab [] listi

odavad = sorted(tulemus)[:20]                         #sorteerib paarid esimese elemendi, ehk hinna järgi. [:20] võtab sellest sorteeritud listist esimesed 20 elementi
odavad_ajad = set(ts for hind, ts in odavad)          #See käib odavad listi läbi ja võtab igast paarist ainult timestampi (ts), hinda ignoreerib

for hind, ts in sorted(tulemus, key=lambda p: p[1]):  # sorteerib kõik 49 paari uuesti, aga nüüd key=lambda p: p[1] abil
    aeg = datetime.fromtimestamp(ts)                  #Teeb timestampi arvuks loetavaks kellaajaks
    
    if ts in odavad_ajad:                             #kontrollib kas ts on odavate aegade listis
        print(aeg.strftime("%d.%m %H:%M"), hind,"kW/h", "LAE AUTOT") #Kui if oli tõene, prindib kellaaja, hinna ja teksti
    else:                                             #kui if ei ole toene
        print(aeg.strftime("%d.%m %H:%M"), hind,"kW/h", "KALLIS")
    