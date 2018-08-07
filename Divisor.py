def main():
    #x  = divisor(5,5)
    #print(x)
    #divisores(997)
    #MDC(40,21)
    #Primos(1000)
    pass

def divisor(x,y):
    if x % y == 0:
        return True
    return False

def divisores(k):
    i = 1
    lst = []
    while i <= k/2:
        x = divisor(k,i)
        if x:
            lst.append(i)
        i += 1
    lst.append(k)
    return lst

def MDC(m,n):
    mdc = 0
    ListaMaior = divisores(m)
    ListaMenor = divisores(n)

    for i in ListaMaior:
        for j in ListaMenor:
            if i == j:
                mdc = i

    print("O MDC é: ", mdc)

def Primo(k):
    lst = divisores(k)
    if len(lst) == 2:
        print("É primo", k)
        return True
    return False

def Primos(k):
    for i in range(k):
        Primo(i)

main()