import csv
from datetime import datetime

# --- 1. Küsime kasutajalt ---
while True:
    tunde = float(input("Mitu tundi soovite voolu kasutada? (nt 1.5): "))
    if (tunde * 4) % 1 == 0:
        break
    print("Sisesta aeg veerandtunni täpsusega (0.25, 0.5, 0.75, 1, ...)")

veerandeid = int(tunde * 4)

voimsus = float(input("Mitu kW on seadme võimsus? (nt 2 pesumasinal): "))

aken = input("Mis ajavahemikul olete kodus? (nt 18:35-23:21): ")
algus_tekst, lopp_tekst = aken.split("-")
algus = datetime.strptime(algus_tekst.strip(), "%H:%M").time()
lopp = datetime.strptime(lopp_tekst.strip(), "%H:%M").time()


# --- 2. Funktsioon, mis annab paari aja ---
def aja_jargi(paar):
    return paar[1]                                    # paar on (hind, aeg)


# --- 3. Loeme CSV ja jätame alles ainult akna sees olevad ---
tulemus = []                                          # paarid (hind, kellaaeg)

with open("hinnad.csv", newline="") as f:
    andmed = csv.DictReader(f, delimiter=";")
    for rida in andmed:
        hind = float(rida["hind_eur_mwh"])
        kellaaeg = datetime.strptime(rida["aeg"], "%Y-%m-%d %H:%M")
        if algus <= kellaaeg.time() < lopp:
            tulemus.append((hind, kellaaeg))

tulemus.sort(key=aja_jargi)                           # aja järgi, et read oleksid järjest

# --- 4. Kontroll: kas aken on piisavalt pikk ---
if len(tulemus) < veerandeid:
    print("Aken on liiga lühike, et sinna see aeg mahuks.")
    exit()

# --- 5. Leiame odavaima järjestikuse lõigu ---
parim_summa = None
parim_algus = 0                                       # mitmendast reast parim lõik algab

for i in range(len(tulemus) - veerandeid + 1):        # kõik võimalikud algused
    summa = 0
    for j in range(i, i + veerandeid):                # liidame veerandeid tk järjest
        summa = summa + tulemus[j][0]                 # [0] on hind
    if parim_summa is None or summa < parim_summa:
        parim_summa = summa
        parim_algus = i

odavad = tulemus[parim_algus : parim_algus + veerandeid]
odavad_ajad = set(aeg for hind, aeg in odavad)

# --- 6. Prindime valitud ajad ---
for hind, aeg in tulemus:
    if aeg in odavad_ajad:
        print(aeg.strftime("%d.%m %H:%M"), hind, "EUR/MWh", "Kasuta")

# --- 7. Arvutame maksumuse ---
keskmine = parim_summa / veerandeid                   # EUR/MWh
energia = voimsus * tunde                             # kWh
kulu = keskmine / 1000 * energia                      # EUR

print(f"\nKeskmine hind: {keskmine:.2f} EUR/MWh")
print(f"Seade ({voimsus} kW, {tunde} h) kulutab {energia:.2f} kWh")
print(f"Elektri maksumus: {kulu:.4f} EUR")