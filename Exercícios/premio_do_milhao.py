def main():
    # Seu código vai aqui
    dias = int(input())

    soma = 0
    contador = 0
    
    while soma < 10**6:
        soma += int(input())
        contador += 1
    
    print(contador)

if __name__ == "__main__":
    main()