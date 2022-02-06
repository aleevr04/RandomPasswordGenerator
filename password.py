import tkinter as tk
import random, string, clipboard

# Colors
LIGHT_GREY = '#555'

class Generator:
    large_font = ('Arial', 16)
    mid_font = ('Arial', 14)
    small_font = ('Arial', 12)

    def __init__(self):
        # Main Window Setup
        self.window = tk.Tk()
        self.window.title('Password Generator')
        self.window.resizable(0, 0)

        # Length Label Frame
        self.length_lb = tk.LabelFrame(self.window, text = 'Length of your password', font = self.mid_font)
        self.length_lb.pack(fill = tk.X, padx = 20, pady = 20)

        # Checkboxes Label Frame
        self.check_lb = tk.LabelFrame(self.window, text = 'What do you want to include?', font = self.mid_font)
        self.check_lb.pack(fill = tk.X, padx = 20)

        # Checkboxes Variables (used to check their values: 0 or 1)
        self.want_symbols = tk.IntVar()
        self.want_numbers = tk.IntVar()
        self.want_upper = tk.IntVar()
        self.want_lower = tk.IntVar()

        # Password Frame
        self.pw_frame = tk.Frame(self.window)
        self.pw_frame.pack(fill = tk.X, padx = 20, pady = 20)
        self.pw_frame.grid_rowconfigure(0, weight=1)
        self.pw_frame.grid_columnconfigure(0, weight=1)
    
    def generate(self):
        try:
            length = int(self.length_entry.get())
            
            # Length is negative
            if length < 0:
                self.pw_entry.delete(0, tk.END)
                self.pw_entry.insert(0, 'Your length should not be negative')
            
            # None of the boxes are selected
            elif self.want_upper.get() == 0 and self.want_lower.get() == 0 and self.want_numbers.get() == 0 and self.want_symbols.get() == 0:
                self.pw_entry.delete(0, tk.END)
                self.pw_entry.insert(0, 'Please select al least one box')
                
            else:
                # If we don't select their boxes, they will be empty.
                # So when we sum they are not included
                upper = string.ascii_uppercase if self.want_upper.get() else ''
                lower = string.ascii_lowercase if self.want_lower.get() else ''
                nums = string.digits if self.want_numbers.get() else ''
                symbols = '!@#$%&*-_:?' if self.want_symbols.get() else ''

                total_chars = upper + lower + nums + symbols

                password = []

                # We add random chars from total_chars
                for i in range(length):
                    password.append(random.choice(total_chars))

                # We shuffle the characters
                random.shuffle(password)

                # We clear the entry and insert the password
                self.pw_entry.delete(0, tk.END)
                self.pw_entry.insert(0, ''.join(password))
        except ValueError:
            pass

    def copy(self):
        password = self.pw_entry.get()

        clipboard.copy(password)

    def create_length_entry(self):
        self.length_entry = tk.Entry(self.length_lb, font = self.mid_font)
        self.length_entry.pack(fill = tk.X, padx = 10, pady = 20)
    
    def create_checkboxes(self):
        # Symbols
        self.symbols_checkbox = tk.Checkbutton(self.check_lb, text = 'Symbols', font = self.small_font, variable = self.want_symbols)
        self.symbols_checkbox.pack(padx = 5, pady = 20, side = tk.LEFT)

        # Numbers
        self.symbols_checkbox = tk.Checkbutton(self.check_lb, text = 'Numbers', font = self.small_font, variable = self.want_numbers)
        self.symbols_checkbox.pack(padx = 5, pady = 20, side = tk.LEFT)

        # Uppercase
        self.symbols_checkbox = tk.Checkbutton(self.check_lb, text = 'Uppercase', font = self.small_font, variable = self.want_upper)
        self.symbols_checkbox.pack(padx = 5, pady = 20, side = tk.LEFT)

        # Lowercase
        self.symbols_checkbox = tk.Checkbutton(self.check_lb, text = 'Lowercase', font = self.small_font, variable = self.want_lower)
        self.symbols_checkbox.pack(padx = 5, pady = 20, side = tk.LEFT)

    def create_gen_button(self):
        gen_button = tk.Button(self.pw_frame, text = 'Generate Random Password', font = self.large_font, command = self.generate)
        gen_button.grid(row = 0, column = 0, columnspan = 2, pady = 10, sticky = 'nsew')

    def create_pw_entry(self):
        self.pw_entry = tk.Entry(self.pw_frame, font = self.mid_font, fg = LIGHT_GREY)
        self.pw_entry.insert(0, 'Your password appears here') # Placeholder
        self.pw_entry.grid(row = 1, column = 0, ipady = 5, sticky = 'nsew')

    def create_copy_button(self):
        copy_button = tk.Button(self.pw_frame, text = 'Copy', font = self.mid_font, width = 8, command = self.copy)
        copy_button.grid(row = 1, column = 1)

    def create_widgets(self):
        self.create_length_entry()
        self.create_checkboxes()
        self.create_gen_button()
        self.create_copy_button()
        self.create_pw_entry()

    def run(self):
        self.create_widgets()
        self.window.mainloop()

generator = Generator()
generator.run()