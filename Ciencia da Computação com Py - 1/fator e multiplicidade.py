# Dado um num inteiro n, n > 1, imprimir sua decomposição em fatores primos, #
# indicando tambem a multiplicidade de cada fator #
# exemplo: 8 = 2*2*2; 20 = 2*2*5; 1000 = 2^3 * 5^3 #

n = int(input('Digite um num inteiro > 1:'))

fator = 2
multiplicidade = 0

while n > 1:
    while n % fator == 0:
        multiplicidade = multiplicidade + 1
        n = n / fator
    if multiplicidade > 0:
        print('fator:', fator, 'e multiplicidade:', multiplicidade)
    fator = fator + 1
    multiplicidade = 0
