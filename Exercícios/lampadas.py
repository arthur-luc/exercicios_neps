def main():
    # Seu código vai aqui
    A = 0
    B = 0

    vezes = int(input())
    N = list(map(int, input().split()))

    for i in N: 
        if i == 1:
            if A == 0:
                A = 1
            else:
                A = 0
        else:
            if A == 0 and B == 0:
                A = 1
                B = 1
            
            elif A == 0 and B == 1:
                A = 1
                B = 0

            elif A == 1 and B == 1:
                A = 0
                B = 0
            
            else:
                A = 0
                B = 1
    print(A)
    print(B)

if __name__ == "__main__":
    main()
