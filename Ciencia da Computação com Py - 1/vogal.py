def vogal(z):
    vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    if z in vogais:
        return True
    else:
        return False

#debugando#

resultado = vogal("U")
print(resultado)

resultado = vogal("f")
print(resultado)