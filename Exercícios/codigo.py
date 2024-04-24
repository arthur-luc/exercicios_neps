def main():
    # Seu código vai aqui
    vezes = int(input())
    nums = list(map(int, input().split()))
    contador = 0

    for i in range(vezes):
        if len(nums) <= 2:
            break

        if nums[0] == 1 and len(nums) > 2:
            if nums[1] == 0:
                if nums[2] == 0:
                    contador += 1
        
        del nums[0]

    print(contador)

if __name__ == "__main__":
    main()
