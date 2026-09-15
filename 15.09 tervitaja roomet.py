# nimekiri = [1, 2, 3, 4]
# vanus1 = 5
# pilsneri_hind = 1.203
# print(type(nimekiri))
# print(type(vanus1))
# print(type(pilsneri_hind))
# nimi = "Roomet" # string muutuja
# print(type(nimi))
# print(nimi + nimi)

# nimi = input("Mis su nimi?")
# sunniaasta = int(input("mis aastal sa sundisid?"))
# int inputi ees muudab inputi objekti tüübi arvutatavateks numbriteks. arvutus ei töötaks muidu.
# vanus = (2026 - sunniaasta)
# print("tere", nimi ,"sa oled umbes", vanus ,"aastat vana.")


# vanus = 98
# lause = f"Jaak Paak {vanus+3}, tal maitseb kartul"
# print(lause)
# f string, saab teha arvutusi lause sees


# nimi = input("Mis su nimi?")
# sunniaasta = int(input("mis aastal sa sundisid?"))
# int inputi ees muudab inputi objekti tüübi arvutatavateks numbriteks. arvutus ei töötaks muidu.
# print(f"tere {nimi} sa oled umbes {2026 - sunniaasta} aastat vana.")


def kontrollitav(vanuse_kontroll):
    vanused = {14: "suudiv",
               16: "kov",
               18: ["rk", "olu"],
               21: "kasiino",
               24: "A kat",
               40: "president"
               }
    for vanus_nimekirjast in vanused.keys():
        if vanuse_kontroll >= vanus_nimekirjast:
            print(vanused[vanus_nimekirjast])
        
       
nimi = input("Mis su nimi?")
sunniaasta = int(input("mis aastal sa sundisid?"))
vanus = (2026 - sunniaasta)
print(f"tere {nimi} sa oled umbes {2026 - sunniaasta} aastat vana.")

kontrollitav(vanus)



