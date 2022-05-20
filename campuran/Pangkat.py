

def fibonacci(N):
    if N<=1:
        return N
    else:
        return fibonacci(N-2)+fibonacci(N-1)


for i in range(0,11):
    print(fibonacci(i), end=" ")