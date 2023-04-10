import tkinter as tk

root = tk.Tk()
root.title("RadioButton List")

# Define variables para las opciones
var = tk.StringVar()
var.set("")

# Crea los RadioButtons
option1 = tk.Radiobutton(root, text="Opción 1", variable=var, value="Opción 1")
option1.pack()

option2 = tk.Radiobutton(root, text="Opción 2", variable=var, value="Opción 2")
option2.pack()

option3 = tk.Radiobutton(root, text="Opción 3", variable=var, value="Opción 3")
option3.pack()

# Crea el botón de reinicio
reset_btn = tk.Button(root, text="Reiniciar", command=lambda: var.set(""))
reset_btn.pack()

root.mainloop()
