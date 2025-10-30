import sqlite3 as sq
import customtkinter as ctk
banco = sq.connect('primeiro_banco.db')
cursor = banco.cursor()
cursor.execute("SELECT * FROM pessoas")
dados=cursor.fetchall()


app1 = ctk.CTk()
app1.geometry('1600x900')

def atualizar():
    valor = int(escolha.get())
    nome.configure(text=f'Nome: {dados[valor][0]}')
    idade.configure(text=f'Idade: {dados[valor][1]}')
    email.configure(text=f'Email: {dados[valor][2]}')

ctkl1 = ctk.CTkLabel(app1, text="Banco de Dados com Interface Gráfica")
ctkl1.place(relx=0.5, y=200, anchor='center')

escolha = ctk.CTkEntry(app1 )
escolha.place(relx=0.5, y=270, anchor='center')



butao=ctk.CTkButton(app1, text="Mostrar Dados", command=atualizar)
butao.place(relx=0.5, y=300, anchor='center')


nome = ctk.CTkLabel(app1, text=f'Nome: {dados[0][0]}')
nome.place(relx=0.5, y=560, anchor='center')

idade = ctk.CTkLabel(app1, text=f'idade: {dados[0][1]}')
idade.place(relx=0.5, y=580, anchor='center')

email = ctk.CTkLabel(app1, text=f'email: {dados[0][2]}')
email.place(relx=0.5, y=600, anchor='center')


banco.commit()
app1.mainloop()





