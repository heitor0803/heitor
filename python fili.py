import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime


class SistemaAluguelVeiculos:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Aluguel de Veículos")

        # Configuração do banco de dados
        self.conn = sqlite3.connect('veiculos.db')
        self.cursor = self.conn.cursor()

        # Criar tabelas se não existirem
        self.criar_tabelas()

        # Interface gráfica
        self.criar_interface()

        # Atualizar listas inicialmente
        self.atualizar_listas()

    def criar_tabelas(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS veiculos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            modelo TEXT NOT NULL,
            placa TEXT NOT NULL UNIQUE,
            ano INTEGER NOT NULL,
            valor_diario REAL NOT NULL
        )
        ''')

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS alugueis (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            veiculo_id INTEGER NOT NULL,
            data_aluguel TEXT NOT NULL,
            data_devolucao TEXT,
            FOREIGN KEY (veiculo_id) REFERENCES veiculos (id)
        )
        ''')
        self.conn.commit()

    def criar_interface(self):
        # Notebook (abas)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True)

        # Aba de Cadastro
        self.frame_cadastro = ttk.Frame(self.notebook)
        self.notebook.add(self.frame_cadastro, text="Cadastro")
        self.criar_aba_cadastro()

        # Aba de Veículos Disponíveis
        self.frame_disponiveis = ttk.Frame(self.notebook)
        self.notebook.add(self.frame_disponiveis, text="Disponíveis")
        self.criar_aba_disponiveis()

        # Aba de Veículos Alugados
        self.frame_alugados = ttk.Frame(self.notebook)
        self.notebook.add(self.frame_alugados, text="Alugados")
        self.criar_aba_alugados()

    def criar_aba_cadastro(self):
        # Campos de entrada
        tk.Label(self.frame_cadastro, text="Modelo:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.entry_modelo = tk.Entry(self.frame_cadastro)
        self.entry_modelo.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.frame_cadastro, text="Placa:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.entry_placa = tk.Entry(self.frame_cadastro)
        self.entry_placa.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.frame_cadastro, text="Ano:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.entry_ano = tk.Entry(self.frame_cadastro)
        self.entry_ano.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self.frame_cadastro, text="Valor Diário (R$):").grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.entry_valor = tk.Entry(self.frame_cadastro)
        self.entry_valor.grid(row=3, column=1, padx=10, pady=5)

        # Botão de cadastro
        btn_cadastrar = tk.Button(self.frame_cadastro, text="Cadastrar Veículo", command=self.cadastrar_veiculo)
        btn_cadastrar.grid(row=4, column=0, columnspan=2, pady=10)

    def criar_aba_disponiveis(self):
        # Treeview para veículos disponíveis
        self.tree_disponiveis = ttk.Treeview(self.frame_disponiveis, columns=("ID", "Modelo", "Placa", "Ano", "Valor"),
                                             show="headings")
        self.tree_disponiveis.heading("ID", text="ID")
        self.tree_disponiveis.heading("Modelo", text="Modelo")
        self.tree_disponiveis.heading("Placa", text="Placa")
        self.tree_disponiveis.heading("Ano", text="Ano")
        self.tree_disponiveis.heading("Valor", text="Valor Diário (R$)")
        self.tree_disponiveis.pack(fill="both", expand=True)

        # Botão para alugar veículo
        btn_alugar = tk.Button(self.frame_disponiveis, text="Alugar Veículo", command=self.alugar_veiculo)
        btn_alugar.pack(pady=10)

    def criar_aba_alugados(self):
        # Treeview para veículos alugados
        self.tree_alugados = ttk.Treeview(self.frame_alugados, columns=("ID", "Modelo", "Placa", "Data Aluguel"),
                                          show="headings")
        self.tree_alugados.heading("ID", text="ID")
        self.tree_alugados.heading("Modelo", text="Modelo")
        self.tree_alugados.heading("Placa", text="Placa")
        self.tree_alugados.heading("Data Aluguel", text="Data do Aluguel")
        self.tree_alugados.pack(fill="both", expand=True)

        # Botão para devolver veículo
        btn_devolver = tk.Button(self.frame_alugados, text="Devolver Veículo", command=self.devolver_veiculo)
        btn_devolver.pack(pady=10)

    def cadastrar_veiculo(self):
        modelo = self.entry_modelo.get()
        placa = self.entry_placa.get()
        ano = self.entry_ano.get()
        valor_diario = self.entry_valor.get()

        if not all([modelo, placa, ano, valor_diario]):
            messagebox.showerror("Erro", "Preencha todos os campos!")
            return

        try:
            self.cursor.execute(
                "INSERT INTO veiculos (modelo, placa, ano, valor_diario) VALUES (?, ?, ?, ?)",
                (modelo, placa, int(ano), float(valor_diario))
            )
            self.conn.commit()
            messagebox.showinfo("Sucesso", "Veículo cadastrado!")
            self.limpar_campos()
            self.atualizar_listas()
        except sqlite3.IntegrityError:
            messagebox.showerror("Erro", "Placa já cadastrada!")
        except ValueError:
            messagebox.showerror("Erro", "Ano ou valor inválido!")

    def alugar_veiculo(self):
        selected = self.tree_disponiveis.focus()
        if not selected:
            messagebox.showerror("Erro", "Selecione um veículo!")
            return

        veiculo_id = self.tree_disponiveis.item(selected)['values'][0]
        data_aluguel = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        try:
            self.cursor.execute(
                "INSERT INTO alugueis (veiculo_id, data_aluguel) VALUES (?, ?)",
                (veiculo_id, data_aluguel)
            )
            self.conn.commit()
            messagebox.showinfo("Sucesso", "Veículo alugado!")
            self.atualizar_listas()
        except sqlite3.Error as e:
            messagebox.showerror("Erro", f"Falha ao alugar veículo: {str(e)}")

    def devolver_veiculo(self):
        selected = self.tree_alugados.focus()
        if not selected:
            messagebox.showerror("Erro", "Selecione um veículo!")
            return

        aluguel_id = self.tree_alugados.item(selected)['values'][0]
        data_devolucao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        try:
            self.cursor.execute(
                "UPDATE alugueis SET data_devolucao = ? WHERE id = ?",
                (data_devolucao, aluguel_id)
            )
            self.conn.commit()
            messagebox.showinfo("Sucesso", "Veículo devolvido!")
            self.atualizar_listas()
        except sqlite3.Error as e:
            messagebox.showerror("Erro", f"Falha ao devolver veículo: {str(e)}")

    def atualizar_listas(self):
        # Limpar listas
        for row in self.tree_disponiveis.get_children():
            self.tree_disponiveis.delete(row)

        for row in self.tree_alugados.get_children():
            self.tree_alugados.delete(row)

        # Atualizar lista de veículos disponíveis
        self.cursor.execute('''
        SELECT v.id, v.modelo, v.placa, v.ano, v.valor_diario
        FROM veiculos v
        LEFT JOIN alugueis a ON v.id = a.veiculo_id AND a.data_devolucao IS NULL
        WHERE a.id IS NULL
        ''')
        for row in self.cursor.fetchall():
            self.tree_disponiveis.insert("", tk.END, values=row)

        # Atualizar lista de veículos alugados
        self.cursor.execute('''
        SELECT a.id, v.modelo, v.placa, a.data_aluguel
        FROM alugueis a
        JOIN veiculos v ON a.veiculo_id = v.id
        WHERE a.data_devolucao IS NULL
        ''')
        for row in self.cursor.fetchall():
            self.tree_alugados.insert("", tk.END, values=row)

    def limpar_campos(self):
        self.entry_modelo.delete(0, tk.END)
        self.entry_placa.delete(0, tk.END)
        self.entry_ano.delete(0, tk.END)
        self.entry_valor.delete(0, tk.END)

    def __del__(self):
        # Fechar conexão com o banco de dados quando o programa terminar
        self.conn.close()


if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaAluguelVeiculos(root)
    root.mainloop()
