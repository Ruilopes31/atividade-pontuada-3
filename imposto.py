import os
os.system
import time

def calcular_inss(salario_bruto):

    if salario_bruto <= 1518.00:
        aliquota = 0.075
    elif 1518.01 <= salario_bruto <= 2793.88:
        aliquota = 0.09
    elif 2793.89 <= salario_bruto <= 4190.83:
        aliquota = 0.12
    else:
        aliquota = 0.14

    desconto_inss = salario_bruto * aliquota

    return desconto_inss

salario_bruto = float(input("Informe o salário bruto: "))
valor_inss = calcular_inss(salario_bruto)

print(f"O valor do desconto do INSS é: R${valor_inss:.2f}")