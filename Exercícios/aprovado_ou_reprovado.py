A = float(input())
B = float(input())

media = (A + B) / 2

if media >= 7:
    print('Aprovado')

elif media >= 4 and media < 7:
    print('Recuperacao')

else:
    print('Reprovado')