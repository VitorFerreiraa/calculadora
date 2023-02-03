#importando biblioteca Tkinter
from tkinter import * 
from tkinter import ttk


#Cores
cor1 = "#2c2c2c" #Cinza
cor2 = "#feffff" #Branca
cor3 = "#38576b" #Azul Carregado
cor4 = "#ECEFF1"  #Cinzento
cor5=  "#FFAB40"  #Laranja


#Criando Janela
janela = Tk()
janela.title("Calculadora")
janela.geometry("242x310")
janela.config(bg=cor1)

#Criando Frames (Dividindo a janela para o display)
frame_tela = Frame(janela, width=244, height=55, bg=cor3)
frame_tela.grid(row=0, column=0)

#Variavel para armazenar todos os valores
armazenarValores=""
#Variavel
valorTexto= StringVar()

#Criando função realização dos calculos
def recebeValores(valor):

    
    global armazenarValores
    armazenarValores = armazenarValores + str(valor)
    
    #Adicionando valor na tela(Display)
    valorTexto.set(armazenarValores)

#Função para calcular os valores
def calcular():

    global armazenarValores

    resultado = eval(armazenarValores)
    
    valorTexto.set(str(resultado))

#Limpando display
def limparDisplay():

    global armazenarValores

    armazenarValores = ""
    valorTexto.set("")

#Janela para os botões
frame_corpo = Frame(janela, width=244, height=265)
frame_corpo.grid(row=1, column=0)

#Criando Label


app_label = Label(frame_tela, textvariable=valorTexto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font = ("Ivy 18"), bg=cor3, fg= cor2)
app_label.place(x=0,y=0)


#Criando os botões
b1 = Button(frame_corpo, command= limparDisplay, text="C", width=11, height=2, bg= cor4, font= ("Ivy 12 bold"), relief=RAISED, overrelief=RIDGE )
b1.place(x=1, y=0)

b2 = Button(frame_corpo, command=lambda:recebeValores("%"), text="%", width=5, height=2, bg= cor4, font= ("Ivy 12 bold"), relief=RAISED, overrelief=RIDGE)
b2.place(x=122, y=0)

b3 = Button(frame_corpo, command=lambda:recebeValores("/"), text="/", width=5, height=2, bg= cor5, fg= cor2, font= ("Ivy 12 bold"), relief=RAISED, overrelief=RIDGE)
b3.place(x=182, y=0)

b4 = Button(frame_corpo, command=lambda:recebeValores("7"), text="7", width=5, height=2, bg= cor4, font= ("Ivy 12 bold"), relief=RAISED, overrelief=RIDGE)
b4.place(x=1, y=52)

b5 = Button(frame_corpo, command=lambda:recebeValores("8"), text="8", width=5, height=2, bg= cor4, font= ("Ivy 12 bold"), relief=RAISED, overrelief=RIDGE)
b5.place(x=61, y=52)

b6 = Button(frame_corpo, command=lambda:recebeValores("9"), text="9",  width=5, height=2, bg= cor4, font= ("Ivy 12 bold"), relief=RAISED, overrelief=RIDGE)
b6.place(x=122, y=52)

b7 = Button(frame_corpo, command=lambda:recebeValores("*"), text="*", width=5, height=2, bg= cor5, fg= cor2, font= ("Ivy 12 bold"), relief=RAISED, overrelief=RIDGE)
b7.place(x=182, y=52)

b8 = Button(frame_corpo, command=lambda:recebeValores("4"), text="4", width=5, height=2, bg= cor4, font= ("Ivy 12 bold"), relief=RAISED, overrelief=RIDGE)
b8.place(x=1, y=104)

b9 = Button(frame_corpo, command=lambda:recebeValores("5"), text="5", width=5, height=2, bg= cor4, font= ("Ivy 12 bold"), relief=RAISED, overrelief=RIDGE)
b9.place(x=61, y=104)

b10 = Button(frame_corpo, command=lambda:recebeValores("6"), text="6", width=5, height=2, bg= cor4, font= ("Ivy 12 bold"), relief=RAISED, overrelief=RIDGE)
b10.place(x=122, y=104)

b11 = Button(frame_corpo, command=lambda:recebeValores("-"), text="-", width=5, height=2, bg= cor5, fg= cor2, font= ("Ivy 12 bold"), relief=RAISED, overrelief=RIDGE)
b11.place(x=182, y=104)

b12 = Button(frame_corpo, command=lambda:recebeValores("1"), text="1", width=5, height=2, bg= cor4, font= ("Ivy 12 bold"), relief=RAISED, overrelief=RIDGE)
b12.place(x=1, y=156)

b13 = Button(frame_corpo, command=lambda:recebeValores("2"), text="2", width=5, height=2, bg= cor4, font= ("Ivy 12 bold"), relief=RAISED, overrelief=RIDGE)
b13.place(x=61, y=156)

b14 = Button(frame_corpo, command=lambda:recebeValores("3"), text="3", width=5, height=2, bg= cor4, font= ("Ivy 12 bold"), relief=RAISED, overrelief=RIDGE)
b14.place(x=122, y=156)

b15 = Button(frame_corpo, command=lambda:recebeValores("+"), text="+", width=5, height=2, bg= cor5, fg= cor2, font= ("Ivy 12 bold"), relief=RAISED, overrelief=RIDGE)
b15.place(x=182, y=156)

b16 = Button(frame_corpo, command=lambda:recebeValores("0"), text="0", width=11, height=2, bg= cor4, font= ("Ivy 12 bold"), relief=RAISED, overrelief=RIDGE )
b16.place(x=1, y=208)

b17 = Button(frame_corpo, command=lambda:recebeValores("."), text=".", width=5, height=2, bg= cor4, font= ("Ivy 12 bold"), relief=RAISED, overrelief=RIDGE)
b17.place(x=122, y=208)

b18 = Button(frame_corpo, command=calcular, text="=", width=5, height=2, bg= cor5, fg= cor2, font= ("Ivy 12 bold"), relief=RAISED, overrelief=RIDGE)
b18.place(x=182, y=208)







janela.mainloop()
