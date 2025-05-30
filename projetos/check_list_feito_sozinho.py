import tkinter as tk
from tkinter import simpledialog, messagebox

#funcoes dos botões

def adicionar_item():
    item = entrada.get()
    if item:
        lista.insert(tk.END, f"🟡 {item} (Em andamento)")
        entrada.delete(0,tk.END)

def remover_item():
    try:
        selecionado = lista.curselection()[0]
        lista.delete(selecionado)
    except IndexError:
        messagebox.showwarning("Atenção", "Selecione uma tarefa para remover.")

def alterar_status():
    try:
        selecionado = lista.curselection()[0]
        texto_original = lista.get(selecionado)
# Remove status anterior
        if " " in texto_original:
            tarefa_pura = texto_orignal.split(" ", 1)[1]
            tarefa_pura = tarefa_pura.split("(", 1)[0].strip()
        else:
            tarefa_pura = texto_original          
# Janela popup para escolher novo status
status = simpledialog.askstring(
    "Alterar Status",
    "Digite o novo status:\n1 - Em andamento\n2 - 90% concluído\n3 - Apresentável\n4 - Concluído"
)
# Dicionário com opções de status

opcoes = {
    "1": ("🟡", "Em andamento"),
    "2": ("🟠", "90% concluído"),
    "3": ("🔵", "Apresentável"),
    "4": ("✅", "Concluído")
}
if status in opcoes:
    emoji, nome = opcoes[status]
    nova_tarefa = f"{emoji} {tarefa_pura} ({nome})"
    lista.delete(selecionado)
    lista.insert(selecionado, nova_tarefa)
else:
    messagebox.showinfo("Cancelado", "Status não alterado.")
except IndexError:
messagebox.showwarning("Atenção", "Selecione uma tarefa para alterar o status.")

# Interface principal
janela = tk.Tk()
janela.title("Lista de Tarefas com Status")
janela.geometry("400x400")

# Entrada
entrada = tk.Entry(janela, width=30)
entrada.pack(pady=10)

# Botões
tk.Button(janela, text="Adicionar", command=adicionar_item).pack(pady=5)
tk.Button(janela, text="Remover", command=remover_item).pack(pady=5)
tk.Button(janela, text="Alterar Status", command=alterar_status).pack(pady=5)

# Lista de tarefas
lista = tk.Listbox(janela, width=50, height=15)
lista.pack(pady=10)

# Executa o app
janela.mainloop()

"""
O QUE EU ERREI NA HORA DE CRIAR ESSE CODIGO 
 

✅ Erros que precisam de correção:

Nome da variável errado :

tarefa_pura = texto_orignal.split(" ", 1)[1]
→ Aqui você escreveu texto_orignal, mas o nome correto é texto_original.

Bloco de código desalinhado (indentação incorreta):
Toda essa parte abaixo está desalinhada — ela deveria estar dentro da função alterar_status():

status = simpledialog.askstring(
    ...
)

opcoes = {
    ...
}

if status in opcoes:
    ...
else:
    ...

Outro erro de indentação no except:
Este trecho:

except IndexError:
messagebox.showwarning("Atenção", "Selecione uma tarefa para alterar o status.")

→ A linha do messagebox.showwarning deve estar indentada corretamente.
"""