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
    