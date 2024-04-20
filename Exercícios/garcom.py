def main():
    # Seu código vai aqui
    vezes = int(input())
    contador = 0
    copos_quebrados = 0
    lista_bandeja = []

    for i in range(vezes):
        lista_bandeja.extend(map(int, input().split()))

    while contador < vezes:
        if lista_bandeja[0] > lista_bandeja[1]:
            copos_quebrados += lista_bandeja[1]

        del lista_bandeja[0]
        del lista_bandeja[0]
        
        contador += 1


    print(copos_quebrados)

if __name__ == "__main__":
    main()
