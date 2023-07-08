# Verifique se a string é um anagrama de um palindromo. 

def anagrama_de_um_palindromo(palavra):
    palavra = palavra.lower()
    # Verifica se é um palíndromo
    for i in range(len(palavra)):
        palindromo = False 
        repete = False 
        if palavra[i] == palavra[-(i+1)]:
            repete = True
            palindromo = True 

    if palindromo == True:
        return True
    else:
        return False


teste1 = anagrama_de_um_palindromo('Radar')
print(teste1)
teste2 = anagrama_de_um_palindromo('Ovo')
print(teste2)
teste3 = anagrama_de_um_palindromo('Frango')
print(teste3)