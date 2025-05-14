import os
import time
import csv
from dataclasses import dataclass

os.system("cls || clear")

# Criando a classe Funcionario 
@dataclass
class Funcionario:
    nome: str
    funcao: str
    pagamento: str

# Lista de Funcionarios
cadastro = []

# Verifica se a lista está vazia
def checar_lista_vazia(lista):
    if not lista:
        print("\nNenhum registro encontrado.")
        return True
    return False

# Adicionar novo Funcionario
def incluir_Funcionario(lista):
    nome = input("Informe o nome do Funcionario: ")
    funcao = input("Informe a função: ")
    pagamento = input("Informe o pagamento: ")

    novo = Funcionario(nome, funcao, pagamento)
    lista.append(novo)

    print(f"\nFuncionario {nome} incluído com sucesso.")

# Exibir todos os Funcionarios
def exibir_Funcionarios(lista):
    if checar_lista_vazia(lista):
        return

    print("\n- Lista de Funcionarios -")
    for pessoa in lista:
        print(f"- Nome: {pessoa.nome} | Função: {pessoa.funcao} | Pagamento: {pessoa.pagamento}")

# Atualizar informações
def editar_Funcionario(lista):
    if checar_lista_vazia(lista):
        return

    antigo_nome = input("Digite o nome do Funcionario a ser editado: ")
    for pessoa in lista:
        if pessoa.nome == antigo_nome:
            novo_nome = input("Novo nome: ")
            nova_funcao = input("Nova função: ")
            novo_pagamento = input("Novo pagamento: ")

            pessoa.nome = novo_nome
            pessoa.funcao = nova_funcao
            pessoa.pagamento = novo_pagamento

            print(f"\nDados de {antigo_nome} foram atualizados.")
            return

    print(f"\nNão foi possível encontrar {antigo_nome}.")

# Remover Funcionario
def remover_Funcionario(lista):
    if checar_lista_vazia(lista):
        return

    nome_excluir = input("Digite o nome do Funcionario que deseja excluir: ")
    for pessoa in lista:
        if pessoa.nome == nome_excluir:
            lista.remove(pessoa)
            print(f"\nFuncionario {nome_excluir} excluído com sucesso.")
            return

    print(f"\n{nome_excluir} não foi encontrado na lista.")

# Salvar em arquivo CSV
def gravar_arquivo(lista):
    with open("Funcionarios.csv", "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["nome", "funcao", "pagamento"])
        for pessoa in lista:
            escritor.writerow([pessoa.nome, pessoa.funcao, pessoa.pagamento])
    print("\nRegistros salvos em 'Funcionarioes.csv'.")

# Carregar do CSV
def carregar_arquivo(lista):
    try:
        with open("Funcionarios.csv", "r", encoding="utf-8") as arquivo:
            leitor = csv.reader(arquivo)
            next(leitor)
            for linha in leitor:
                nome, funcao, pagamento = linha
                lista.append(Funcionario(nome, funcao, pagamento))
        print("\nDados carregados com sucesso.")
    except FileNotFoundError:
        print("\nArquivo 'Funcionarios.csv' não foi encontrado.")

# Menu principal
while True:
    print("""
    - Sistema de Cadastro de Funcionarios -
    1 - Incluir Funcionario
    2 - Exibir Funcionarios
    3 - Editar Funcionario
    4 - Remover Funcionario
    5 - Gravar Arquivo
    6 - Carregar Arquivo
    7 - Sair
    """)

    try:
        escolha = int(input("Escolha uma opção: "))
    except ValueError:
        print("\nEntrada inválida. Digite um número.")
        time.sleep(2)
        os.system("cls || clear")
        continue

    match escolha:
        case 1:
            incluir_Funcionario(cadastro)
        case 2:
            exibir_Funcionarios(cadastro)
        case 3:
            editar_Funcionario(cadastro)
        case 4:
            remover_Funcionario(cadastro)
        case 5:
            gravar_arquivo(cadastro)
        case 6:
            carregar_arquivo(cadastro)
        case 7:
            print("\nEncerrando o sistema.")
            break
        case _:
            print("\nOpção inválida. Tente novamente.")

    if escolha != 1:
        time.sleep(5)
    os.system("cls || clear")
