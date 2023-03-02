nome =  'Luiz Otávio'
tamanho_nome = len(nome)

print(nome)
print(tamanho_nome)
contador = 0
novo_nome = ''
while contador <= tamanho_nome:
    print('*')
    contador = 0
    novo_nome += nome[contador]
    contador += 1
    
print(novo_nome)
