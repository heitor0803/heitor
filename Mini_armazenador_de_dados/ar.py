import sqlite3 as sq
import customtkinter as ctk


banco = sq.connect('primeiro_banco.db')
cursor = banco.cursor()
cursor.execute("SELECT * FROM pessoas")
dados=cursor.fetchall()


app1 = ctk.CTk()
app1.geometry('600x500')
app2 = ctk.CTkToplevel()
app2.geometry('600x500')
app2.withdraw()


def delet():
    global valor,dados
    cursor.execute("DELETE FROM pessoas WHERE nome = ? AND idade = ? AND email = ?",(dados[valor][0],dados[valor][1],dados[valor][2]))
    banco.commit()
    cursor.execute("SELECT * FROM pessoas")
    dados=cursor.fetchall()
    nome.configure(text='DELETADO')
    idade.configure(text='DELETADO')
    email.configure(text='DELETADO')
def pag2(): 
    app2.deiconify()
    app1.withdraw()


def pag1():
    app1.deiconify()
    app2.withdraw()

def adicionar_dados():
    global dados,quantidade
    nome = psa.get()
    idade = ida.get()
    email = eml.get()
    cursor.execute("INSERT INTO pessoas VALUES(?,?,?)",(nome,idade,email))
    banco.commit()
    psa.delete(0, 'end')
    ida.delete(0, 'end')
    eml.delete(0, 'end')
    cursor.execute("SELECT * FROM pessoas")
    dados=cursor.fetchall()
    cursor.execute("SELECT COUNT(*) FROM pessoas")
    quantidade = cursor.fetchone()[0]
    
ctk2 = ctk.CTkButton(app2, text="Voltar para pagina principal", command=pag1)
ctk2.place(relx=0.5, y=485, anchor='center')

tpsa = ctk.CTkLabel(app2, text="Nome:")
tpsa.place(relx=0.5, y=160, anchor='center')
psa = ctk.CTkEntry(app2)
psa.place(relx=0.5, y=180, anchor='center')

tida = ctk.CTkLabel(app2, text="Idade:")
tida.place(relx=0.5, y=210, anchor='center')
ida = ctk.CTkEntry(app2)
ida.place(relx=0.5, y=230, anchor='center')

teml = ctk.CTkLabel(app2, text="Email:")
teml.place(relx=0.5, y=260, anchor='center')
eml = ctk.CTkEntry(app2)
eml.place(relx=0.5, y=280, anchor='center')

butao2 = ctk.CTkButton(app2, text="Adicionar Dados", command=adicionar_dados)
butao2.place(relx=0.5, y=320, anchor='center')



def atualizar():
    global valor,dados
    valor = int(escolha.get())
    nome.configure(text=f'Nome: {dados[valor][0]}')
    idade.configure(text=f'Idade: {dados[valor][1]}')
    email.configure(text=f'Email: {dados[valor][2]}')

cursor.execute("SELECT COUNT(*) FROM pessoas")
quantidade = cursor.fetchone()[0]

ctkl1 = ctk.CTkLabel(app1, text="Banco de Dados com Interface Gráfica")
ctkl1.place(relx=0.5, y=200, anchor='center')

quantidade = ctk.CTkLabel(app1, text = f'Quantidade de pessoas adicionadas: {quantidade}')
quantidade.place(relx=0.7, y=40, anchor='center')

escolha = ctk.CTkEntry(app1 )
escolha.place(relx=0.5, y=270, anchor='center')



butao=ctk.CTkButton(app1, text="Mostrar Dados", command=atualizar)
butao.place(relx=0.5, y=300, anchor='center')

delete = ctk.CTkButton(app1, text="Deletar esse dado", command = delet)
delete.place(relx=0.5, y=340, anchor='center')
nome = ctk.CTkLabel(app1, text=f'Nome: {dados[0][0]}')
nome.place(relx=0.5, y=400, anchor='center')

idade = ctk.CTkLabel(app1, text=f'idade: {dados[0][1]}')
idade.place(relx=0.5, y=430, anchor='center')

email = ctk.CTkLabel(app1, text=f'email: {dados[0][2]}')
email.place(relx=0.5, y=460, anchor='center')

trocar = ctk.CTkButton(app1, text="Trocar de Janela", command=pag2)
trocar.place(relx=0.5, y=485, anchor='center')

banco.commit()
app1.mainloop()




