def media(a: float, b:float, c:float) -> float:
      
    # Recebe tres numeros float e retorna a média aritmetica.

    return (a + b + c) / 3

    if type(a) == float and type (b) == float and type (c) == float:
      return (a + b + c) / 3
    else: 
       raise TypeError


a = float (input('Primeiro nuúmero:'))
b = float (input('Segundo número:'))
c = float (input('Terceiro número:'))
print(f'Media de {a}, {b}, e {c} é {round(media(a, b, c),2)}')