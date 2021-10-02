import tkinter as tk
from tkinter import messagebox
from tkinter.constants import DISABLED
from gamemanager import Gamemanager


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.game = Gamemanager()

        self.title("Tic Tac Toe")

        canvas = tk.Canvas(self, width=400, height=400)
        canvas.grid(columnspan=3, rowspan=3)

        self.button0 = tk.Button(self, command=lambda: self.button_push(self.button0))
        self.button1 = tk.Button(self, command=lambda: self.button_push(self.button1))
        self.button2 = tk.Button(self, command=lambda: self.button_push(self.button2))

        self.button3 = tk.Button(self, command=lambda: self.button_push(self.button3))
        self.button4 = tk.Button(self, command=lambda: self.button_push(self.button4))
        self.button5 = tk.Button(self, command=lambda: self.button_push(self.button5))

        self.button6 = tk.Button(self, command=lambda: self.button_push(self.button6))
        self.button7 = tk.Button(self, command=lambda: self.button_push(self.button7))
        self.button8 = tk.Button(self, command=lambda: self.button_push(self.button8))

        self.buttons = [
            self.button0,
            self.button1,
            self.button2,
            self.button3,
            self.button4,
            self.button5,
            self.button6,
            self.button7,
            self.button8,
        ]

        self.init_buttons()

    def init_buttons(self):
        count = 0
        for i in range(3):
            for j in range(3):
                self.buttons[count].grid(row=i, column=j, sticky="wens")
                count += 1

    def disable_buttons(self):
        for but in self.buttons:
            but.config(state=DISABLED)

    def state_checker(self):
        mat = self.buttons_to_matrix()
        state = self.game.state(mat)
        print(state)

        if state == "BLUE" or state == "RED":
            self.disable_buttons()
            winner = "Blue" if state == "BLUE" else "Red"
            messagebox.showinfo("Win!", f"{winner} has won the game.")
        elif state == "FULL":
            messagebox.showinfo("Win!", f"Nobody won that's sad!")

    def button_push(self, button):
        if self.game.player:
            button.config(bg="blue", state=DISABLED)
        else:
            button.config(bg="red", state=DISABLED)

        self.state_checker()
        self.game.turn_player()

    def buttons_to_matrix(self):
        tmp = []
        mat = []
        for but in self.buttons:
            if but.cget("bg") == "blue":
                tmp.append(1)
            elif but.cget("bg") == "red":
                tmp.append(0)
            else:
                tmp.append(-1)

        for i in [0, 3, 6]:
            mat.append(tmp[i : i + 3])

        return mat


def main():
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()
