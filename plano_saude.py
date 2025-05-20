import os
import time

os.system("cls" if os.name == "nt" else "clear")

# Constantes
MATRICULA_CORRETA = "ronyrustico"
SENHA_CORRETA = "bicicleta"
DEDUCAO_DEPENDENTE_IRRF = 189.59
DESCONTO_PLANO_SAUDE_POR_DEPENDENTE = 150.00
TETO_INSS = 8157.41
MAX_DESCONTO_INSS = 1142.04

# Funções
def calcular_inss(salario):
    if salario <= 1518.00:
        return salario * 0.075
    elif salario <= 2793.88:
        return salario * 0.09 - 113.85
    elif salario <= 4190.83:
        return salario * 0.12 - 189.54
    elif salario <= TETO_INSS:
        return salario * 0.14 - 318.38
    else:
        return MAX_DESCONTO_INSS

def calcular_irrf(salario, dependentes):
    base_calculo = salario - (dependentes * DEDUCAO_DEPENDENTE_IRRF)
    if base_calculo <= 2259.20:
        return 0.0
    elif base_calculo <= 2826.65:
        return base_calculo * 0.075 - 169.44
    elif base_calculo <= 3751.05:
        return base_calculo * 0.15 - 381.44
    elif base_calculo <= 4664.68:
        return base_calculo * 0.225 - 662.77
    else:
        return base_calculo * 0.275 - 896.00

def calcular_vale_transporte(salario, opta):
    return salario * 0.06 if opta == "s" else 0.0

def calcular_vale_refeicao(valor_refeicao):
    return valor_refeicao * 0.20

def calcular_plano_saude(dependentes):
    return dependentes * DESCONTO_PLANO_SAUDE_POR_DEPENDENTE

# Autenticação
while True:
    matricula = input("Digite sua matrícula: ")
    if matricula == MATRICULA_CORRETA:
        break
    print("Matrícula incorreta.\n")

while True:
    senha = input("Digite sua senha: ")
    if senha == SENHA_CORRETA:
        break
    print("Senha incorreta.\n")

time.sleep(1)
print("\nLogin realizado com sucesso!\n")

# Entradas
salario_base = float(input("Informe seu salário base: R$ "))
vale_transporte = input("Deseja receber vale transporte? (s/n): ").lower()
valor_vale_refeicao = float(input("Informe o valor total do vale refeição fornecido pela empresa: R$ "))
qtd_dependentes = int(input("Informe a quantidade de dependentes: "))

# Cálculos
desconto_inss = calcular_inss(salario_base)
desconto_irrf = calcular_irrf(salario_base, qtd_dependentes)
desconto_transporte = calcular_vale_transporte(salario_base, vale_transporte)
desconto_refeicao = calcular_vale_refeicao(valor_vale_refeicao)
desconto_plano_saude = calcular_plano_saude(qtd_dependentes)

total_descontos = desconto_inss + desconto_irrf + desconto_transporte + desconto_refeicao + desconto_plano_saude
salario_liquido = salario_base - total_descontos

# Resultados
print("\n===== RESUMO DA FOLHA DE PAGAMENTO =====")
print(f"Salário Base: R${salario_base:.2f}")
print(f"Desconto INSS: R${desconto_inss:.2f}")
print(f"Desconto IRRF: R${desconto_irrf:.2f}")
print(f"Desconto Vale Transporte: R${desconto_transporte:.2f}")
print(f"Desconto Vale Refeição: R${desconto_refeicao:.2f}")
print(f"Desconto Plano de Saúde (dependentes): R${desconto_plano_saude:.2f}")
print(f"Total de Descontos: R${total_descontos:.2f}")
print(f"Salário Líquido: R${salario_liquido:.2f}")
