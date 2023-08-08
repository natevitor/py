def soma_dos_quadrados(a: int, b: int) -> int:

    # Recebe dois numeros inteiros e retorna a soma dos quadrados desses dois numeros.
    return a**2 + b**2

a = int(input('Primeiro número:'))
b = int(input('Sefundo número:'))
c = soma_dos_quadrados(a,b)
print(f'Resultados: {c}')