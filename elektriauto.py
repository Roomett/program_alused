import requests
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

# homse päeva algus ja lõpp (arvuti kohalik aeg)
tana = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
algus = tana + timedelta(days=1)    # homme 00:00
lopp = tana + timedelta(days=2)     # ülehomme 00:00 (ehk homse päeva lõpp)

# Elering tahab aega UTC-s formaadis 2026-10-05T16:00:00.000Z
def utc_str(dt):
    return dt.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.000Z")

url = (
    "https://dashboard.elering.ee/api/nps/price"
    f"?start={utc_str(algus)}&end={utc_str(lopp)}"
)


andmed = requests.get(url, timeout=10).json()         #timeout on aeg kaua serverilt vastust oodatakse, et serveri maasoleku ajal ei jaadaks loputult ootama

tulemus = []                                          #[] on tyhi list mida ma taitma hakkan
for rida in andmed["data"]["ee"]:                     #votab andmetest data ja eesti andmed
    tulemus.append((rida["price"], rida["timestamp"]))#votab sealt siis hinna ja aja, lisab [] listi

if len(tulemus) < 96:                                 #kui vasteid on vahem kui peaks siis annab kood sellest teada(ehk andmed pole veel avalikud)
    print("Hinnad pole veel täielikult saadaval, andmeid on ainult", len(tulemus), "perioodi")

odavad = sorted(tulemus)[:20]                         #sorteerib paarid esimese elemendi, ehk hinna järgi. [:20] võtab sellest sorteeritud listist esimesed 20 elementi
odavad_ajad = set(ts for hind, ts in odavad)          #See käib odavad listi läbi ja võtab igast paarist ainult timestampi (ts), hinda ignoreerib

for hind, ts in sorted(tulemus, key=lambda p: p[1]):  # sorteerib kõik 49 paari uuesti, aga nüüd key=lambda p: p[1] abil
    aeg = datetime.fromtimestamp(ts)                  #Teeb timestampi arvuks loetavaks kellaajaks
    
    if ts in odavad_ajad:                             #kontrollib kas ts on odavate aegade listis
        print(aeg.strftime("%d.%m %H:%M"), hind,"kW/h", "LAE AUTOT") #Kui if oli tõene, prindib kellaaja, hinna ja teksti
    else:                                             #kui if ei ole toene
        print(aeg.strftime("%d.%m %H:%M"), hind,"kW/h", "KALLIS")

    