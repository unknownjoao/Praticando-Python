'''
Faça um programa para a leitura de duas notas parciais de um aluno.
O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.
'''

try:
    nota_parcial = float(input('Nota parcial: '))
    nota_bimestral = float(input('Nota bimestral: '))
    
    if nota_parcial in range(0, 11) and nota_bimestral in range(0, 11):
        media = (nota_parcial + nota_bimestral) / 2
    
        if media == 10:
            print('Sua média é ', media)
            print('Aprovado com Distinção!')
        elif media >= 7:
            print('Sua média é ', media)
            print('Aprovado!')
        else:
            print('Sua média é ', media)
            print('Reprovado!')
    else:
        print('Nota somente de 0 a 10')
    
except:
    print('Erro! Tente digitar somente numeros de 0 a 10.')
    