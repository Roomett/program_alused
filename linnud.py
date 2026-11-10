def linnud_sõnastikku(failinimi):
    sonastik = {}

    fail = open(failinimi+".txt", encoding="utf-8")

    for rida in fail:
        rida = rida.strip()
        osad = rida.split(",")

        liik = osad[0]   #linnu nimi
        arv = int(osad[1]) # arv

        sonastik[liik] = arv
    
    fail.close()
    
    return sonastik

failinimi = input("Sisesta failinimi: ")
linnud = linnud_sõnastikku(failinimi)
piir = int(input("Sisesta alampiir:"))

def alampiir_linnud(alampiir):
    lst=[]
    for liik in linnud:
        arv = linnud[liik]
        if arv > alampiir:    
            lst.append((liik, arv))
    return lst
            
             
print (alampiir_linnud)
  