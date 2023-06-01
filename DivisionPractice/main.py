from random import randint as rd
import tkinter as tk
from tkinter import ttk

Limit = 100

Root = tk.Tk()
MainFrame = tk.Frame(Root)
Question = ttk.Label(MainFrame, text="144 / 12 = ?", font=('jetBrains Mono', 20))
ScoreBoard = ttk.Label(MainFrame, text="0", font=('jetBrains Mono', 20))
One = ttk.Button(MainFrame, text="1", command=lambda: Submit(2))
Two = ttk.Button(MainFrame, text="2", command=lambda: Submit(2))
Three = ttk.Button(MainFrame, text="3", command=lambda: Submit(3))
Four = ttk.Button(MainFrame, text="4", command=lambda: Submit(4))
Five = ttk.Button(MainFrame, text="5", command=lambda: Submit(5))
Six = ttk.Button(MainFrame, text="6", command=lambda: Submit(6))
Seven = ttk.Button(MainFrame, text="7", command=lambda: Submit(7))
Eight = ttk.Button(MainFrame, text="8", command=lambda: Submit(8))
Nine = ttk.Button(MainFrame, text="9", command=lambda: Submit(9))
Ten = ttk.Button(MainFrame, text="10", command=lambda: Submit(10))
Eleven = ttk.Button(MainFrame, text="11", command=lambda: Submit(11))
Twelve = ttk.Button(MainFrame, text="12", command=lambda: Submit(12))

def Submit(n):
    y = rd(2, 12)
    z = rd(2, 12)
    if n == int(Question.cget("text").split(" ")[0]) / int(Question.cget("text").split(" ")[2]):
        Score = ScoreBoard["text"]
        ScoreBoard.config(text=str(int(Score) + 1))
    if int(ScoreBoard["text"]) == Limit:
        Question.config(text="All done. Good job")
    Question.config(text=f"{y * z} / {y} = ?")



Root.geometry("300x300")
Root.title("Math Practice")

MainFrame.pack(fill='both', expand=True)

Question.grid(row=0, column=1)
Submit(0)

ScoreBoard.grid(row=5, column=1)

One.grid(row=4, column=0)
Two.grid(row=4, column=1)
Three.grid(row=4, column=2)
Four.grid(row=3, column=0)
Five.grid(row=3, column=1)
Six.grid(row=3, column=2)
Seven.grid(row=2, column=0)
Eight.grid(row=2, column=1)
Nine.grid(row=2, column=2)
Ten.grid(row=1, column=0)
Eleven.grid(row=1, column=1)
Twelve.grid(row=1, column=2)

Root.mainloop()
