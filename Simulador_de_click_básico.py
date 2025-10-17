import customtkinter as ctk
msg = 0
boost = 1
boost_pago = False
aclk_pago = False
Valor = 10
Valor_auto = 50
def cl():  
    global msg
    msg += boost
    clicker.configure(text=str(msg))
    money.configure(text=str(msg))
ctk.set_appearance_mode('Dark')

app = ctk.CTk()
app.title('top')
app.geometry ('500x500')

app2 = ctk.CTkToplevel()
app2.title('top2')
app2.geometry ('500x500')

def pag1():
    app2.withdraw()
    app.deiconify()

def x2():
    global msg,boost,boost_pago,Valor
    if not boost_pago and msg >= Valor:
        boost += 2
        msg = msg - Valor
        Valor = Valor * 2
        Preço_2x.configure(text=f"Preço: {Valor}")
        mltr.configure(text=f'Multiplicador: {boost}')

        clicker.configure(text=str(msg))
        money.configure(text=str(msg))

def aclk():
    global msg,boost,boost_pago,aclk_pago
    if not aclk_pago and msg >= 50:
        aclk_pago = True
        clicker.configure(text=str(msg))
        money.configure(text=str(msg))
        auto.configure(text='COMPRADO')
        Auto_clicker()

def Auto_clicker():
         global msg,boost,boost_pago,aclk_pago         
         msg = msg + (boost * 0.5)
         clicker.configure(text=str(msg))
         money.configure(text=str(msg))
         money.after(1000,Auto_clicker)





clicker = ctk.CTkButton(app2,text= msg ,command=cl,height=200, width=400)
clicker.place(relx=0.5, rely=0.5, anchor="center") 
text= ctk.CTkButton(app2,text="Loja",command= pag1)
text.place(relx=0.5, rely=0.9, anchor="center")
app2.withdraw()
mltr = ctk.CTkLabel(app2,text=f"multiplicador: {boost}")
mltr.place(relx=0.2, rely=0.05, anchor="center")

def pagina2():
    app.withdraw()
    new_windows()



money = ctk.CTkLabel(app,text=f"dinheiro: {msg}")
money.place(x=10,y=-6.2) 

two = ctk.CTkButton(app,text="2x dinheiro",command= x2)
two.place(relx=0.5, rely=0.5, anchor="center") 

auto = ctk.CTkButton(app,text="Auto Clicker",command= aclk)
auto.place(relx=0.5, rely=0.4, anchor="center")

oi=ctk.CTkButton(app,text='Farm', command=pagina2)
oi.place(relx=0.5, rely=0.9, anchor="center")

Preço_2x = ctk.CTkLabel(app,text=f"Preço: {Valor}")
Preço_2x.place(relx=0.7, rely=0.5, anchor="center")

Preço_auto = ctk.CTkLabel(app,text=f"Preço: {Valor_auto}")
Preço_auto.place(relx=0.7, rely=0.4, anchor="center")

def new_windows():
    app2.deiconify()


app.mainloop()
