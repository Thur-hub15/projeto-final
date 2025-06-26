import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Conexão com o banco de dados SQLite
def conectar():
    return sqlite3.connect('clientes.db')

# Criar tabela se não existir
def criar_tabela():
    conn = conectar()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            telefone TEXT,
            endereco TEXT
        )
    ''')
    conn.commit()
    conn.close()

# CREATE - Inserir novo cliente
def inserir_cliente():
    nome = entry_nome.get()
    email = entry_email.get()
    telefone = entry_telefone.get()
    endereco = entry_endereco.get()

    if nome and email:
        conn = conectar()
        c = conn.cursor()
        c.execute('INSERT INTO clientes (nome, email, telefone, endereco) VALUES (?, ?, ?, ?)', 
                  (nome, email, telefone, endereco))
        conn.commit()
        conn.close()
        messagebox.showinfo('Sucesso', 'Cliente cadastrado com sucesso!')
        mostrar_clientes()
    else:
        messagebox.showerror('Erro', 'Nome e e-mail são obrigatórios!')

# READ - Mostrar clientes
def mostrar_clientes():
    for row in tree.get_children():
        tree.delete(row)
    conn = conectar()
    c = conn.cursor()
    c.execute('SELECT * FROM clientes')
    dados = c.fetchall()
    for cliente in dados:
        tree.insert("", "end", values=cliente)
    conn.close()

# DELETE - Excluir cliente
def excluir_cliente():
    selecionado = tree.selection()
    if selecionado:
        cliente_id = tree.item(selecionado)['values'][0]
        conn = conectar()
        c = conn.cursor()
        c.execute('DELETE FROM clientes WHERE id = ?', (cliente_id,))
        conn.commit()
        conn.close()
        messagebox.showinfo('Exclusão', 'Cliente excluído com sucesso.')
        mostrar_clientes()
    else:
        messagebox.showerror('Erro', 'Selecione um cliente para excluir.')

# UPDATE - Editar cliente
def editar_cliente():
    selecionado = tree.selection()
    if selecionado:
        cliente_id = tree.item(selecionado)['values'][0]
        nome = entry_nome.get()
        email = entry_email.get()
        telefone = entry_telefone.get()
        endereco = entry_endereco.get()

        if nome and email:
            conn = conectar()
            c = conn.cursor()
            c.execute('''
                UPDATE clientes 
                SET nome = ?, email = ?, telefone = ?, endereco = ?
                WHERE id = ?
            ''', (nome, email, telefone, endereco, cliente_id))
            conn.commit()
            conn.close()
            messagebox.showinfo('Atualizado', 'Dados atualizados com sucesso.')
            mostrar_clientes()
        else:
            messagebox.showerror('Erro', 'Nome e e-mail são obrigatórios!')
    else:
        messagebox.showwarning('Aviso', 'Selecione um cliente para editar.')

# Função para preencher os campos ao selecionar
def preencher_campos(event):
    selecionado = tree.focus()
    if selecionado:
        valores = tree.item(selecionado, 'values')
        entry_nome.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_telefone.delete(0, tk.END)
        entry_endereco.delete(0, tk.END)
        entry_nome.insert(0, valores[1])
        entry_email.insert(0, valores[2])
        entry_telefone.insert(0, valores[3])
        entry_endereco.insert(0, valores[4])

# ------------------- Interface Gráfica ---------------------
janela = tk.Tk()
janela.title('Cadastro de Clientes')
janela.geometry('800x600')
janela.configure(bg="#49425c")

tk.Label(janela, text="Cadastro de Clientes", font=('Arial', 20, 'bold'), bg='#f0f0f0').grid(row=0, column=0, columnspan=2, pady=20)

tk.Label(janela, text='Nome:', font=('Arial', 14), bg='#f0f0f0').grid(row=1, column=0, sticky='e')
entry_nome = tk.Entry(janela, font=('Arial', 14), width=30)
entry_nome.grid(row=1, column=1, pady=5)

tk.Label(janela, text='E-mail:', font=('Arial', 14), bg='#f0f0f0').grid(row=2, column=0, sticky='e')
entry_email = tk.Entry(janela, font=('Arial', 14), width=30)
entry_email.grid(row=2, column=1, pady=5)

tk.Label(janela, text='Telefone:', font=('Arial', 14), bg='#f0f0f0').grid(row=3, column=0, sticky='e')
entry_telefone = tk.Entry(janela, font=('Arial', 14), width=30)
entry_telefone.grid(row=3, column=1, pady=5)

tk.Label(janela, text='Endereço:', font=('Arial', 14), bg='#f0f0f0').grid(row=4, column=0, sticky='e')
entry_endereco = tk.Entry(janela, font=('Arial', 14), width=30)
entry_endereco.grid(row=4, column=1, pady=5)

# Botões
tk.Button(janela, text="Salvar", font=('Arial', 12), bg="#51FF00", fg='black', command=inserir_cliente).grid(row=5, column=0, pady=10)
tk.Button(janela, text="Editar", font=('Arial', 12), bg="#2B4AF8", fg='black', command=editar_cliente).grid(row=5, column=1, pady=10)
tk.Button(janela, text="Deletar", font=('Arial', 12), bg='#f44336', fg='black', command=excluir_cliente).grid(row=5, column=2, columnspan=2, pady=10)

# Tabela de dados
columns = ('ID', 'Nome', 'E-mail', 'Telefone', 'Endereço')
tree = ttk.Treeview(janela, columns=columns, show='headings', height=10)
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, minwidth=0, width=120)
tree.grid(row=7, column=0, columnspan=2, padx=10, pady=10)
tree.bind("<<TreeviewSelect>>", preencher_campos)

# Executar tudo
criar_tabela()
mostrar_clientes()
janela.mainloop()
