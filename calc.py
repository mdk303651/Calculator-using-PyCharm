import tkinter as tk
from tkinter import ttk
import math


class AdvancedCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Calculator")
        self.root.geometry("400x550")
        self.root.resizable(False, False)

        # Set theme colors
        self.bg_color = "#2C3E50"  # Dark blue background
        self.button_color = "#34495E"  # Darker blue for buttons
        self.text_color = "#ECF0F1"  # White-ish text
        self.accent_color = "#E74C3C"  # Red accent
        self.secondary_accent = "#3498DB"  # Light blue accent

        # Configure the main window
        self.root.configure(bg=self.bg_color)

        # Initialize the expression variable
        self.current_expression = ""
        self.display_text = tk.StringVar()
        self.display_text.set("0")

        # Create the display and signature
        self.create_display()

        # Create calculator buttons
        self.create_buttons()

        # Add signature
        self.add_signature()

    def create_display(self):
        # Display frame
        display_frame = tk.Frame(self.root, bg=self.bg_color)
        display_frame.pack(padx=10, pady=10, fill=tk.X)

        # Main display
        display = tk.Entry(
            display_frame,
            textvariable=self.display_text,
            font=("Helvetica", 24),
            bg=self.bg_color,
            fg=self.text_color,
            bd=0,
            justify=tk.RIGHT
        )
        display.pack(padx=5, pady=5, fill=tk.X)

    def create_buttons(self):
        # Buttons frame
        buttons_frame = tk.Frame(self.root, bg=self.bg_color)
        buttons_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Configure grid
        for i in range(6):
            buttons_frame.rowconfigure(i, weight=1)
        for i in range(4):
            buttons_frame.columnconfigure(i, weight=1)

        # Button details: text, row, column, bg_color, command
        button_data = [
            ("C", 0, 0, self.accent_color, lambda: self.clear()),
            ("±", 0, 1, self.secondary_accent, lambda: self.negate()),
            ("%", 0, 2, self.secondary_accent, lambda: self.percent()),
            ("÷", 0, 3, self.secondary_accent, lambda: self.add_to_expression("/")),

            ("7", 1, 0, self.button_color, lambda: self.add_to_expression("7")),
            ("8", 1, 1, self.button_color, lambda: self.add_to_expression("8")),
            ("9", 1, 2, self.button_color, lambda: self.add_to_expression("9")),
            ("×", 1, 3, self.secondary_accent, lambda: self.add_to_expression("*")),

            ("4", 2, 0, self.button_color, lambda: self.add_to_expression("4")),
            ("5", 2, 1, self.button_color, lambda: self.add_to_expression("5")),
            ("6", 2, 2, self.button_color, lambda: self.add_to_expression("6")),
            ("-", 2, 3, self.secondary_accent, lambda: self.add_to_expression("-")),

            ("1", 3, 0, self.button_color, lambda: self.add_to_expression("1")),
            ("2", 3, 1, self.button_color, lambda: self.add_to_expression("2")),
            ("3", 3, 2, self.button_color, lambda: self.add_to_expression("3")),
            ("+", 3, 3, self.secondary_accent, lambda: self.add_to_expression("+")),

            ("0", 4, 0, self.button_color, lambda: self.add_to_expression("0"), 2),
            (".", 4, 2, self.button_color, lambda: self.add_to_expression(".")),
            ("=", 4, 3, self.accent_color, lambda: self.calculate()),

            ("sin", 5, 0, self.secondary_accent, lambda: self.calculate_scientific("sin")),
            ("cos", 5, 1, self.secondary_accent, lambda: self.calculate_scientific("cos")),
            ("tan", 5, 2, self.secondary_accent, lambda: self.calculate_scientific("tan")),
            ("√", 5, 3, self.secondary_accent, lambda: self.calculate_scientific("sqrt"))
        ]

        # Create buttons
        for data in button_data:
            text, row, col, bg, command = data[:5]
            colspan = 1
            if len(data) > 5:
                colspan = data[5]

            button = tk.Button(
                buttons_frame,
                text=text,
                font=("Helvetica", 16),
                bg=bg,
                fg=self.text_color,
                bd=0,
                highlightthickness=0,
                activebackground=self.secondary_accent if bg == self.button_color else bg,
                activeforeground=self.text_color,
                command=command
            )
            button.grid(row=row, column=col, columnspan=colspan, padx=5, pady=5, sticky="nsew")

    def add_signature(self):
        # Signature frame
        signature_frame = tk.Frame(self.root, bg=self.bg_color)
        signature_frame.pack(padx=5, pady=5, fill=tk.X)

        # Signature text
        signature = tk.Label(
            signature_frame,
            text="© Created by Kamrul Islam Anik",
            font=("Helvetica", 8),
            fg=self.text_color,
            bg=self.bg_color
        )
        signature.pack(side=tk.RIGHT, padx=10, pady=5)

    def add_to_expression(self, value):
        # Handle initial zero and first input
        if self.current_expression == "" and value in "0123456789":
            self.current_expression = value
        elif self.current_expression == "0" and value in "0123456789":
            self.current_expression = value
        else:
            self.current_expression += value

        self.update_display()

    def clear(self):
        self.current_expression = ""
        self.update_display()

    def calculate(self):
        try:
            # Evaluate the expression
            result = eval(self.current_expression)
            self.current_expression = str(result)
        except Exception as e:
            self.current_expression = "Error"

        self.update_display()

    def negate(self):
        if self.current_expression:
            try:
                value = eval(self.current_expression)
                self.current_expression = str(-value)
                self.update_display()
            except:
                pass

    def percent(self):
        if self.current_expression:
            try:
                value = eval(self.current_expression)
                self.current_expression = str(value / 100)
                self.update_display()
            except:
                pass

    def calculate_scientific(self, operation):
        try:
            value = eval(self.current_expression)

            if operation == "sin":
                result = math.sin(math.radians(value))
            elif operation == "cos":
                result = math.cos(math.radians(value))
            elif operation == "tan":
                result = math.tan(math.radians(value))
            elif operation == "sqrt":
                result = math.sqrt(value)

            self.current_expression = str(result)
            self.update_display()
        except Exception as e:
            self.current_expression = "Error"
            self.update_display()

    def update_display(self):
        if not self.current_expression:
            self.display_text.set("0")
        else:
            self.display_text.set(self.current_expression)


if __name__ == "__main__":
    root = tk.Tk()
    app = AdvancedCalculator(root)
    root.mainloop()