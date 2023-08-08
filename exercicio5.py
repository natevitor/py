def calcular_salario (salario: float) -> float:

    # Calcula o salario do funcionario de acordo com o percentual de reajuste

    if salario > 2000:
        return salario + salario * 0.07
    else: 
        return salario + salario * 0.15
    
salario = float (input('Informe o seu salario:'))
print (f'Salario atualizado: {calcular_salario(salario)}')
