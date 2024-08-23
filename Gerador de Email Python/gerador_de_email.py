# Script de automação em Python
# Autor: Kelven Patrick Novaes Barbosa
# Data: 13-08-2024
# Descrição: esse escript de automação feito em python faz analise de dados e envia por email.

# bibliotecas utilizadas nesse projeto!
# * yfinance
# * pyautogui
# * webbrowser
# * pyperclip

# importando o yfinance
import yfinance

# digitar a entrada ex: `PETR4.SA`` Petróleo Brasileiro S.A.
ticker = input("Digite o Código da ação desejada: ")

dados = yfinance.Ticker(ticker).history(start="2024-01-01", end="2024-07-01")
fechamento = dados.Close
fechamento.plot()

# `round` = cria aredondamentos de casas decimais.
minima = round(fechamento.min(), 2)
media = round(fechamento.mean(), 2)
maxima = round(fechamento.max(), 2)

# mostrar os dados coletados
print(minima)

print(media)
print(maxima)

# importar as bibliotecas
import pyautogui
import pyperclip
import webbrowser
import time

# dados para enviar o email
destinatario = "kelvenpatricknb@gmail.com"
assunto = "Teste de automação com Python"
mensagen = f"""
Prezado XXX

Segue os dados solicitados {ticker}

Cotação mínima: R${minima}
Cotação média: R${media}
Cotação máxima: R${maxima}


Qualquer duvida estou à disposição!

Atte. Kelven Patrick
"""
# abrir o navegador e ir para o email
webbrowser.open("www.gmail.com")
time.sleep(4)

# configurando uma pausa de
pyautogui.PAUSE = 3

# clicar no botão escrever
pyautogui.click(x=90, y=182)

# digitar o email do destinatário e teclar TAB
pyperclip.copy(destinatario)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

# digitar o assunto do email
pyperclip.copy(assunto)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

# digitar a mensagem do corpo do email
pyperclip.copy(mensagen)
pyautogui.hotkey("ctrl", "v")

# clicar no botão enviar
pyautogui.click(x=767, y=988)


# aqui realizamos a capitura do mouse na tela onde clicar
# time.sleep(5)
# pyautogui.position()

# Fim do Porcesso.
