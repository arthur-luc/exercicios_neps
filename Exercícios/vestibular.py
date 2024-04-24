def main():
    # Seu código vai aqui
    vezes = int(input())
    gabarito = input()
    respostas = list(input())
    contador = 0

    for letra in gabarito:
        if len(respostas) < 1:
            break

        if respostas[0] == letra:
            contador += 1
        
        del respostas[0]

    print(contador)


if __name__ == "__main__":
    main()
