def main():
    # Seu código vai aqui
    X = int(input())
    vezes = list(range(1, X+1))
    divisores = []

    for i in vezes:
        if X % i == 0:
            divisores.append(i)

    for i in divisores:
        print(i, end=' ')

if __name__ == "__main__":
    main()
