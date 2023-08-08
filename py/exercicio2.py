def quadrado(numero: int) -> int:
    """recebe um número inteiro e retorna o quadrado desse número."""
    return numero ** 2

numero = int(input('Número: '))
print(f'O quadrado de {numero} é {quadrado(numero)}')
