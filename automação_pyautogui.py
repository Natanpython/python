
# Passo a passo do projeto.
import pyautogui
from time import sleep
import pandas
import numpy
import openpyxl


# 1 - entrar no sistema da empresa.
# https://dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.PAUSE = 10
# pip install pyautogui
# clicar -> pyautogui.click
# escrever -> pyautogui.write
# apertar uma tecla -> pyautogui.press
# apertar -> pyautogui.hotkey
#scroll (rolar pagina) -> pyautogui.scroll

pyautogui.press('win')

pyautogui.write('Navegador Opera gx')

pyautogui.press('enter')
sleep(7)
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
pyautogui.write(link)

pyautogui.press('enter')

sleep(5)

pyautogui.click(x=509, y=358)

# 2 - fazer login.
sleep(5)
pyautogui.write('natanael@gmail.com')

pyautogui.press('tab')

pyautogui.write('1234')

pyautogui.press('enter')

# 3 - importar base de dados.
tabela = pandas.read_csv('produtos.csv')

for linha in tabela.index:

    # 4 - cadastar um produto.
    pyautogui.click(x=566, y=240)

    codigo = tabela.loc[linha, "codigo"]
    #codigo do produto
    pyautogui.write(codigo)
    pyautogui.press('tab')
    #marca do produto
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press('tab')
    #tipo do produto
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press('tab')
    #categoria do produto
    pyautogui.write(str(tabela.loc[linha, "categoria"])) #duas formas de cadastrar numero (str('1')) ou apenas ('1').
    pyautogui.press('tab')
    #Preço Unitário do Produto
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press('tab')
    #Custo do Produto
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press('tab')
    #observação
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna('obs'):
        pyautogui.write(obs)
    pyautogui.press('tab')
    pyautogui.press('enter')

    pyautogui.scroll(5000)





# 5 - cadastar todos.ail.com



