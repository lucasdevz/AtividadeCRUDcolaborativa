# Alunos: Lucas Pereira, Victor Santana

"""
# AtividadeCRUDcolaborativa

## Objetivo
Em dupla, usando funções implemente um CRUD com os dados informados abaixo.

class funcionário:
   def __init___(self, nome, idade, cpf, setor, função, salario, telefone):

## Tecnologias:
Será necessário utilizar as tecnologias abaixo:
- ORM: SQLAlchemy
- Banco de dados: SQLite
-  Versionamento: Git

## Resultado esperado:
Um sistema onde o usuário veja um menu e escolher dentre as opções disponíveis:

   === RH System ===
1 - Adicionar funcionário
2 - Consultar um funcionário
3 - Atualizar os dados de um funcionário
4 - Excluir um funcionário
5 - Listar todos os funcionários
0 - Sair do sistema.
O menu será exibido após realizar as ações do menu.

"""
import os
from sqlalchemy import create_engine, Column, String, Integer, Float
from sqlalchemy.orm import sessionmaker, declarative_base

# Criando banco de dados.
MEU_BANCO = create_engine("sqlite:///meubanco.db")

# Criando conexão com banco de dados.
Session = sessionmaker(bind=MEU_BANCO)
session = Session()

# Criando tabela.
Base = declarative_base()

class Funcionario(Base):
    __tablename__ = "funcionarios"

    # Definindo campos da tabela.
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    idade = Column("idade", Integer)
    cpf = Column("cpf", String)
    setor = Column("setor", String)
    funcao = Column("funcao", String)
    salario = Column("salario", Float)
    telefone = Column("telefone", String)

    # Definindo atributos da classe.
    def __init__(self, nome: str, idade: int, cpf: str, setor: str, funcao: str, salario: float, telefone: str):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.setor = setor
        self.funcao = funcao
        self.salario = salario
        self.telefone = telefone

# Criando tabela no banco de dados.
Base.metadata.create_all(bind=MEU_BANCO)

def menu():
    while True:
        print("""
        === RH System ===
        1 - Adicionar funcionário
        2 - Consultar um funcionário
        3 - Atualizar os dados de um funcionário
        4 - Excluir um funcionário
        5 - Listar todos os funcionários
        0 - Sair do sistema.
        """)
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_funcionario()
        elif opcao == "2":
            consultar_funcionario()
        elif opcao == "3":
            atualizar_funcionario()
        elif opcao == "4":
            excluir_funcionario()
        elif opcao == "5":
            listar_funcionarios()
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")

def adicionar_funcionario():
    os.system("cls || clear")
    print("Adicionando novo funcionário:")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    cpf = input("CPF: ")
    setor = input("Setor: ")
    funcao = input("Função: ")
    salario = float(input("Salário: "))
    telefone = input("Telefone: ")

    funcionario = Funcionario(nome, idade, cpf, setor, funcao, salario, telefone)
    session.add(funcionario)
    session.commit()
    print("Funcionário adicionado com sucesso.")

def consultar_funcionario():
    os.system("cls || clear")
    cpf = input("Informe o CPF do funcionário: ")
    funcionario = session.query(Funcionario).filter_by(cpf=cpf).first()
    if funcionario:
        print(f"Funcionário encontrado: {funcionario.nome}, Idade: {funcionario.idade}, Setor: {funcionario.setor}, Função: {funcionario.funcao}, Salário: {funcionario.salario}, Telefone: {funcionario.telefone}")
    else:
        print("Funcionário não encontrado.")

def atualizar_funcionario():
    os.system("cls || clear")
    cpf = input("Informe o CPF do funcionário que será atualizado: ")
    funcionario = session.query(Funcionario).filter_by(cpf=cpf).first()
    if funcionario:
        funcionario.nome = input("Novo nome: ")
        funcionario.idade = int(input("Nova idade: "))
        funcionario.setor = input("Novo setor: ")
        funcionario.funcao = input("Nova função: ")
        funcionario.salario = float(input("Novo salário: "))
        funcionario.telefone = input("Novo telefone: ")
        session.commit()
        print("Funcionário atualizado com sucesso.")
    else:
        print("Funcionário não encontrado.")

def excluir_funcionario():
    os.system("cls || clear")
    cpf = input("Informe o CPF do funcionário a ser excluído: ")
    funcionario = session.query(Funcionario).filter_by(cpf=cpf).first()
    if funcionario:
        session.delete(funcionario)
        session.commit()
        print("Funcionário excluído com sucesso.")
    else:
        print("Funcionário não encontrado.")

def listar_funcionarios():
    os.system("cls || clear")
    print("Lista de Funcionários:")
    funcionarios = session.query(Funcionario).all()
    for funcionario in funcionarios:
        print(f"{funcionario.id} - {funcionario.nome} - {funcionario.idade} - {funcionario.cpf} - {funcionario.setor} - {funcionario.funcao} - {funcionario.salario} - {funcionario.telefone}")

# chamando o menu
menu()

# Fechando conexão.
session.close()