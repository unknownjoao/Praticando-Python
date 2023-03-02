# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.


letra = input('Digite uma letra: ')

str_letra = str(letra).isalpha()
vogais = 'aeiou'

if str_letra is True:
    if len(letra) == 1:
        if letra in vogais:
            print(f'A letra {letra} é uma vogal.')
        else:
            print(f'A letra {letra} é uma consoante.')
    else:
        print('Digite apenas uma letra.')
else:
    print('Digite apenas Letras')