#Faça um Programa que leia três números e mostre o maior e o menor deles.

try:
    numero_1 = float(input('Digite o primeiro número: '))
    numero_2 = float(input('Digite o segundo número: '))
    numero_3 = float(input('Digite o terceiro número: '))

    if numero_1 > numero_2 and numero_1 > numero_3:
        print('O maior número é: ' , numero_1)
    elif numero_2 > numero_1 and numero_2 > numero_3:
        print('O maior número é: ' , numero_2)
    elif numero_3 > numero_1 and numero_3 > numero_2:
        print('O maior número é: ' , numero_3)
    else:
        print('Os três números são iguais.')
        
    if numero_1 < numero_2 and numero_1 < numero_3:
        print('O menor número é: ' , numero_1)
    elif numero_2 < numero_1 and numero_2 < numero_3:
        print('O menor número é: ' , numero_2)
    elif numero_3 < numero_1 and numero_3 < numero_2:
        print('O menor número é: ' , numero_3)
    
except:
    print('Erro! Digite apenas números.')