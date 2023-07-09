from palindromo import *

def substring_palindromo(palavra):
    lista_palavras = []

    for i in range(len(palavra)):
        lista_palavras.append(palavra[0:i])

    for j in lista_palavras:
        # Vamos testar se é um palindromo utilizando a função que fizemos na questao 5
        e_palindromo = anagrama_palindromo(j)
        # Pegamos somente quando o len é maior que 1, pois se permitirmos o 1, iremos pegar uma letra isolada sem significado
        if len(j) > 1:
            if e_palindromo == True:
                print(j)
            else:
                pass 

palavra = input('Digite uma palavra:')
substring_palindromo(palavra)