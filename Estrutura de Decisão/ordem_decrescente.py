#Faça um Programa que leia três números e mostre-os em ordem decrescente.

try:
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
    n3 = float(input('Digite o terceiro número: '))
    
    lista = [n1, n2, n3]
    
    lista.sort(reverse=True)
    print(lista)
except:
    print('Error: Invalid. Digite apenas numeros')