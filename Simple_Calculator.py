from tkinter import *
from math import *

"""
* The super() builtin returns a proxy object (temporary object of the superclass)
  that allows us to access methods of the base class.
* super() can take two arguments, super(subclass, an object that is an instance of that subclass) 
  so here we call the parent class of sub class object.
"""


class Calculator(Frame):

    def __init__(self, master):

        super(Calculator, self).__init__(master)
        self.config(bg='gray')
        self.task = ''
        self.data = ''
        self.answer = ''
        self.hist = 'no calculations yet !'
        self.UserIn = StringVar()
        self.grid()

        self.user_input = Entry(self, bg='black', fg='orange', bd=29, insertwidth=2, width=24,
                                font=('Verdana', 20, 'bold'), insertbackground='white',
                                textvariable=self.UserIn, justify=RIGHT)

        self.b7 = Button(self, bg='black', fg='gray', bd=12, text='7', padx=33, pady=25,
                         font=('Helvetica', 20, 'bold'), command=lambda: self.button_click(7))

        self.b8 = Button(self, bg='black', fg='gray', bd=12, text='8', padx=33, pady=25,
                         font=('Helvetica', 20, 'bold'), command=lambda: self.button_click(8))

        self.b9 = Button(self, bg='black', fg='gray', bd=12, text='9', padx=33, pady=25,
                         font=('Helvetica', 20, 'bold'), command=lambda: self.button_click(9))

        self.b4 = Button(self, bg='black', fg='gray', bd=12, text='4', padx=33, pady=25,
                         font=('Helvetica', 20, 'bold'), command=lambda: self.button_click(4))

        self.b5 = Button(self, bg='black', fg='gray', bd=12, text='5', padx=33, pady=25,
                         font=('Helvetica', 20, 'bold'), command=lambda: self.button_click(5))

        self.b6 = Button(self, bg='black', fg='gray', bd=12, text='6', padx=33, pady=25,
                         font=('Helvetica', 20, 'bold'), command=lambda: self.button_click(6))

        self.b1 = Button(self, bg='black', fg='gray', bd=12, text='1', padx=33, pady=25,
                         font=('Helvetica', 20, 'bold'), command=lambda: self.button_click(1))

        self.b2 = Button(self, bg='black', fg='gray', bd=12, text='2', padx=33, pady=25,
                         font=('Helvetica', 20, 'bold'), command=lambda: self.button_click(2))

        self.b3 = Button(self, bg='black', fg='gray', bd=12, text='3', padx=33, pady=25,
                         font=('Helvetica', 20, 'bold'), command=lambda: self.button_click(3))

        self.b0 = Button(self, bg='black', fg='gray', bd=12, text='0', padx=33, pady=25,
                         font=('Helvetica', 20, 'bold'), command=lambda: self.button_click(0))

        self.b_add = Button(self, bg='black', fg='orange', bd=12, text='+', padx=38, pady=25,
                            font=('Helvetica', 20, 'bold'), command=lambda: self.button_click('+'))

        self.b_sub = Button(self, bg='black', fg='orange', bd=12, text='-', padx=40, pady=25,
                            font=('Helvetica', 20, 'bold'), command=lambda: self.button_click('-'))

        self.b_multi = Button(self, bg='black', fg='orange', bd=12, text='*', padx=40, pady=25,
                              font=('Helvetica', 20, 'bold'), command=lambda: self.button_click('*'))

        self.b_divid = Button(self, bg='black', fg='orange', bd=12, text='/', padx=40, pady=25,
                              font=('Helvetica', 20, 'bold'), command=lambda: self.button_click('/'))

        self.b_equal = Button(self, bg='black', fg='orange', bd=12, text='=', padx=100, pady=25,
                              font=('Helvetica', 20, 'bold'), command=lambda: self.calculate_task())

        self.b_clear = Button(self, bg='black', fg='orange', bd=12, text='AC', padx=7, width=28,
                              font=('Helvetica', 20, 'bold'), command=lambda: self.clear_display())

        self.parentheses_o = Button(self, bg='black', fg='orange', bd=12, text='(', padx=33, pady=25,
                                    font=('Helvetica', 20, 'bold'), command=lambda: self.button_click('('))

        self.parentheses_c = Button(self, bg='black', fg='orange', bd=12, text=')', padx=33, pady=25,
                                    font=('Helvetica', 20, 'bold'), command=lambda: self.button_click(')'))

        self.log = Button(self, bg='black', fg='orange', bd=12, text='log', padx=33, pady=25,
                          font=('Helvetica', 20, 'bold'), command=lambda: self.button_click('log('))

        self.exp = Button(self, bg='black', fg='orange', bd=12, text='exp', padx=33, pady=25,
                          font=('Helvetica', 20, 'bold'), command=lambda: self.button_click('exp('))

        self.pow = Button(self, bg='black', fg='orange', bd=12, text='pow', padx=33, pady=25,
                          font=('Helvetica', 20, 'bold'), command=lambda: self.button_click('pow('))

        self.sqrt = Button(self, bg='black', fg='orange', bd=12, text='sqrt', padx=33, pady=25,
                           font=('Helvetica', 20, 'bold'), command=lambda: self.button_click('sqrt('))

        self.history = Button(self, bg='black', fg='orange', bd=12, text='Hist', padx=33, pady=25,
                              font=('Helvetica', 20, 'bold'), command=lambda: self.return_history())

        self.comma = Button(self, bg='black', fg='orange', bd=12, text=',', padx=33, pady=25,
                            font=('Helvetica', 20, 'bold'), command=lambda: self.button_click(','))

        self.organise_widgets()

    def organise_widgets(self):

        self.user_input.grid(row=0, column=0, columnspan=6, sticky='nsew')
        self.user_input.insert(0, '0')

        self.b_clear.grid(row=1, column=0, columnspan=6, sticky='nsew')

        self.parentheses_o.grid(row=2, column=0, sticky='nsew')
        self.parentheses_c.grid(row=2, column=1, sticky='nsew')

        self.b7.grid(row=2, column=2, sticky='nsew')
        self.b8.grid(row=2, column=3, sticky='nsew')
        self.b9.grid(row=2, column=4, sticky='nsew')
        self.b_add.grid(row=2, column=5, sticky='nsew')

        self.log.grid(row=3, column=0, sticky='nsew')
        self.exp.grid(row=3, column=1, sticky='nsew')
        self.b4.grid(row=3, column=2, sticky='nsew')
        self.b5.grid(row=3, column=3, sticky='nsew')
        self.b6.grid(row=3, column=4, sticky='nsew')
        self.b_sub.grid(row=3, column=5, sticky='nsew')

        self.pow.grid(row=4, column=0, sticky='nsew')
        self.sqrt.grid(row=4, column=1, sticky='nsew')
        self.b1.grid(row=4, column=2, sticky='nsew')
        self.b2.grid(row=4, column=3, sticky='nsew')
        self.b3.grid(row=4, column=4, sticky='nsew')
        self.b_multi.grid(row=4, column=5, sticky='nsew')

        self.history.grid(row=5, column=0, sticky='nsew')
        self.comma.grid(row=5, column=1, sticky='nsew')
        self.b0.grid(row=5, column=2, sticky='nsew')
        self.b_equal.grid(row=5, column=3, columnspan=2, sticky='nsew')
        self.b_divid.grid(row=5, column=5, sticky='nsew')

    def button_click(self, number):
        self.task = str(self.task) + str(number)
        self.UserIn.set(self.task)

    def handler(self, event):
        self.task = str(self.task) + str(event.char)
        self.UserIn.set(self.task)

    def calculate_task(self):
        self.data = self.user_input.get()
        try:
            self.answer = eval(self.data)
            self.display_text(self.answer)
            self.task = self.answer
            self.hist = self.answer
        except SyntaxError:
            self.user_input.config(justify=CENTER)
            self.display_text('Invalid Syntax !')
            self.task = ''

    def handler_e(self, event):
        self.calculate_task()

    def display_text(self, value):
        self.user_input.delete(0, END)
        self.user_input.insert(0, value)

    def return_history(self):
        self.user_input.delete(0, END)
        if self.hist == 'no calculations yet !':
            self.user_input.config(justify=CENTER)
            self.user_input.insert(0, self.hist)
        else:
            self.user_input.insert(0, self.hist)

    def clear_display(self):
        self.task = ''
        self.user_input.delete(0, END)
        self.user_input.insert(0, '0')
        self.user_input.config(justify=RIGHT)

    def handler_clear(self, event):
        self.clear_display()


root = Tk()
root.title('Calculator')
root.resizable(width=False, height=False)
root.bind('<Escape>', lambda self: root.destroy())
calculator = Calculator(root)
for i in range(0, 10):
    root.bind(str(i), calculator.handler)
root.bind('+', calculator.handler)
root.bind('-', calculator.handler)
root.bind('*', calculator.handler)
root.bind('/', calculator.handler)
root.bind('<Return>', calculator.handler_e)
root.bind('<Delete>', calculator.handler_clear)
calculator.mainloop()
