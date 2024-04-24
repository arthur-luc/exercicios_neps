def main():
    # Seu código vai aqui
    vezes = int(input())
    nums = list(map(float, input().split()))

    for i in nums:
        print('%.4f' %(i ** 0.5))

if __name__ == "__main__":
    main()
