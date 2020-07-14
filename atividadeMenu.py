import os
import time
from transactions import Transactions
import functions as fun
from datetime import date

transf = Transactions(1)
func = fun.functionsADM()
gatilho = 0
# ------------------------------------- Área de administração ------------------------------------------------
def principalADM():
    nceduls= func.take_ceduls()
    tableOp = func.createOpTable()
    data_atual = date.today()
    while True:
        try:
            time.sleep(3)
            os.system("cls")
            print(" === MÓDULO ADMINISTRATIVO === ")
            print("1 - Alimentação de cédulas")
            print("2 - Emitir relatório")
            print("3 - Sangria")
            print("4 - Log-out")
            opcao = int(input("Digite o Opção Desejada:"))


            if opcao == 4:
                print('\033[31m'"\n Saindo do Programa..."'\033[0;0m')
                break

            elif opcao ==1:
                func.takeOperation(1,data_atual,"Alimentação de cédulas",tableOp)
                statusC = func.ceduls_control(nceduls)
                if statusC == 1:
                    print('\033[32m'+"Tudo ok com as notas"+'\033[0;0m')
                else:
                    print('\033[31m'+"Reposição necessária!"+'\033[0;0m')
                    
            elif opcao ==2:
                func.takeOperation(2,data_atual,"Emissão de relatório",tableOp)
                print("================================")
                print(tableOp)
                print('\033[32m'+"Emitindo documento..."+'\033[0;0m')
                arquivo = open('relatorioDeOperacoes.txt', 'w')
                arquivo.write(str(tableOp))
                arquivo.close()

            elif opcao ==3:
                valor_S = func.sangria()
                desc = "Sangria", valor_S
                func.takeOperation(3,data_atual,desc,tableOp)
                print('\033[32m'+"Aguarde enquanto é registrado..."+'\033[0;0m')

        except ValueError:
            print("Não foi possivel realizar esta operação",)


    data_atual = date.today()
    while True:
        try:
            time.sleep(3)
            os.system("cls")
            print(" === MÓDULO ADMINISTRATIVO === ")
            print("1 - Alimentação de cédulas")
            print("2 - Emitir relatório")
            print("3 - Sangria")
            print("4 - Log-out")
            opcao = int(input("Digite o Opção Desejada:"))


            if opcao == 4:
                print('\033[31m'"\n Saindo do Programa..."'\033[0;0m')
                break

            elif opcao ==1:
                func.takeOperation(1,data_atual,"Alimentação de cédulas",tableOp)
                statusC = func.ceduls_control(nceduls)
                if statusC == 1:
                    print('\033[32m'+"Tudo ok com as notas"+'\033[0;0m')
                else:
                    print('\033[31m'+"Reposição necessária!"+'\033[0;0m')
                    
            elif opcao ==2:
                func.takeOperation(2,data_atual,"Emissão de relatório",tableOp)
                print("================================")
                print(tableOp)
                print('\033[32m'+"Emitindo documento..."+'\033[0;0m')
                arquivo = open('relatorioDeOperacoes.txt', 'w')
                arquivo.write(str(tableOp))
                arquivo.close()

            elif opcao ==3:
                valor_S = func.sangria()
                desc = "Sangria", valor_S
                func.takeOperation(3,data_atual,desc,tableOp)
                print('\033[32m'+"Aguarde enquanto é registrado..."+'\033[0;0m')

        except ValueError:
            print("Não foi possivel realizar esta operação")

# ----------------------------------------- Área do cliente ------------------------------------------------

def principalCLI():
    lista = [] # inicializa a lista vazia
    while True:
        time.sleep(2)
        os.system("cls")
        print(" === MÓDULO CLIENTE === ")
        print("1 - Cadastrar Banco ou Fintech")
        print("2 - Editar Cadastro")
        print("3 - Listar Banco ou Fintech")
        print("4 - Sair do Sistema do Banco")
        opcao = int(input("Digite o Opção Desejada:"))

        if opcao == 1:
            print("\n Digite o Nome da Empresa:")
            print("\n Digite o CNPJ da Empresa:")
            print("\n Digite Localização da Empresa:")
            print("\n Digite a Inscrição Estadual da Empresa:")
            print("\n Escolher Funcionalidades: S ou N")
        # print("\n  - Saque:")
        # print("\n  - Depósito:")
        # print("\n  ...")

        if opcao == 2:
            print("\n Digite o CNPJ da Empresa:")
            print("\n Digite um Novo Nome:")
            print("\n Digite uma Nova Localização:")
            print("\n Digite uma Nova Inscrição Estadual:")
            print("\n Escolha Novas Funcionalidades:")
        # print("\n  - Saque:")
        # print("\n  - Depósito:")
        # print("\n  ...")
            print("\n Escolha o Estado do Banco:")
        # print("\n  Ativo: S ou N")

        if opcao == 3:
            #print("\n DECIDIR POR PEGAR INDIVIDUAL PELO NOME DO ARQUIVO OU COLETIVO DE TODAS EMPRESAS PELA PASTA COM TODOS ARQUIVOS ARMAZENADOS")

            #INDIVIDUAL
            print("\n Digite o CNPJ da Empresa:")

            #GERAL
            #LISTAR DIRETO
            #opção de parar de listar

        if opcao == 4:
            print("\n Saindo do Programa...")
            break

# ------------------------------------- Área de Movimentação ------------------------------------------------

def saldo():
    transf.query()

    print("\nPara imprimir digite 1")
    print("Para finalizar a consulta digite 2")
    escolha = input("Digite o número: ")
    print()

    while(escolha != "1" and escolha != "2"):
        print("Digite corretamente...")
        escolha = input("Digite o número: ")
        print()

    if(escolha == "1"):
        print("Imprimindo...\n")
        time.sleep(2)


def trans():
    transf.transference()

    t = input("\nConfirmar a transação (Digite 1 para SIM ou 2 para NÃO)\n")
    while(t != "1" and t != "2"):
        t = input("\nConfirmar transação (Digite 1 para SIM ou 2 para NÃO)\n")

    if(t == "1"):
        print("Transferência Concluída")
        time.sleep(2)
    else:
        print("Voltando para o menu...")
        time.sleep(2)


def extrato():
    print("\n Histórico das operações\n")
    transf.statement()

    input("\nPressione enter para voltar para o menu")


def principalMOV():
    while True:
        time.sleep(2)
        os.system("cls")
        print("===Banco Digital===")
        print("1 - Consulte seu saldo")
        print("2 - Realize uma transferência")
        print("3 - Consulte seu extrato")
        print("4 - Sair do sistema Banco")
        opcao = int(input("Digite o opção desejada:"))


        if opcao == 1:
            saldo()
        elif opcao == 2:
            trans()
        elif opcao == 3:
            extrato()
        elif opcao == 4:
            print("Saindo do programa...")
            break
        else:
            print("Opcão incorreta, por favor digite novamente...")

# --------------------------------------------- Funcionamento -------------------------------------------------
def principal():
    while True:
        time.sleep(2)
        os.system("cls")
        print("------- Selecione a opção desejada -------")
        print("1 - Área administrativa")
        print("2 - Área de cliente")
        print("3 - Movimentações")
        opcao = int(input("Digite a opção desejada: "))

        if opcao == 1:
            login = func.open()
                
            if login == "open": 
                gatilho = 1
                print('\033[32m'+"=========Bem-Vindo=========== "+'\033[0;0m')
                principalADM()
            else:
                print('\033[31m'+"Login inválido"+'\033[0;0m')

        elif opcao == 2:
            principalCLI()

        elif opcao == 3:
            principalMOV()
        
        else:
            print("Opcão incorreta, por favor digite novamente...")

principal()