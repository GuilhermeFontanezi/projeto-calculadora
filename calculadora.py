import tkinter as tk
from tkinter import *

cor_de_fundo = '#292929'
cor_da_margem = '#a2a2a2'
numero_1 = int(0)
numero_2 = 0
soma_produto = 0
mudou = ''
fator_mudou = ''
somaetc = ''
result = 0

janela = tk.Tk()
janela.geometry('340x400')
janela.maxsize(340, 400)
janela.minsize(340, 400)
janela.configure(bg=cor_de_fundo)


def apagar():
    caixa_texto.delete(0, END)


def click_button(numero):
    atual = caixa_texto.get()
    caixa_texto.delete(0, END)
    caixa_texto.insert(END, str(atual) + str(numero))


def ponto():
    caixa_texto.insert(END, '.')


def somar():
    global adicao, numero_1, somaetc
    numero_1 = int(caixa_texto.get())
    somaetc = 'soma'
    caixa_texto.delete(0, END)


def subtracao():
    global somaetc, numero_1
    numero_1 = float(caixa_texto.get())
    somaetc = 'subtracao'
    caixa_texto.delete(0, END)


def multiplicacao():
    global somaetc, numero_1
    numero_1 = float(caixa_texto.get())
    somaetc = 'multiplicacao'
    caixa_texto.delete(0, END)


def divisao():
    global somaetc, numero_1
    numero_1 = float(caixa_texto.get())
    somaetc = 'divisao'
    caixa_texto.delete(0, END)


def resultado():
    global numero_1, numero_2, somaetc, result
    numero_2 = float(caixa_texto.get())

    if somaetc == 'soma':
        result = numero_1 + numero_2
    elif somaetc == 'subtracao':
        result = numero_1 - numero_2
    elif somaetc == 'multiplicacao':
        result = numero_1 * numero_2
    elif somaetc == 'divisao':
        result = numero_1 / numero_2
    else:
        result = 'Error...'

    if isinstance(result, float) and result.is_integer():
        result = int(result)

    caixa_texto.delete(0, END)
    caixa_texto.insert(END, str(result))


margem_caixa = Canvas(janela, width=340, height=100, bg=cor_da_margem, relief='ridge', highlightthickness=0)
margem_caixa.pack()

caixa_texto = Entry(janela, bg=cor_da_margem, borderwidth=0, fg='white', font=('Arial', 30, 'bold'))
caixa_texto.place(x=0, y=0)

apagar_tudo = Button(janela, height=3, width=21, font=('Calisto MT', 8, 'bold'), text='C', command=apagar)
apagar_tudo.place(x=5, y=110)

igual_a = Button(janela, height=3, width=21, font=('Calisto MT', 8, 'bold'), text='=', command=resultado)
igual_a.place(x=175, y=110)

sete = Button(janela, height=3, width=10, font=('Calisto MT', 8, 'bold'), bg=cor_da_margem, fg='#ffffff', text='7',  command=lambda: click_button(7))
sete.place(x=5, y=170)

oito = Button(janela, height=3, width=10, font=('Calisto MT', 8, 'bold'), bg=cor_da_margem, fg='#ffffff', text='8',  command=lambda: click_button(8))
oito.place(x=90, y=170)

nove = Button(janela, height=3, width=10, font=('Calisto MT', 8, 'bold'), bg=cor_da_margem, fg='#ffffff', text='9',  command=lambda: click_button(9))
nove.place(x=175, y=170)

quatro = Button(janela, height=3, width=10, font=('Calisto MT', 8, 'bold'), bg=cor_da_margem, fg='#ffffff', text='4',  command=lambda: click_button(4))
quatro.place(x=5, y=225)

cinco = Button(janela, height=3, width=10, font=('Calisto MT', 8, 'bold'), bg=cor_da_margem, fg='#ffffff', text='5',  command=lambda: click_button(5))
cinco.place(x=90, y=225)

seis = Button(janela, height=3, width=10, font=('Calisto MT', 8, 'bold'), bg=cor_da_margem, fg='#ffffff', text='6',  command=lambda: click_button(6))
seis.place(x=175, y=225)

um_1 = Button(janela, height=3, width=10, font=('Calisto MT', 8, 'bold'), bg=cor_da_margem, fg='#ffffff', text='1',  command=lambda: click_button(1))
um_1.place(x=5, y=280)

dois = Button(janela, height=3, width=10, font=('Calisto MT', 8, 'bold'), bg=cor_da_margem, fg='#ffffff', text='2', command=lambda: click_button(2))
dois.place(x=90, y=280)

tres = Button(janela, height=3, width=10, font=('Calisto MT', 8, 'bold'), bg=cor_da_margem, fg='#ffffff', text='3',  command=lambda: click_button(3))
tres.place(x=175, y=280)

zero = Button(janela, height=3, width=22, font=('Calisto MT', 8, 'bold'), bg=cor_da_margem, fg='#ffffff', text='0',  command=lambda: click_button(0))
zero.place(x=5, y=335)

ponto = Button(janela, height=3, width=10, font=('Calisto MT', 8, 'bold'), bg=cor_da_margem, fg='#ffffff', text='.', command=ponto)
ponto.place(x=175, y=335)

adicao = Button(janela, height=3, width=8, font=('Calisto MT', 8, 'bold'), bg="#fcac3c", fg='#ffffff', text='+',  command=somar)
adicao.place(x=266, y=170)

subtracao = Button(janela, height=3, width=8, font=('Calisto MT', 8, 'bold'), bg="#fcac3c", fg='#ffffff', text='-', command=subtracao)
subtracao.place(x=266, y=225)

multiplicacao = Button(janela, height=3, width=8, font=('Calisto MT', 8, 'bold'), bg="#fcac3c", fg='#ffffff', text='X', command=multiplicacao)
multiplicacao.place(x=266, y=280)

divisao = Button(janela, height=3, width=8, font=('Calisto MT', 8, 'bold'), bg="#fcac3c", fg='#ffffff', text='➗', command=divisao)
divisao.place(x=266, y=335)

janela.mainloop()
