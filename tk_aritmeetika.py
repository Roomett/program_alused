
# ===== Aritmeetika =====


# A1. Ristküliku pindala ja ümbermõõt
# Tagasta list [pindala, ümbermõõt].
def ristkylik(a, b):
    
    return [(a*b),(2*a + 2*b)]


print(ristkylik(3, 4))  # expected output: [12, 14]


# A2. Keskmine
# Tagasta kolme arvu aritmeetiline keskmine.
def keskmine(a, b, c):
    
    return ((a+c+b)/3)


print(keskmine(2, 4, 9))  # expected output: 5.0


# A3. Jagamine
# Tagasta list [täisarvuline jagatis, jääk, tavaline jagatis].
# Vihje: // , % , /
def jaga(a, b):
    # Kirjuta siia implementatsioon
    return [(a//b),(a%b),(a/b)]


print(jaga(17, 5))  # expected output: [3, 2, 3.4]


# A4. Celsius -> Fahrenheit
# Valem: F = C * 9 / 5 + 32. Ümarda tulemus ühe komakohani.
def celsius_fahrenheit(c):
    # Kirjuta siia implementatsioon
    return (c* 9 / 5 + 32)


print(celsius_fahrenheit(21.5))  # expected output: 70.7
print(celsius_fahrenheit(-40))  # expected output: -40.0


# A5. Sekundid -> tunnid, minutid, sekundid
# Tagasta sõne kujul "h:mm:ss", st minutid ja sekundid alati kahekohalised.
# Vihje: // , % ja f-string vormindus {m:02d}
def aeg(s):
    # Kirjuta siia implementatsioon
    return [(s//3600),((s%3600)//60),(s%60)]
    


print(aeg(3725))  # expected output: 1:02:05
print(aeg(59))  # expected output: 0:00:59


# A6. Tüübiteisendus
# Parameetrid on sõned (nagu input() tagastab). Liida arvud kokku ja tagasta täisarv.
def liida_soned(a, b):
    # Kirjuta siia implementatsioon
    return


#print(liida_soned("12", "30"))  # expected output: 42
