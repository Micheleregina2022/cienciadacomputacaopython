n = int(input("Digite o numero maior inteiro:"))
while n >= 0:
    fatorial = 1
    while n > 1:
        fatorial = fatorial * n
        n = n - 1
    print(fatorial)
    n = int(input("Digite o numero maior que 1:"))