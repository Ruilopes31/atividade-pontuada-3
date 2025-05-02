import os
os.system
import time

def calcular_inss(salario_bruto):

    if salario_bruto <= 1412.00:
        aliquota = 0.075
    elif 1412.01 <= salario_bruto <= 2826.65:
        aliquota = 0.09
    elif 2826.66 <= salario_bruto <= 4240.00:
        aliquota = 0.12
    else:
        aliquota = 0.14

    desconto_inss = salario_bruto * aliquota

    return desconto_inss

salario_bruto = float(input("Informe o salário bruto: "))
valor_inss = calcular_inss(salario_bruto)

print(f"O valor do desconto do INSS é: R${valor_inss:.2f}")