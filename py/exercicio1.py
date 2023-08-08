def somar (numero1: float, numero2: float) -> float:
    """Recebe dois numeros float e retorna a soma desses dois numeros."""
    return numero1 + numero2


a = float (input('Primeiro Numero:'))
b = float (input('Segundo Número:'))
print (f'Soma de {a} e {b} é {somar(a, b)}')