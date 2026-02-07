import tkinter as tk
from tkinter import messagebox

from app.models import Cliente, OrdemServico
from app import services
from app.database import carregar_dados

# ---------- Funções ----------
def criar_ordem():
    nome = entry_nome.get()
    telefone = entry_telefone.get()
    descricao = entry_descricao.get()

    try:
        cliente = Cliente(nome, telefone)
        ordem = OrdemServico(cliente, descricao)
        services.criar_ordem(ordem)
        messagebox.showinfo("Sucesso", "Ordem criada com sucesso!")
        limpar_campos()
        atualizar_lista()
    except ValueError as e:
        messagebox.showerror("Erro", str(e))


def finalizar_ordem():
    selecionado = listbox_ordens.curselection()
    if not selecionado:
        messagebox.showwarning("Aviso", "Selecione uma ordem.")
        return

    indice = selecionado[0]
    sucesso, mensagem = services.finalizar_ordem(indice)
    if sucesso:
        messagebox.showinfo("Sucesso", mensagem)
        atualizar_lista()
    else:
        messagebox.showerror("Erro", mensagem)


def atualizar_lista():
    listbox_ordens.delete(0, tk.END)
    for i, ordem in enumerate(services.listar_ordens()):
        texto = f"{i} - {ordem.cliente.nome} | {ordem.status}"
        listbox_ordens.insert(tk.END, texto)


def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_telefone.delete(0, tk.END)
    entry_descricao.delete(0, tk.END)

# ---------- Interface ----------
carregar_dados()

janela = tk.Tk()
janela.title("Sistema de Ordens de Serviço")
janela.geometry("500x500")

# Cadastro
tk.Label(janela, text="Nome do Cliente").pack()
entry_nome = tk.Entry(janela)
entry_nome.pack(fill="x", padx=10)

tk.Label(janela, text="Telefone").pack()
entry_telefone = tk.Entry(janela)
entry_telefone.pack(fill="x", padx=10)

tk.Label(janela, text="Descrição do Serviço").pack()
entry_descricao = tk.Entry(janela)
entry_descricao.pack(fill="x", padx=10)

tk.Button(janela, text="Criar Ordem", command=criar_ordem).pack(pady=10)

# Lista
tk.Label(janela, text="Ordens de Serviço").pack()
listbox_ordens = tk.Listbox(janela)
listbox_ordens.pack(fill="both", expand=True, padx=10, pady=5)

tk.Button(janela, text="Finalizar Ordem", command=finalizar_ordem).pack(pady=10)

atualizar_lista()

janela.mainloop()
