def main():
    # Seu código vai aqui
    a, b, c = map(int, input().split())

    if a != b and a != c:
        print('A')

    elif b != a and b != c:
        print('B')

    elif c != a and c != b:
        print('C')

    else: 
        print('*')

if __name__ == "__main__":
    main()
