#tee 6 realine pool-puu
def kool(tarn, korgus):    
    for rida in range (korgus):    
        vasak = ((korgus-rida-1) * " " + (tarn * (rida*2 + 1)) + (korgus-rida-1) * " ")
        vahe = "|"
        parem = ((" " * (rida)) + (((korgus -1 - rida)*2 + 1) * tarn))
        print(vasak + vahe + parem)       
kool("*", 6)