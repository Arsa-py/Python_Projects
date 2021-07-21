import tkinter as tk

class TICKTACKTOE(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic Tac Toe")
        self.btns = []      # kreiranje dugmica (buttons), niz (list)
        self.turn = True    # Red na igraca, koji igrac je na potezu
        self.count = 0      # brojac poteza
        self.resizable(width=False, height=False)   # tkinter prozor NE MOZE da mijenja svoju velicinu po potrebi korisnika,
                                                    # velicina prozora ce da zavisi od dugmica (buttons)
        self.Board()        # ova funkcija ce kreirati tablu za igranje

    def Board(self):
        for i in range(0, 3):
            row = []
            for j in range(0, 3):
                row.append(tk.Button(self, width=10, height=3, font="Calibre 35 bold",
                                     command=lambda x=i, y=j: self.Turn_Taken(x,y)))
                row[j].grid(row=i, column=j)
            self.btns.append(row)
            # dugme za novu igru
        tk.Button(self, text="New Game", width=10, height=1, font="Calibre 15 bold",
                  bg="black", fg="white", activebackground="blue3", activeforeground="white",
                  command=self.NEWGAME).grid(row=3, column=1)
            # dugme za izlazak iz igre
        tk.Button(self, text="QUIT", width=10, height=1, font="Calibre 15 bold",
                  bg="black", fg="white", activebackground="blue3", activeforeground="white",
                  command=self.destroy).grid(row=4, column=1)

    def Turn_Taken(self, x, y):
        self.count += 1
        if self.turn:
            char = "X"
            self.btns[x][y].config(text="X", bg="black", state="disabled")
        else:
            char = "O"
            self.btns[x][y].config(text="O", bg="white", state="disabled")
        self.Check_Results(char)
        self.turn = not self.turn

    def NEWGAME(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.btns = []
        self.turn = True
        self.count = 0
        self.Board()

    def Check_Results(self, char):
                # horizontala krece odavde (Horizonatl Check)
        if (((self.btns[0][0]["text"] == char) and (self.btns[0][1]["text"] == char)
            and (self.btns[0][2]["text"] == char)) or
                ((self.btns[1][0]["text"] == char) and (self.btns[1][1]["text"] == char)
                and(self.btns[1][2]["text"] == char)) or
                ((self.btns[2][0]["text"] == char) and (self.btns[2][1]["text"] == char)
                 and (self.btns[2][2]["text"] == char)) or
                # vertikala krece odavde (Vertical Check)
                ((self.btns[0][0]["text"] == char) and (self.btns[1][0]["text"] == char)
                 and (self.btns[2][0]["text"] == char)) or
                ((self.btns[0][1]["text"] == char) and (self.btns[1][1]["text"] == char)
                 and (self.btns[2][1]["text"] == char)) or
                ((self.btns[0][2]["text"] == char) and (self.btns[1][2]["text"] == char)
                 and (self.btns[2][2]["text"] == char)) or
                # dijagonala krece odavde (Diagonal Check)
                ((self.btns[0][0]["text"] == char) and (self.btns[1][1]["text"] == char)
                 and (self.btns[2][2]["text"] == char)) or
                ((self.btns[0][2]["text"] == char) and (self.btns[1][1]["text"] == char)
                 and (self.btns[2][0]["text"] == char))
        ):
            self.Result(char)
        elif self.count == 9:
            self.Result("Draw")

    def Result(self, char):
        top = tk.Toplevel(self)     # novi top prozor koji iskace sa odrenjenom informacijom (WIN, DRAW...)
        if char == "Draw":
            top.title("OOPS!")
            topText = tk.Label(top, text=f"It is a Draw!", font="Calibre 30 bold", fg="red")
        else:
            top.title("Congratulations!")
            topText = tk.Label(top, text=f"{char} is a Winner!", font="Calibre 30 bold", fg="blue")

        topButton = tk.Button(top, text="New Game", bg="black", fg="white",
                              activebackground="blue3", activeforeground="white", command=self.NEWGAME)
        quit = tk.Button(top, text="QUIT",
                  bg="black", fg="white", activebackground="blue3", activeforeground="white",
                  command=self.destroy)
        topText.grid(row=0, column=0, padx=10, pady=10)
        topButton.grid(row=1, column=0)
        quit.grid(row=2, column=0, padx=12, pady=10)

TICKTACKTOE().mainloop()