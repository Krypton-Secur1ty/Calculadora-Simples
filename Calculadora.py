import tkinter as tk
from tkinter import ttk
import simpleeval  

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora")
        self.geometry("300x400")
        self.create_widgets()

    def create_widgets(self):
        self.entry = ttk.Entry(self, font=("Arial", 18), justify='right')
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')
        
        style = ttk.Style()
        style.configure("TButton", font=("Arial", 16), padding=10)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('÷', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('×', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0, 4)
        ]

        for (text, row, col, *args) in buttons:
            button = ttk.Button(self, text=text, command=lambda t=text: self.click_button(t))
            button.grid(row=row, column=col, sticky='nsew', padx=5, pady=5, columnspan=args[0] if args else 1)

        for i in range(6):
            self.grid_rowconfigure(i, weight=1)
            self.grid_columnconfigure(i, weight=1)

    def click_button(self, value):
        current = self.entry.get()
        if value == "=":
            try:
                current = current.replace('÷', '/').replace('×', '*')
                result = simpleeval.simple_eval(current)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif value == "C":
            self.entry.delete(0, tk.END)
        else:
            self.entry.insert(tk.END, value)

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
