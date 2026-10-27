import numpy as np
def print_maatriks(matrix):
    for el in matrix:
        print (el)
        
def print_peadiagonaal(matrix):
    suurus = len(matrix)
    for el in range(suurus):
        print(matrix[el][el])

def prints_vastasdiagonaal(matrix):
    suurus2 = len(matrix)
    for i in range(suurus2):
        elu = -i-1
        #print(matrix[i][elu])  #esimese rea viimase elemendi leiab sest -1 on tagantpoolt esimene element, -2 teine, jne
        print(matrix[i][suurus2 - i -1]) #laheneb maatriksile vasakult mitte lopust
    
maatriks = A = np.array ([[1,2,3],
            [4,5,6],
            [7,8,9]])

print_maatriks(maatriks)
print_peadiagonaal(maatriks)
prints_vastasdiagonaal(maatriks)
print(A * A)
