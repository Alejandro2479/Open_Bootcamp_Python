import tkinter as tk

# crear ventana
root = tk.Tk()

# crear label
label = tk.Label(root, text="Selecciona un elemento de la lista")
label.pack()

# crear lista de elementos
elementos = ["Elemento 1", "Elemento 2", "Elemento 3", "Elemento 4", "Elemento 5"]
var = tk.StringVar(value=elementos[0])

# crear RadioButton para cada elemento de la lista
for elemento in elementos:
    radio_button = tk.Radiobutton(root, text=elemento, variable=var, value=elemento)
    radio_button.pack(anchor="w")

# mostrar ventana
root.mainloop()
