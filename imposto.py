import os
os.system ("cls || clear")

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






def calcular_irrf(salario_bruto):

    if 2259.21 <= salario_bruto <= 2826.65:
        aliquota = 0.075
    elif  2826.65 <= salario_bruto <= 3751.05:
        aliquota = 0.15
    elif 3751.05 <= salario_bruto <= 4664.68:
        aliquota = 0.225
    else:
        aliquota = 0.275

    desconto_irrf = salario_bruto * aliquota

    return desconto_irrf

salario_bruto = float(input("Informe o salário bruto: "))
valor_inss = calcular_inss(salario_bruto)
valor_irrf = calcular_irrf(salario_bruto)
print(f"O valor do desconto do INSS é: R${valor_inss:.2f}")

print(f"O valor do desconto do Irrf é: R${valor_irrf:.2f}")
