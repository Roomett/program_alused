#set() hulk-tunnused?
def loe_nimekiri(failinimi):
    with open(failinimi, encoding="utf-8") as f:
        for rida in f:
            if rida.strip():
                yield rida.strip().lower()
                
def lisa_hulka(hulk, nimekiri):
    for produkt in nimekiri:
        hulk.add(produkt)

jaagu_nimekiri = loe_nimekiri("jaak_nimekiri.txt")
koidu_ehalend_nimekiri = loe_nimekiri("koidu-ehalend.txt")

yhis_nimekiri = set()

lisa_hulka(yhis_nimekiri, koidu_ehalend_nimekiri)
lisa_hulka(yhis_nimekiri, jaagu_nimekiri)
print(yhis_nimekiri)

jaagu_set = set([el for el in loe_nimekiri("jaak_nimekiri.txt")])
koidu_ehalend_set = set([el for el in loe_nimekiri("koidu-ehalend.txt")])


#print("yhend", jaagu_set.union(koidu_ehalend_set))   #pole tahtsust kumba kasutad, molemad tootavad
print("yhend", jaagu_set | koidu_ehalend_set)

#print("yhisosa", jaagu_set.intersection(koidu_ehalend_set))
print("yhisosa", jaagu_set & koidu_ehalend_set)

#print("vahe", jaagu_set.difference(koidu_ehalend_set))
print("vahe", jaagu_set - koidu_ehalend_set)
