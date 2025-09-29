#Author: Denisander Vivan. Data: 29/09/2025
#Correções do Chat GPT
#Um pequeno aplicativo para calcular as raízes de uma equação quadrática.
import tkinter as tk
from tkinter import ttk
from entry import CustomEntry
from calcular import calcular

#Aqui eu crio a janela principal
root = tk.Tk()

#Aqui eu determino o tamanho da janela
root.geometry('500x500+300+300')

#Aqui eu ajusto para não haver redimensionamento da janela
root.resizable(False, False)

#Aqui eu crio um LabelFrame para colocar o Label do resultado
painel = ttk.LabelFrame(root, text="Resultados")

#Aqui eu coloco o painel na janela
painel.grid(row=0, column=0, sticky='snew')

#Aqui eu crio a variável que vai armazenar o resultado
most_var = tk.StringVar()

#Aqui eu crio o Label que vai mostrar o resultado
mostrador = tk.Label(painel, textvariable=most_var, fg='lime', bg='black')

#Aqui eu coloco o mostrador no painel
mostrador.grid(row=0, column=0, sticky='nsew')

#Aqui eu instancio a classe que tem as entradas
entradas_frame = CustomEntry(root)

#Aqui eu crio uma variável que vai armazenar o retorno da classe CustomEntry
entradas = entradas_frame.custom_entry(root)

"""Aqui eu crio o botão que vai dar o comando para calcular as raízes. O Command
lambda chama a função calcular ao mesmo tempo de pega os valores de A, B e C vindos
da variável 'entradas'"""
botão = ttk.Button(root, text='Calcular', command=lambda: calcular(
    entradas[0].get(),
    entradas[1].get(),
    entradas[2].get(),
    most_var))

#Aqui eu coloco o botão na janela
botão.grid(row=4, column=0, sticky='nsew', padx=5, pady=5)

#Aqui roda o programa
root.mainloop()
