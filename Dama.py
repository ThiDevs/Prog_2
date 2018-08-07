def main():
    print(posicao(4,4,4,4))

def posicao(x,y,m,n):



    X = False
    Y = False

    if x == m:
        X = True
    if y == n:
        Y = True

    if X and Y:
        return 0




main()