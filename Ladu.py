##kirjutad algorytmi yhe rea kohta ja siis yield laheb rida rea haaval yle failist

#iga rea kohta on vaja teada:
#mitu toodet failis on;
#mitu toodet on iga käibemaksumääraga; (teeme dicti)
#mitu toodet on laost otsas (laoseis == 0) ja nende nimetused;   if laoseis == 0 siis otsas tooted +1 v midagi
#kõige kallim ja kõige odavam toode (nimetus, inventarinumber, hind km-ta ja km-ga);
#lao koguväärtus käibemaksuta;   lao_vaartus(tooted, km_ga=False)  hind * laoseis
#lao koguväärtus käibemaksuga vana ja uue määraga ning nende vahe.   hind_km_ga(hind, maar)  uus_maar(maar)

#opetaja algoritm
#   *csv                                 loe rida
#toodete_arv = 0                          toodete_arv +=1
#vanad_mm={"mm_0";0}                      vanad_mm=["22"]= vanad_mm["22"]+1
#eks_toode: {"max_t":{nimetus:"",         eks_toode
#                     inv_nr:"",          
#                     hind: 0.0,          
 #                    hind_km: 0.0},      
 #           "min_t":{nimetus:"",
#                     inv_nr:"",
#                     hind: 0.0,
#                     hind_km: 0.0}
#            }
#otsas_toode:{}                          otsas_toode
#ladu_neto = 0.0                         
#ladu_neto_uus = 0                              KM_valideerimine
#bruto = 0.0                           ladu_neto+=hind       ladu_neto_uus+=hind
#bruto_vana = 0.0                      bruto_vana            bruto+=...

from pprint import pprint
    
def loe_read(failinimi, kodeering="utf-8"):
    with open(failinimi, encoding=kodeering) as f:
        next(f, None)
        for rida in f:
            yield rida.rstrip("\n")


def lisa_toode(nimekiri, toode):
    nimekiri.append({
        'inventari_nr': toode[0],
        'nimetus': toode[1],
        'hind_km_ta': toode[2],
        'laoseis': toode[3],
        'km_maar': toode[4]
    })


toodete_arv = 0
vanad_mm = {}
otsas = []

for rida in loe_read("tooted.csv"):
    toode_rida = rida.split(";")

    toodete_arv += 1
    km = float(toode_rida[4])
    vanad_mm[km] = vanad_mm.get(km, 0) + 1

    if int(toode_rida[3]) <= 0:
        lisa_toode(otsas, toode_rida)
        
def kontrolli_eks_toode(nimekiri, toode):
    if nimekiri.get("max_t")["hind"]< toode[2]:
        lisa_toode(
    
print("Tooteid kokku:", toodete_arv)
print("Käibemaksumäärad:", vanad_mm)
print("Otsas olevad tooted:")
for toode in otsas:
    print(nimekiri,toode)
        
