# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

while True:
    try:
        number = float(input('Digite o numero negativo ou positivo: '))
    
        if number < 0:
            print(f'O número {number} é negativo.')
        elif number > 0:
            print(f'O número {number} é positivo.')
        else:
            print('o número zero não é um número positivo nem negativo.')
    except:
        print('Erro! Digite apenas números.')
    
    sair = input('Deseja [s]air??: ').lower().startswith('s')
    
    if sair is True:
        print('Você saiu :D')
        break     
    


