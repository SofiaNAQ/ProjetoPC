import os
import time

#faz a importacão do modulo prettytable
from prettytable import PrettyTable
from prettytable import from_csv
from prettytable import from_html

#classe de funcoes do adm

class functionsADM:

    def open(self):

        login = "admin@2020"
        senha="admin"

        print("==========LOGIN=============")
        
        VeLogin = str(input("Login: "))
        VeSenha = str(input("Senha: "))

        if VeLogin == login and VeSenha == senha:
            status= "open"
            return status 
        else:
            status = "closed"
            return status 

    def ceduls_control(self, numberCels):

        min_ = 2000

        if numberCels < min_ :
            status = 0
            return status
        else:
            status = 1
            return status

    def take_ceduls(self):
        nceduls = int(input("Número de cédulas no caixa: "))
        return nceduls



    def createOpTable(self):
        # Cria a tabela
        tableOp = PrettyTable(["Id da operação", "Data", "Description"])

        # Alinha as colunas
        tableOp.align["Id da operação"] = "l"
        tableOp.align["Data"] = "l"
        tableOp.align["Description"]="l"

        # Deixa um espaço entre a borda das colunas e o conteúdo (default)
        tableOp.padding_width = 1

        return tableOp

    def takeOperation(self, idOp, date, desc, nomeT):

        nomeT.add_row([idOp, date, desc]) #nomeT deve ser uma constante que guarda tableOP 

        

    def sangria(self):

        valor_ = int(input("Valor da sangria: "))

        return valor_