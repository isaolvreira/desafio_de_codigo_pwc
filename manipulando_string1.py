# Reverta as ordens das palavras nas frases, mantendo a ordem das palavras:

def inverte_ordem_das_palavras(frase):
    palavras = frase.split()
    palavras_invertidas = palavras[::-1]
    frase_invertida = ' '.join(palavras_invertidas)
    return frase_invertida

frase1 = inverte_ordem_das_palavras('Ana foi a praia')
print(frase1)

frase2 = inverte_ordem_das_palavras('Fui ao parque no final de semana.')
print(frase2)

frase3 = inverte_ordem_das_palavras('Corri para a varanda do meu apartamento, estava a procura de meu filho')
print(frase3)