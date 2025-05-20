import os
from dataclasses import dataclass
os.system(" cls || clear")


@dataclass
class Funcionario:
    nome: str
    cpf:str
    cargo:str
    salario:str


def cadastrar_fun(lista_funcionario):
    print("\n--- Cadastrar novo funcionario ---")
    funcionario = Funcionario(
        nome= input("Nome:"),
        cpf= input("Cpf:"),
        cargo= input("Cargo:"),
        salario= input("Salario:")        
    )
    
    lista_funcionario.append(funcionario)
    print()





def atualizar(lista):
    if verificar_lista_vazia(lista):
        return
   
    nome_atualizar = input("Digite o nome do funcionário que deseja atualizar: ")
    encontrado = False
   
    for funcionario in lista:
        if funcionario.nome == nome_atualizar:
            print("= Digite os dados do funcionário = ")
            funcionario.nome=input("Nome: "),
            funcionario.cpf=input("CPF: "),
            funcionario.cargo=input("Cargo: "),
            funcionario.salario=input("Salario: ")
            encontrado = True
            break