# Faça um Programa que peça dois números e imprima o maior deles.

while True:
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
    
    if n1 > n2:
        print('o maior numero é: ', n1)
    elif n1 < n2:
        print('O maior número é: ', n2)
    else:
        print('Os dois números são iguais.')
    
    