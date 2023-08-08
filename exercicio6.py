def soma_divisores(numero: int) -> int:
    # Retorna a soma dos divisores de um numero

    soma = 0 
    for i in range (1, numero + 1):
        if numero % i == 0:
            print(i)
            soma += i
    return soma


numero = int(input('Informe um numnero inteiro:'))
print(f'Soma dos divisores: {soma_divisores(numero)}')