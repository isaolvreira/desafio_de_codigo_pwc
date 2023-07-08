'''Encontre a substring palindroma mais longa na string abaixo:
String palindromo na definição: Uma palavra é dita palíndroma 
quando possui o mesmo significado se lida da esquerda para  adireita
ou da direita para a esquerda.
Ex: 
a) Input: "badab"
b) Output: "Bab"(Observação: Pode haver várias saídas validas, você
só precisa retornar uma delas.)'''

def encontrar_substring_palindroma():
    string = str(input('Digite uma frase: '))

    substring_palindroma_mais_longa = ""

    for i in range(len(string)):
        for j in range(i+1, len(string)+1):
            substring = string[i:j]
            if substring == substring[::-1] and len(substring) > len(substring_palindroma_mais_longa):
                substring_palindroma_mais_longa = substring

    return substring_palindroma_mais_longa
substring_palindroma = encontrar_substring_palindroma()
print(substring_palindroma)


print1 = encontrar_substring_palindroma