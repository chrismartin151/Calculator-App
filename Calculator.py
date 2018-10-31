#Chris Martin
#10/29/18
#CS480

import tkinter as tk


class Calculator:

    equation = ""

    def __init__(self):

        self.root = tk.Tk()
        self.root.title("Spoopy Calculator")
        self.root.geometry("376x500")
        self.root.configure(background='black')
        self.root.iconbitmap("pumpkin.ico")

        self.wide = 94
        self.high = 75
        self.text_font = 'Helvetica'
        self.text_size = 25
        self.text_style = 'bold'
        self.color = '#ff9900'
        self.color2 = '#ffcc80'

        self.button_clear = tk.Button(self.root, text='CE', command=self.clear, bg=self.color,
                                      font=(self.text_font, self.text_size, self.text_style))
        self.button_clear.place(x=0, y=125, width=self.wide, height=self.high)

        self.button_add = tk.Button(self.root, text='+', command=lambda: self.append('+'), bg=self.color,
                                    font=(self.text_font, self.text_size, self.text_style))
        self.button_add.place(x=94, y=125, width=self.wide, height=self.high)

        self.button_subtract = tk.Button(self.root, text='-', command=lambda: self.append('-'), bg=self.color,
                                         font=(self.text_font, self.text_size, self.text_style))
        self.button_subtract.place(x=188, y=125, width=self.wide, height=self.high)

        self.button_multiply = tk.Button(self.root, text='*', command=lambda: self.append('*'), bg=self.color,
                                         font=(self.text_font, self.text_size, self.text_style))
        self.button_multiply.place(x=282, y=125, width=self.wide, height=self.high)

        self.button_divide = tk.Button(self.root, text='/', command=lambda: self.append('/'), bg=self.color2,
                                       font=(self.text_font, self.text_size, self.text_style))
        self.button_divide.place(x=282, y=200, width=self.wide, height=self.high)

        self.button_exponent = tk.Button(self.root, text='^', command=lambda: self.append('^'), bg=self.color,
                                         font=(self.text_font, self.text_size, self.text_style))
        self.button_exponent.place(x=282, y=275, width=self.wide, height=self.high)

        self.button_equal = tk.Button(self.root, text='=', command=lambda: self.solve(self.equation), bg=self.color2,
                                      font=(self.text_font, self.text_size, self.text_style))
        self.button_equal.place(x=282, y=350, width=self.wide, height=self.high)

        self.button_left_par = tk.Button(self.root, text='(', command=lambda: self.append('('), bg=self.color,
                                         font=(self.text_font, self.text_size, self.text_style))
        self.button_left_par.place(x=188, y=425, width=self.wide, height=self.high)

        self.button_right_par = tk.Button(self.root, text=')', command=lambda: self.append(')'), bg=self.color,
                                          font=(self.text_font, self.text_size, self.text_style))
        self.button_right_par.place(x=282, y=425, width=self.wide, height=self.high)

        self.button_decimal = tk.Button(self.root, text='.', command=lambda: self.append('.'), bg=self.color,
                                        font=(self.text_font, self.text_size, self.text_style))
        self.button_decimal.place(x=0, y=425, width=self.wide, height=self.high)

        self.button_zero = tk.Button(self.root, text='0', command=lambda: self.append('0'), bg=self.color,
                                     font=(self.text_font, self.text_size, self.text_style))
        self.button_zero.place(x=94, y=425, width=self.wide, height=self.high)

        self.button_one = tk.Button(self.root, text='1', command=lambda: self.append('1'), bg=self.color2,
                                    font=(self.text_font, self.text_size, self.text_style))
        self.button_one.place(x=0, y=350, width=self.wide, height=self.high)

        self.button_two = tk.Button(self.root, text='2', command=lambda: self.append('2'), bg=self.color2,
                                    font=(self.text_font, self.text_size, self.text_style))
        self.button_two.place(x=94, y=350, width=self.wide, height=self.high)

        self.button_three = tk.Button(self.root, text='3', command=lambda: self.append('3'), bg=self.color2,
                                      font=(self.text_font, self.text_size, self.text_style))
        self.button_three.place(x=188, y=350, width=self.wide, height=self.high)

        self.button_four = tk.Button(self.root, text='4', command=lambda: self.append('4'), bg=self.color,
                                     font=(self.text_font, self.text_size, self.text_style))
        self.button_four.place(x=0, y=275, width=self.wide, height=self.high)

        self.button_five = tk.Button(self.root, text='5', command=lambda: self.append('5'), bg=self.color,
                                     font=(self.text_font, self.text_size, self.text_style))
        self.button_five.place(x=94, y=275, width=self.wide, height=self.high)

        self.button_six = tk.Button(self.root, text='6', command=lambda: self.append('6'), bg=self.color,
                                    font=(self.text_font, self.text_size, self.text_style))
        self.button_six.place(x=188, y=275, width=self.wide, height=self.high)

        self.button_seven = tk.Button(self.root, text='7', command=lambda: self.append('7'), bg=self.color2,
                                      font=(self.text_font, self.text_size, self.text_style))
        self.button_seven.place(x=0, y=200, width=self.wide, height=self.high)

        self.button_eight = tk.Button(self.root, text='8', command=lambda: self.append('8'), bg=self.color2,
                                      font=(self.text_font, self.text_size, self.text_style))
        self.button_eight.place(x=94, y=200, width=self.wide, height=self.high)

        self.button_nine = tk.Button(self.root, text='9', command=lambda: self.append('9'), bg=self.color2,
                                     font=(self.text_font, self.text_size, self.text_style))
        self.button_nine.place(x=188, y=200, width=self.wide, height=self.high)

        self.equation = ''

        self.equation_SV = tk.StringVar()
        self.equation_SV.set(' ')

        self.final = 0


        pass

    def __del__(self):
        pass

    def api(self):
        self.root.after(0, self.equate())
        self.root.mainloop()

    def equate(self):
        self.show = tk.Label(self.root, textvariable=self.equation_SV, anchor='e', bg=self.color2,
                             font=(self.text_font, self.text_size, self.text_style))
        self.show.place(x=0, y=0, width=375, height=125)

    def append(self, stringy):
        self.equation = self.equation + stringy
        self.equation_SV.set(self.equation)

    def clear(self):
        self.equation = ""
        self.equation_SV.set(self.equation)

    def solve(self, expression):
        counter = 0
        paren_counter = 0
        exponent = False
        e = 0
        if len(expression) == 1:
            self.equation_SV.set("Error! Please Try Again!")
            self.equation = ""
            return
        for i in expression:
            if exponent is True:
                counter += 1
                exponent = False
                continue
            if expression[counter] in {"+", "-", "^", "*", "/"}:
                if counter == 0:
                    self.equation_SV.set("Error! Please Try Again!")
                    self.equation = ""
                    return
                if counter == len(expression)-1:
                    self.equation_SV.set("Error! Please Try Again!")
                    self.equation = ""
                    return
                if expression[counter + 1] in {"+", "-", "^", "*", "/"}:
                    self.equation_SV.set("Error! Please Try Again!")
                    self.equation = ""
                    return
                if expression[counter - 1] in {"+", "-", "^", "*", "/"}:
                    self.equation_SV.set("Error! Please Try Again!")
                    self.equation = ""
                    return
            if expression[counter] in {"(", ")"}:
                paren_counter += 1
                if expression[counter] == "(":
                    if counter == len(expression):
                        self.equation_SV.set("Error! Please Try Again!")
                        self.equation = ""
                        return
                    elif expression[counter + 1] == ")":
                        self.equation_SV.set("Error! Please Try Again!")
                        self.equation = ""
                        return
                elif expression[counter] == ")":
                    if counter == 0:
                        self.equation_SV.set("Error! Please Try Again!")
                        self.equation = ""
                        return
                    elif expression[counter - 1] == "(":
                        self.equation_SV.set("Error! Please Try Again!")
                        self.equation = ""
                        return
            if expression[counter] == "^":
                if counter + 1 == len(expression):
                    self.equation_SV.set("Error! Please Try Again!")
                    self.equation = ""
                    return
                expression = expression[ : counter] + "**" + expression[counter + 1 : ]
                exponent = True
            counter += 1
        if paren_counter % 2 == 1:
            self.equation_SV.set("Error! Please Try Again!")
            self.equation = ""
            return
        try:
            if expression == str(eval(expression)):
                self.equation_SV.set("Error! Please Try Again!")
                self.equation = ""
                return

            expression = str(eval(expression))

        except:
            self.equation_SV.set("Error! Please Try Again!")
            self.equation = ""

        """if len(expression) > 17:
            e = len(expression[17, ])"""

        self.equation_SV.set(expression)
        self.equation = ""







calculator = Calculator()
calculator.api()

exit()
