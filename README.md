# 🧾 Sistema de Cadastro de Clientes

Um sistema simples e funcional de **cadastro de clientes** desenvolvido em **Python**, utilizando **Tkinter** para a interface gráfica e **SQLite** como banco de dados local.

---

## 📌 Funcionalidades

- ✅ Cadastro de novos clientes
- ✅ Edição de dados existentes
- ✅ Exclusão de registros
- ✅ Visualização em tabela (Treeview)
- ✅ Interface gráfica intuitiva

---

## 💻 Tecnologias Utilizadas

| Tecnologia | Função |
|------------|--------|
| Python     | Linguagem principal |
| Tkinter    | Criação da interface gráfica |
| SQLite3    | Banco de dados local |
| ttk        | Tabela interativa (Treeview) |
| messagebox | Caixas de mensagem/erro |

---

## 🧠 Estrutura da Tabela (SQLite)

```sql
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL,
    telefone TEXT,
    endereco TEXT
);
