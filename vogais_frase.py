frase = input('Por favor, digite uma frase ')
lista, soma, vogais = list(frase), 0, 'aeiouAEIOUáàãâéêíóõôúÁÀÃÂ'
for vogal in vogais:
    soma += lista.count(vogal)
print(f'"{frase}" possui {soma} vogais')

if frase == '':
    palavras = 0
else:
    palavras = 1
for caracter in frase:
    if caracter == ' ':
        palavras += 1
print(f'"{frase}" possui {palavras} palavras')
