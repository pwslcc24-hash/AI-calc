import tkinter as tk
from tkinter import font


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        
        self.expression = ""
        
        # Entry field
        self.entry = tk.Entry(
            root,
            font=("Arial", 20),
            borderwidth=2,
            relief=tk.SUNKEN,
            justify=tk.RIGHT
        )
        self.entry.pack(fill=tk.BOTH, padx=10, pady=10, ipady=10)
        
        # Buttons frame
        buttons_frame = tk.Frame(root)
        buttons_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        # Button layout
        button_layout = [
    ["1", "2", "3", "+"],
    ["4", "5", "6", "-"],
    ["7", "8", "9", "*"],
    ["0", ".", "=", "/"],
    ["C"]
]
        
        for row in button_layout:
            row_frame = tk.Frame(buttons_frame)
            row_frame.pack(fill=tk.BOTH, expand=True, pady=5)
            
            for btn_text in row:
                btn = tk.Button(
                    row_frame,
                    text=btn_text,
                    font=("Arial", 18),
                    command=lambda text=btn_text: self.on_button_click(text)
                )
                btn.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
    
    def on_button_click(self, char):
        if char == "=":
            self.evaluate()
        elif char == "C":
            self.clear()
        else:
            self.expression += char
            self.entry.delete(0, tk.END)
            self.entry.insert(0, self.expression)
    
    def evaluate(self):
        try:
            result = eval(self.expression)
            self.expression = str(result)
            self.entry.delete(0, tk.END)
            self.entry.insert(0, self.expression)
        except Exception as e:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Error")
            self.expression = ""
    
    def clear(self):
        self.expression = ""
        self.entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
