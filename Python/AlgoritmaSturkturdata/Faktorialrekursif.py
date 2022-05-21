
def Faktorial (N) :
    if(N==0) or (N==1) :
        return 1
    else :
        return N * Faktorial(N-1)

N = int(input("Masukan Nilai N : "))
print('Nilai Faktorial',N,'adalah',Faktorial(N))