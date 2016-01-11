import tkinter as tk
import operator
import math


class Gui:
    def __init__(self, master):
        self.total = 0
        self.ent_num = 0
        self.run = []
        self.stor = None
        self.lastop = None
        self.topfrmbtns = ['10^', '^2', '^', 'sqrt', 'sin', 'cos', 'tan', 'Mod']
        self.btmfrmbtns = ['c', 'ce', 'bk', "+", 7, 8, 9, '-', 4, 5, 6, '*', 1, 2, 3, '/', '+/-', 0, '.', '=']

        # Main Window
        self.master = master
        master.title('Calculator')
        master.minsize(340, 540)
        master.columnconfigure(0, weight=1)
        master.rowconfigure(0, weight=1)
        master.rowconfigure(1, weight=1)
        # master.bind_all('<Key>', butt.key)

        # Top Frame
        topfrm = tk.Frame(master, bg='#000000')
        topfrm.grid(row=0, column=0, sticky='nsew')
        for x in range(4):
            topfrm.columnconfigure(x, weight=1)
        for y in range(4):
            topfrm.rowconfigure(y, weight=1)

        # Bottom Frame
        btmfrm = tk.Frame(master, bg='#484848')
        btmfrm.grid(row=1, column=0, sticky='nsew')
        for x in range(4):
            btmfrm.columnconfigure(x, weight=1)
        for y in range(5):
            btmfrm.rowconfigure(y, weight=1)

        # Top Label
        self.runtot = tk.StringVar()
        self.runtot.set(self.run)
        self.total_label = tk.Label(topfrm, textvariable=self.runtot, fg='#FFFFFF', bg='#000000', justify='right',
                                    anchor='e', font=('Cambria', '10'))
        self.total_label.grid(row=0, column=0, columnspan=4, sticky='nsew')

        # Text Box
        vcmd = master.register(self.isnum)
        self.entry = tk.Entry(topfrm, validate='key', validatecommand=(vcmd, '%P'), font=('Cambria', '24', 'bold'),
                              justify='right', bd=2, relief='sunken', fg='#FFFFFF', bg='#000000')
        self.entry.grid(row=1, column=0, columnspan=4, sticky='nsew')

        # Generate Buttons
        r = 2
        c = 0
        for t in self.topfrmbtns:
            btn = tk.Button(topfrm, text=self.char(t), font=('Cambria', '13', 'bold'), fg='#FFFFFF', bg='#000000',
                            bd=0, command=lambda t=t: self.asimeth(t))
            btn.grid(row=r, column=c, sticky='nsew')
            btn.bind("<Enter>", lambda event, e=btn: e.configure(bg="#A9A9A9"))
            btn.bind("<Leave>", lambda event, l=btn: l.configure(bg="#000000"))
            c += 1
            if c > 3:
                c = 0
                r += 1
        r = 0
        c = 0
        for b in self.btmfrmbtns:
            btn = tk.Button(btmfrm, text=self.char(b), font=('Cambria', '13', 'bold'), fg='#FFFFFF', bg='#808080',
                            bd=0, command=lambda b=b: self.asimeth(b))
            btn.grid(row=r, column=c, sticky='nsew')
            btn.bind("<Enter>", lambda event, e=btn: e.configure(bg="#A9A9A9"))
            btn.bind("<Leave>", lambda event, l=btn: l.configure(bg="#808080"))
            c += 1
            if c > 3:
                c = 0
                r += 1

    # Checks Entry is a Number
    def isnum(self, new_text):
        if not new_text:
            gui.ent_num = 0
            return True
        try:
            gui.ent_num = float(new_text)
            return True
        except ValueError:
            return False

    # Assigns Unicode Characters to the sqrt, 10^, ^2, ^, bk buttons
    def char(self, char):
        if char not in ('sqrt', '10^', '^2', '^', 'bk'):
            return char
        elif char == 'sqrt':
            return '\u221a'
        elif char == '^':
            return 'x\u207f'
        elif char == '^2':
            return 'x\u00b2'
        elif char == '10^':
            return '10 \u02e3'
        elif char == 'bk':
            return '\u25c0'

    # Assigns Methods to Buttons
    def asimeth(self, op):
        if op in range(10) or op == '.':
            butt.nums(op)
        elif op in ('+', '-', '*', '/', 'Mod', '^'):
            butt.oper(op)
        elif op in ('10^', '^2'):
            butt.pow(op)
        elif op == 'sqrt':
            butt.sqrt()
        elif op in ('sin', 'cos', 'tan'):
            butt.sct(op)
        elif op in ('c', 'ce', 'bk'):
            butt.clear(op)
        elif op == '+/-':
            butt.neg()
        elif op == '=':
            butt.equals()


class Buttons:
    def __init__(self):
        self.isqr = False
        self.ops = {'+': operator.add,
                    '-': operator.sub,
                    '*': operator.mul,
                    '/': operator.truediv,
                    'Mod': operator.mod,
                    '^': math.pow,
                    'sin': math.sin,
                    'cos': math.cos,
                    'tan': math.tan
                    }

    ''' I never could get this section of code to work with binding <Key> to the main window

    # Handles keyboard input
    def key(self, event):
        key = event.keysym
        if key in range(1, 10) or key == '.':
           self.nums(key)
        elif key in ('+', '-', '*', '/', '%', '^'):
           self.oper(key)
        elif key == '=':
           self.equals()'''

    # Clear, Clear Entry, Back
    def clear(self, clear):
        if clear == 'c':
            gui.total = 0
            gui.entry.delete(0, tk.END)
            gui.run = []
            gui.runtot.set(gui.run)
            gui.stor = None
            gui.lastop = None
        elif clear == 'ce':
            gui.entry.delete(0, tk.END)
        elif clear == 'bk':
            entry = gui.entry.get()
            length = len(entry)
            gui.entry.delete(length - 1, tk.END)

    # Numbers & Decimal
    def nums(self, num):
        if self.isqr is True:
            self.isqr = False
            del gui.run[2:6]
            gui.entry.delete(0, tk.END)
            gui.entry.insert(0, num)
        elif gui.ent_num == gui.total:
            gui.entry.delete(0, tk.END)
            gui.entry.insert(0, num)
        else:
            gui.entry.insert('end', num)

    # Negative
    def neg(self):
        negative = gui.ent_num * -1
        gui.entry.delete(0, tk.END)
        gui.entry.insert(0, negative)

    # Add, Subtract, Multiply, Divide, Mod, Power
    def oper(self, op):
        if gui.stor is None:
            gui.stor = gui.ent_num
            gui.run.append(gui.ent_num)
            gui.run.append(op)
            gui.lastop = self.ops[op]
            gui.entry.delete(0, tk.END)
        elif self.isqr is True:
            gui.run.append(op)
            gui.lastop = self.ops[op]
            gui.entry.delete(0, tk.END)
            gui.entry.insert(0, gui.total)
            self.isqr = False
        else:
            if gui.lastop == operator.truediv and gui.ent_num == 0:
                gui.total = 0
                gui.entry.delete(0, tk.END)
                del gui.run[:]
                gui.run.append('Cannot divide by zero')
                gui.stor = None
                gui.lastop = None
            else:
                gui.total = gui.lastop(gui.stor, gui.ent_num)
                gui.run.append(gui.ent_num)
                gui.run.append(op)
                gui.stor = gui.total
                gui.lastop = self.ops[op]
                gui.entry.delete(0, tk.END)
                gui.entry.insert(0, gui.total)

        gui.runtot.set(' '.join(map(str, gui.run)))

    # Square Root
    def sqrt(self):
        if gui.stor is None:
            if gui.ent_num >= 0:
                gui.total = math.sqrt(gui.ent_num)
                gui.run.append('\u221a')
                gui.run.append('(')
                gui.run.append(gui.ent_num)
                gui.run.append(')')
                gui.stor = gui.total
                self.isqr = True
                gui.lastop = None
                gui.entry.delete(0, tk.END)
                gui.entry.insert(0, gui.total)
            else:
                gui.total = 0
                gui.entry.delete(0, tk.END)
                gui.run = []
                gui.runtot = 'Invalid Entry'
                gui.stor = None
                gui.lastop = None
        else:
            gui.total = math.sqrt(gui.ent_num)
            gui.run.append('\u221a')
            gui.run.append('(')
            gui.run.append(gui.ent_num)
            gui.run.append(')')
            self.isqr = True
            gui.entry.delete(0, tk.END)
            gui.entry.insert(0, gui.total)

        gui.runtot.set(''.join(map(str, gui.run)))

    # X Square and Ten Power
    def pow(self, op):
        if op == '^2':
            if gui.stor is None:
                gui.total = gui.ent_num ** 2
                gui.run.append('sqr(')
                gui.run.append(gui.ent_num)
                gui.run.append(')')
                self.isqr = True
                gui.lastop = None
                gui.stor = gui.total
                gui.entry.delete(0, tk.END)
                gui.entry.insert(0, gui.total)
            else:
                gui.total = gui.ent_num ** 2
                gui.run.append('sqr(')
                gui.run.append(gui.ent_num)
                gui.run.append(')')
                self.isqr = True
                gui.entry.delete(0, tk.END)
                gui.entry.insert(0, gui.total)
        elif op == '10^':
            if gui.stor is None:
                gui.total = 10 ** gui.ent_num
                gui.run.append('10^(')
                gui.run.append(gui.ent_num)
                gui.run.append(')')
                self.isqr = True
                gui.lastop = None
                gui.stor = gui.total
                gui.entry.delete(0, tk.END)
                gui.entry.insert(0, gui.total)
        else:
            gui.total = 10 ** gui.ent_num
            gui.run.append('10^(')
            gui.run.append(gui.ent_num)
            gui.run.append(')')
            self.isqr = True
            gui.entry.delete(0, tk.END)
            gui.entry.insert(0, gui.total)

        gui.runtot.set(''.join(map(str, gui.run)))

    # Sin, Cos, Tan
    def sct(self, op):
        if op == 'sin':
            labl = 'sin'
        elif op == 'cos':
            labl = 'cos'
        elif op == 'tan':
            labl = 'tan'
        if gui.stor is None:
            gui.total = self.ops[op](gui.ent_num)
            gui.run.append(labl)
            gui.run.append('(')
            gui.run.append(gui.ent_num)
            gui.run.append(')')
            self.isqr = True
            gui.lastop = None
            gui.stor = gui.total
            gui.entry.delete(0, tk.END)
            gui.entry.insert(0, gui.total)
        else:
            gui.total = self.ops[op](gui.ent_num)
            gui.run.append(labl)
            gui.run.append('(')
            gui.run.append(gui.ent_num)
            gui.run.append(')')
            self.isqr = True
            gui.entry.delete(0, tk.END)
            gui.entry.insert(0, gui.total)

        gui.runtot.set(''.join(map(str, gui.run)))

    # Equals Button
    def equals(self):
        if gui.lastop == operator.truediv and gui.ent_num == 0:
            gui.total = 0
            gui.entry.delete(0, tk.END)
            del gui.run[:]
            gui.run.append('Cannot divide by zero')
            gui.stor = None
            gui.lastop = None
        elif gui.stor is not None:
            gui.total = gui.lastop(gui.stor, gui.ent_num)
            del gui.run[:]
            gui.stor = None

        gui.entry.delete(0, tk.END)
        gui.entry.insert(0, gui.total)
        gui.runtot.set(''.join(map(str, gui.run)))

butt = Buttons()
root = tk.Tk()
gui = Gui(root)
root.mainloop()
