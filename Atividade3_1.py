numeros = []
for numero in range(1000,2001):
    if numero % 11 == 5:
        numeros.append(numero)
        print('Números entre 1000 e 2000 que divididos por 11 produzem resto 5:')
        for numero in numeros:
            print(numero)