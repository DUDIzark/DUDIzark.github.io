import random
import tkinter as tk
import random

def gerar_pergunta():
    operadores = ['+', '-', '*']
    operador = random.choice(operadores)
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    pergunta = f"Quanto é {num1} {operador} {num2}? "
    if operador == '+':
        resposta = num1 + num2
    elif operador == '-':
        resposta = num1 - num2
    else:
        resposta = num1 * num2
    return pergunta, resposta

def verificar_resposta():
    resposta = int(entry_resposta.get())
    if resposta == pergunta_atual[1]:
        lbl_feedback.config(text="Resposta correta!", fg="green")
        atualizar_pergunta()
    else:
        lbl_feedback.config(text="Resposta incorreta.", fg="red")
    
def atualizar_pergunta():
    global pergunta_atual
    pergunta_atual = gerar_pergunta()
    lbl_pergunta.config(text=pergunta_atual[0])
    entry_resposta.delete(0, tk.END)
    lbl_feedback.config(text="")

# Criar a janela principal
janela = tk.Tk()
janela.title("Jogo de Matemática")
janela.geometry("300x200")

# Criar os widgets
lbl_pergunta = tk.Label(janela, text="", font=("Arial", 12))
entry_resposta = tk.Entry(janela, width=10)
btn_verificar = tk.Button(janela, text="Verificar", command=verificar_resposta)
lbl_feedback = tk.Label(janela, text="", font=("Arial", 12))

# Posicionar os widgets na janela
lbl_pergunta.pack(pady=10)
entry_resposta.pack()
btn_verificar.pack(pady=10)
lbl_feedback.pack()

# Iniciar o jogo
atualizar_pergunta()

# Iniciar o loop principal da janela
janela.mainloop()

def gerar_pergunta():
    operadores = ['+', '-', '*']
    operador = random.choice(operadores)
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    pergunta = f"Quanto é {num1} {operador} {num2}? "
    if operador == '+':
        resposta = num1 + num2
    elif operador == '-':
        resposta = num1 - num2
    else:
        resposta = num1 * num2
    return pergunta, resposta

def verificar_resposta(pergunta, resposta):
    try:
        valor = int(input(pergunta))
        if valor == resposta:
            print("Resposta correta!")
            return True
        else:
            print("Resposta incorreta.")
            return False
    except ValueError:
        print("Resposta inválida. Digite um número inteiro.")
        return False

def jogar():
    print("Bem-vindo ao jogo de matemática!")
    pontos = 0
    tentativas = 0
    while tentativas < 5:
        pergunta, resposta = gerar_pergunta()
        if verificar_resposta(pergunta, resposta):
            pontos += 1
        tentativas += 1
    print(f"Fim do jogo! Pontuação final: {pontos}/5")


jogar()

