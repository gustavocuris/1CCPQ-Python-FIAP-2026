#  Localizando o Workspace do Python (Diretório):
import os
print("O caminho é:", os.getcwd())

# Leitura de Arquivos:
# TXT
import pandas

dados1 = pandas.read_csv("DadosAula(2).txt", sep= ";", header=0)
print(f"\n {dados1}")

dados2 = pandas.read_csv("DadosAula(2).csv", sep= ";", header=0)
print( f"\n {dados2}")

dados3 = pandas.read_excel("DadosAula(2).xlsx", engine= "openpyxl")
print( f"\n {dados3}")