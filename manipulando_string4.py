# Coloque em maiúsculo a primeira letra de cada frase na string:



def capitalizar_sentences(string):
    result = ''
    capitalizar_prox = True

    for char in string:
        if capitalizar_prox and char.isalpha():
            char = char.upper()
            capitalizar_prox = False
        elif char in ['.', '!', '?']:
            capitalizar_prox = True
        elif char == ' ' and result.endswith('.'):
            capitalizar_prox = True

        result += char
    

    return result

teste1 = "ana correu. foi ao parque, e acabou se machucando. tadinha."
print(capitalizar_sentences(teste1))

teste2 = "ana correu. dançou, e comeu."
print(capitalizar_sentences(teste2))
teste3 = "elias foi ao cinema, e esqueceu sua carteira. sua memoria já não é a mesma! a vida é complicada."
print(capitalizar_sentences(teste3))