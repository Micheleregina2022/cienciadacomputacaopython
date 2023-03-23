numero = int(input("Digite um número inteiro:"))
valor = numero % 5 and numero % 3

if valor == 0:
    print("buzz")
else:
    print(numero)