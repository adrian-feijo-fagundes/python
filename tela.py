import tkinter as tk

janela = tk.Tk()

janela.title("Meu programa")
janela.geometry("400x300")

texto = tk.Label(janela, text="Olá, Python!")
texto.pack()

botao = tk.Button(janela, text="Clique aqui")
botao.pack()

janela.mainloop()