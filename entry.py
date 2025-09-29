#Classe para gerar as caixas de entrada

import tkinter as tk
from tkinter import ttk

#Essa classe foi feita parte por mim, parte pelo chat GPT
class CustomEntry(ttk.Frame):
    """Classe para herdar de Frame para gerar múltiplos Entry."""

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.grid(row=1, column=0, sticky='nsew')
    
    #Aqui eu crio o método principal que vai criar os trê entrys na tela
    def custom_entry(self, root):

        #Aqui eu crio o rótulo para o primeiro entry
        ttk.Label(self, text='A').grid(row=0, column=0)

        #Aqui eu crio a variável de controle    
        ent_1_var = tk.StringVar()

        #Aqui eu crio o primeiro entry
        ent_1 = ttk.Entry(self, textvariable=ent_1_var)

        #Aqui eu fixo o entry no Frame
        ent_1.grid(row=1, column=0, sticky='nsew', padx=5, pady=5)

        #Aqui eu crio o rótulo do segundo entry
        ttk.Label(self, text='B').grid(row=0, column=1)

        #Aqui eu crio a variável de controle
        ent_2_var = tk.StringVar()

        #Aqui eu crio o segundo entry
        ent_2 = ttk.Entry(self, textvariable=(ent_2_var))

        #Aqui eu fixo o entry no frame
        ent_2.grid(row=1, column=1, sticky='nsew', padx=5, pady=5)

        #Aqui eu crio o rótulo para o terceiro entry
        ttk.Label(self, text='C').grid(row=0, column=2)

        #Aqui eu crio a variável de controle
        ent_3_var = tk.StringVar()

        #Aqui eu crio o terceiro entry
        ent_3 = ttk.Entry(self, textvariable=ent_3_var)

        #Aqui eu fixo o entry no frame
        ent_3.grid(row=1, column=2, sticky='nsew', padx=5, pady=5)

        #Aqui eu faço o retorno do método
        return (ent_1_var, ent_2_var, ent_3_var)