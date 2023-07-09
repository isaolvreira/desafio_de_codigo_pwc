def anagrama_palindromo(palavra):
    palindromo = False
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