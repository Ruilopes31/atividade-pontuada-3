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





def excluir(lista):
    if verificar_lista_vazia(lista):
        return
   
    nome_excluir = input("Digite o nome do funcionário: ")
    for funcionario in lista_funcionarios:
        if funcionario.nome == nome_excluir:
            lista_funcionarios.remove(nome_excluir)
            print("Funcionário excluído com sucesso.")
        else:
            print("Funcionário não encontrado.")
   
