# Ler dados da planilha
# Inserie cada célula de cada linha em um campo do sistema
import openpyxl
import pyautogui

workbook = openpyxl.load_workbook('freela/rede_publica.xlsx')
vendas_sheet = workbook['REDE PUBLICA']

for linha in vendas_sheet.iter_rows(min_row=3):
    pyautogui.click()
    print(linha[0].value)
    print(linha[1].value)
    print(linha[2].value)
    print(linha[3].value)
    print(linha[4].value)
    print(linha[5].value)

#Continuação aqui: Para cadastrar automaticamente:
   # https://www.youtube.com/watch?v=LwTbvEIOsKI&list=PLnNURxKyyLIJ5ftIIYFLNNLyCmBx5uXYM