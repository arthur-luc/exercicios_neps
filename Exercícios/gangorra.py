P1, C1, P2, C2 = map(int, input().split())

lado1 = P1 * C1
lado2 = P2 * C2

if (lado1 - lado2) == 0:
    print(0)

elif lado1 > lado2:
    print(-1)

else:
    print(1)