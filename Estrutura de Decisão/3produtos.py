#Faça um programa que pergunte o preço de três produtos 
#e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

try:
    produto_1 = float(input('Digite o preço do primeiro produto: '))
    produto_2 = float(input('Digite o preço do segundo produto: '))
    produto_3 = float(input('Digite o preço do terceiro produto: '))
        
    if produto_1 < produto_2 and produto_1 < produto_3:
        print('Você deve comprar o primeiro produto.')
    elif produto_2 < produto_1 and produto_2 < produto_3:
        print('Você deve comprar o segundo produto.')
    elif produto_3 < produto_1 and produto_3 < produto_2:
        print('Você deve comprar o terceiro produto.')
    elif produto_1 == produto_2 < produto_3:
        print('Você deve comprar o primeiro ou segundo produto, pois os dois tem o mesmo preço.')
    elif produto_1 == produto_3 < produto_2:
        print('Você deve comprar o primeiro ou terceiro produto, pois os dois tem o mesmo preço.')
    elif produto_2 == produto_3 < produto_1:
        print('Você deve comprar o segundo ou terceiro produto, pois os dois tem o mesmo preço.')
    
    else:
        print('Os três produtos tem o mesmo preço.')
        
except:
    print('Erro! Digite apenas números.')