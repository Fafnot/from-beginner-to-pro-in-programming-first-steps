import tkinter as tk
from PIL import Image, ImageTk
import random

def определить_победителя(ваш_выбор):
    варианты = ["камень", "ножницы", "бумага"]
    компьютер = random.choice(варианты)

    img_user = Image.open(f"{ваш_выбор}.png")
    img_computer = Image.open(f"{компьютер}.png")

    img_user = ImageTk.PhotoImage(img_user)
    img_computer = ImageTk.PhotoImage(img_computer)

    картинка_пользователя.configure(image=img_user)
    картинка_компьютера.configure(image=img_computer)
    текст_vs.configure(text="vs")

    результат = tk.Label(root, text="Выбор компьютера: " + компьютер)
    результат.pack()

    if ваш_выбор == компьютер:
        результат["text"] += "\nНичья!"
    elif (
        (ваш_выбор == "камень" and компьютер == "ножницы") or
        (ваш_выбор == "ножницы" and компьютер == "бумага") or
        (ваш_выбор == "бумага" and компьютер == "камень")
    ):
        результат["text"] += "\nВы выиграли!"
    else:
        результат["text"] += "\nВы проиграли!"

    картинка_пользователя.image = img_user
    картинка_компьютера.image = img_computer

root = tk.Tk()
root.title("Камень, Ножницы, Бумага")

фрейм_изображений = tk.Frame(root)
фрейм_изображений.pack()

картинка_пользователя = tk.Label(фрейм_изображений)
картинка_пользователя.grid(row=0, column=0)

текст_vs = tk.Label(фрейм_изображений, text="")
текст_vs.grid(row=0, column=1, padx=20)

картинка_компьютера = tk.Label(фрейм_изображений)
картинка_компьютера.grid(row=0, column=2)

камень_btn = tk.Button(root, text="Камень", command=lambda: определить_победителя("камень"))
камень_btn.pack()

ножницы_btn = tk.Button(root, text="Ножницы", command=lambda: определить_победителя("ножницы"))
ножницы_btn.pack()

бумага_btn = tk.Button(root, text="Бумага", command=lambda: определить_победителя("бумага"))
бумага_btn.pack()

root.mainloop()
