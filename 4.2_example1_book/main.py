from tkinter import *
# Novos temas de widget adicionados ao Tk no 8.5
# quando uso Entry() .. - importo tkinter basic
# quando uso ttk.Entry() invoco a função dentro do TTK
from tkinter import ttk


def calculate(*args):
    try:
        value = float(feet.get())
        meters.set((0.3048*value*10000.0+0.5)/10000.0)
    except ValueError:
        pass


root = Tk()
root.title("Pés para metros")

# Para cada um dos três Widgets, nos precisamos fazer duas coisas
# criar um o próprio widget e então colocá-o na tela
# Os três widgets, são filhos da nossa janela de conteudo
# GRID
# 1. colocamos a posição adequada coluna e linha
# 2. a opção sticky mostr como o widget ira se alinhar com a célula de
# grid. Então o W (west) significa que o widget fica do lado esquerdo
# da celula.
# WE significa que ancora do mesmo lado

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

feet = StringVar()
meters = StringVar()

feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label (mainframe, textvariable=meters).grid(column=2,
                                                row=2,
                                                sticky=(W, E))

ttk.Button(mainframe, text="Calculate", command=calculate).grid(
    column=3, row=3, sticky=W)

ttk.Label(mainframe, text="feet").grid(column=3, row=1,sticky=W)
ttk.Label(mainframe, text="é equivalente a").grid(column=1,
                                                  row=2,
                                                  sticky=E)
ttk.Label(mainframe,text="meters").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind('<Return>', calculate)

root.mainloop()

