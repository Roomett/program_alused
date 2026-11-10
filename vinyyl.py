def loe_fail(failinimi):
    with open(failinimi, encoding="utf-8") as f:
        for rida in f:
            if rida.strip():
                yield [osa.strip() for osa in rida.split(",")]
            

def kysi_kasutaja_sisendit(kysimus):
    return input(f"{kysimus}:")


def tingimuste_kontroll(kogumik, kasutaja_zanr=None, kasutaja_aasta=None):
   lst = []
   for pealkiri, zanr, aasta in kogumik:
       if zanr.lower() == kasutaja_zanr.lower():
           lst.append((pealkiri,zanr,aasta))
       if aasta == kasutaja_aasta:
            lst.append((pealkiri,zanr,aasta))
   return lst 
    
def naita_kasutajale(kogumik):
    for pealkiri, zanr, aasta in kogumik:
        print(f"{pealkiri}, {zanr}, {aasta}")
 
 
kogumik= loe_fail("kogumik.txt")      
zanr = kysi_kasutaja_sisendit("Mis zanri otsid?")
aasta = kysi_kasutaja_sisendit("Mis aastat otsid?")
filtreeritud_kogumik = tingimuste_kontroll(kogumik, zanr, aasta)
naita_kasutajale(filtreeritud_kogumik)