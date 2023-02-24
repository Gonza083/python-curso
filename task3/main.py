def numeros_primos(n):
    primos = []
    for numero in range(2, n+1):
        es_primo = True
        for divisor in range(2, int(numero/2)+1):
            if numero % divisor == 0:
                es_primo = False
                break
        if es_primo:
            primos.append(numero)
    return primos


numero = int(input("Introduce el numero "))
print(numeros_primos(numero))
