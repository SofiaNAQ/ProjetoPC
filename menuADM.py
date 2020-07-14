import os
import time
#importa o arquivo de functions
import functions as fun


#importa a biblioteca de data para python
from datetime import date

def principal():
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


func = fun.functionsADM()
trigger = 0

while trigger == 0:
    login = func.open()
    
    if login == "open": 
        trigger =1
        print('\033[32m'+"=========Bem-Vindo=========== "+'\033[0;0m')
        nceduls= func.take_ceduls()
        tableOp = func.createOpTable()
        principal()
    else:
        print('\033[31m'+"Login inválido"+'\033[0;0m')