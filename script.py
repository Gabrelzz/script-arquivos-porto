from renomeador import renomear, arquivos_renomear
import pyautogui
import time
import sys
import os 
import subprocess
import keyboard
import tkinter as tk
from tkinter import PhotoImage, messagebox

''' Renomear todos os arquivos '''
renomear()
time.sleep(1)

''' Definindo funções '''
# Função para fechar janela 
def fechar():
    if messagebox.askokcancel("Fechar", "Você realmente deseja fechar?"):
        sys.exit()
    else:
        print("Você não deseja fechar.")

# Função botão SIM
def continuar():
    abrir_pasta()
    iniciar_script()
    f4()
    encerrar_script()

# Função botão NÃO
def fechar_janela():    
    sys.exit()

# Centralizar a janela
def centralizar_janela(root,largura, altura):
    largura_tela = root.winfo_screenwidth()
    altura_tela = root.winfo_screenheight()

    # Calcular a posição x e y para centralizar a janela
    x = (largura_tela / 2) - (largura / 2)
    y = (altura_tela / 2 ) - (altura / 2)

    root.geometry(f'{largura}x{altura}+{int(x)}+{int(y)}')

def abrir_pasta():
    pasta_script = os.path.dirname(os.path.abspath(__file__))
    subprocess.Popen(f'explorer {os.path.realpath(pasta_script)}')
    time.sleep(2)

def f4():
    pyautogui.hotkey('alt', 'f4')

def encerrar_script():
    # Exibir mensagem ou notificação dizendo que o script já foi utilizado
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Finalização do Script", "O script foi concluído com sucesso.")
    # Encerrar script
    sys.exit()

''' Criar a janela Tkinter '''
root = tk.Tk()
root.title("Aviso!")
root.resizable(False, False)
icone = PhotoImage(file="icone.png")
root.iconphoto(True, icone)
largura_janela = 400
altura_janela = 200
centralizar_janela(root, largura_janela, altura_janela)


# Caixa de aviso
messagem = tk.Label(root, text="Antes de inicializar o script, garanta que o Excel está em tela cheia para um bom funcionamento.\n\nVocê deseja continuar?", wraplength=350)
messagem.pack(pady=20)

# Configurando botões de SIM e NÃO
botao_frame = tk.Frame(root)
botao_frame.pack(pady=20)

botao_sim = tk.Button(botao_frame, text="Sim", command=continuar)
botao_sim.pack(side=tk.LEFT, padx=10)

botao_nao = tk.Button(botao_frame, text="Não", command=fechar_janela)
botao_nao.pack(side=tk.RIGHT, padx=10)

def iniciar_script():
    i = 0
    while i < len(arquivos_renomear):

        # Acessar um arquivo e ir para o próximo
        pyautogui.press('[')
        time.sleep(1)
        pyautogui.press('enter')

        #Aguardar abrir excel
        time.sleep(3)

        # Acessar primeira coluna
        pyautogui.hotkey('ctrl', 'space')
        time.sleep(1)

        # Clickar em Dados
        pyautogui.click(x=556, y=82)
        time.sleep(1)

        # Clickar em Texto para colunas
        pyautogui.click(x=1059, y=147)
        time.sleep(1)

        # Clickar em delimitado
        pyautogui.click(x=1010, y=442)
        time.sleep(1)

        # Avançar 
        pyautogui.click(x=1510, y=795)
        time.sleep(1)

        # Clickar em Outros
        pyautogui.click(x=987, y=517)
        time.sleep(1)

        # Digitar o caractér "pipe" / "|"
        pyautogui.write('|')
        time.sleep(1)

        # Clickar em avançar
        pyautogui.click(x=1508, y=799)
        time.sleep(1)

        # Clickar em concluir
        pyautogui.click(x=1645, y=802)
        time.sleep(1)

        # Salvar
        pyautogui.hotkey('ctrl', 'b')
        time.sleep(1)

        # Fechar o Excel
        pyautogui.hotkey('alt', 'f4')
        time.sleep(1)
        i += 1

# Mensagem para exibir mostrando que foi finalizado o script!

# Configurar fechamento da janela
root.protocol("WM_DELETE_WINDOW", fechar)

# Manter o loop da janela
root.mainloop()