''' Remova todos os caracteres duplicados da string abaixo:
input: "Hello, World!
output: "Helo, World!'''

def retira_duplicatas(frase):
        # Transforma numa lista a string e cada elemento da lista é um elemento da string
    lista_frase = list(frase)

    # Flag para monitorar se repetiu
    repetida = False

    # Lista vazia para guardar as posições q houve repetição
    posicao_repetida = []

    for i in range(len(lista_frase)):
        repetida = False
        if i >0 and i+1 < len(lista_frase):
            # Verifica o elemento na posição i e o posterior
            if lista_frase[i] == lista_frase[i+1]:
                repetida = True
                lista_frase[i+1] = ','

    # Varre a lista posicao_repetida e remove da lista_frase o elemento de posição
    # igual a o numero armazenado na lista de posicao_repetida
    for j in range(len(lista_frase)):
        if j >0 and j < len(lista_frase):
            if lista_frase[j] == ',':
                lista_frase.pop(j)

    # Transformando a lista em string novamente
    string = ''.join(lista_frase)
    return string

frase1 = retira_duplicatas('Anaa foi a praiaa')
print(frase1)

frase2 = retira_duplicatas('Helo World')
print(frase2)

frase3 = retira_duplicatas('Hello World')
print(frase3)