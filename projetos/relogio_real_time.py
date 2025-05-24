import tkinter as tk
import datetime

def mostrar_hora():
    agora = datetime.datetime.now().strftime("%H:%M:%S")
    label.config(text=agora)
    janela.after(1000, mostrar_hora)  # chama de novo após 1000ms (1s)

janela = tk.Tk()
janela.title("Relógio Digital")
janela.geometry("250x100")

label = tk.Label(janela, font=("Arial", 24))
label.pack(pady=20)

mostrar_hora()  # inicia a função pela primeira vez

janela.mainloop()

