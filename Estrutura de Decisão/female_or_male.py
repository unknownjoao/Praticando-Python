'''
Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
'''
try:
    
    genero = input('Digite qual o genero [M]asculino ou [F]eminino: ')

    if genero == 'F' or genero == 'f':
        print('Genero digitado é Feminino.')
    elif genero == 'M' or genero == 'm':
        print('Genero digitado é Masculino.')
    else:
        print('Sexo inválido.')
except:
    print('Erro! Digite apenas M ou F')