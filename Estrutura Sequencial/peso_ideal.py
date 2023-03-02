'''
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
'''
print('-' * 10)
print('CALCULE SEU PESO IDEAL')
print('-' * 10)

genero = str(input('Você é Homem[M] ou Mulher[F]? '))

generos_permitidos = 'MFmf'

if genero in generos_permitidos:
    if genero == 'm':
        altura = float(input('Digite sua altura: '))
        peso_ideal = (72.7 * altura) - 58
        print('Seu peso ideal é: ', peso_ideal)
    if genero == 'f':
        altura = float(input('Digite sua altura: '))
        peso_ideal = (62.1 * altura) - 44.7
        print('Seu peso ideal é: ', peso_ideal)
if genero not in generos_permitidos:
    print('Genero inválido')








