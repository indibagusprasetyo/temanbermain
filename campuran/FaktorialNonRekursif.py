
def Faktorial (N) :
    if(N==0) or (N==1) :
        return 1
    else :
        Fak = N
        for i in range(2,N) :
            Fak = Fak * i
        return Fak

N = int(input("Masukan Nilai N : "))
print('Nilai Faktorial',N,'adalah',Faktorial(N))