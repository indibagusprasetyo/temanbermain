def count(n,p):
    if(p==0):
        return 1
    else :
        return n * count(n, p-1)

p = int(input("Input Rank  : "))
n = int(input("Input Value :"))

print(count(n,p))