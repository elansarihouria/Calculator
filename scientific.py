import tkinter as tk
from math import *
from random import *
import os
# used to switch between units of rad, and deg mke calc on deg as default
convert_constant = pi / 180
inverse_convert_constant = 180 / pi

btn_params = {
    'padx': 16,
    'pady': 1,
    'bd': 4,
    'fg': '#f2f2f2',
    'bg': '#484848',
    'font': ('arial', 18),
    'width': 5,
    'height': 2,
    'relief': 'flat',
    'activebackground': "#666666",
    'highlightbackground':'#303030'
}
number_params = {
    'padx': 16,
    'pady': 1,
    'bd': 4,
    'fg': '#f2f2f2',
    'bg': '#696969',
    'font': ('arial', 18),
    'width': 5,
    'height': 2,
    'relief': 'flat',
    'activebackground': "#666666",
    'highlightbackground':'#303030'
}
menu_params={

    'fg': 'orange',
    'bg': '#303030',
    'font': ('arial', 12),
    'bd':0

}
opertors_params={
    'padx': 16,
    'pady': 1,
    'bd': 4,
    'fg': '#f2f2f2',
    'bg': 'orange',
    'font': ('arial', 18),
    'width': 5,
    'height': 2,
    'relief': 'flat',
    'activebackground': "#666666",
    'highlightbackground':'#303030'
}

def fsin(arg):
    return sin(arg * convert_constant)


def fcos(arg):
    return cos(arg * convert_constant)


def ftan(arg):
    return tan(arg * convert_constant)


def arcsin(arg):
    return inverse_convert_constant * (asin(arg))


def arccos(arg):
    return inverse_convert_constant * (acos(arg))


def arctan(arg):
    return inverse_convert_constant * (atan(arg))



class Calculator:
    def __init__(self, master):
        # expression that will be displayed on screen
        self.expression = ""
        # be used to store data in memory
        self.recall = ""
        # self.answer
        self.sum_up = ""
        # create string for text input
        self.text_input = tk.StringVar()
        # assign instance to master
        self.master = master
        self.menubar=tk.Menu(master, **menu_params)

        self.menubar.add_command(label="simple",command=switch)
        #menubar.pack(side=tkinter.TOP)
        master.config(menu=self.menubar)
        # set frame showing inputs
        top_frame = tk.Frame(master, width=650, height=50, relief='flat', bg='#303030')
        top_frame.pack(side=tk.TOP)
        # set frame showing all button
        bottom_frame = tk.Frame(master, width=650, height= 470,relief='flat', bg='#666666')
        bottom_frame.pack(side=tk.BOTTOM)
        self.text_input.set("0")
        # entry interface for inputs
        txt_display = tk.Entry(top_frame,font=('arial',36),relief='flat',
        bg="#303030",fg='white', justify='right',width=30, bd=2, textvariable=self.text_input,highlightbackground ='#303030')
        txt_display.pack()

        # row 0
        # left bracket button
        self.btn_left_brack = tk.Button(bottom_frame,**btn_params, text= "(",command=lambda: self.btn_click('('))
        self.btn_left_brack.grid(row=0, column=0)
        # right bracket button
        self.btn_right_brack = tk.Button(bottom_frame, **btn_params, text=")", command=lambda: self.btn_click(')'))
        self.btn_right_brack.grid(row=0, column=1)
        # 'memory clear' button. Wipes self.recall to an empty string
        self.btn_MC = tk.Button(bottom_frame, **btn_params, text="mc", command=self.memory_clear)
        self.btn_MC.grid(row=0, column=2)
        # adds current self.expression to self.recall string
        self.btn_M_plus = tk.Button(bottom_frame, **btn_params, text="m+", command=self.memory_add)
        self.btn_M_plus.grid(row=0, column=3)
        # adds current self.expression to self.recall string
        self.btn_M_subtract  = tk.Button(bottom_frame, **btn_params, text="m-", command=self.memory_subtract)
        self.btn_M_subtract .grid(row=0, column=4)
        # outputs what is in self.recall
        self.btn_MR = tk.Button(bottom_frame, **btn_params, text="mr", command=self.memory_recall)
        self.btn_MR.grid(row=0, column=5)
        # clears self.expression
        self.btn_clear = tk.Button(bottom_frame, **btn_params, text="AC", command=self.btn_clear_all)
        self.btn_clear.grid(row=0, column=6)
        # inputs a negative sign to the next entry
        self.btn_change_sign = tk.Button(bottom_frame, **btn_params, text="+/-", command=self.change_signs)
        self.btn_change_sign.grid(row=0, column=7)
        # outputs percentage of self.expression
        self.btn_percentage = tk.Button(bottom_frame, **btn_params, text="%", command=self.make_percentage)
        self.btn_percentage.grid(row=0, column=8)
        # division
        self.btn_div = tk.Button(bottom_frame, **opertors_params, text=u"\u00F7", command=lambda: self.btn_click('/'))
        self.btn_div.grid(row=0, column=9)

        #row 1
        self.btn_2_power_nd = tk.Button(bottom_frame, **btn_params, text=u"2\u207f\u1d48", command=lambda: self.btn_click('2**'))
        self.btn_2_power_nd.grid(row=1, column=0)
        # square function
        self.btn_sqr = tk.Button(bottom_frame, **btn_params, text=u"x\u00B2", command=lambda: self.btn_click('**2'))
        self.btn_sqr.grid(row=1, column=1)
        # cubes a value
        self.cube = tk.Button(bottom_frame, **btn_params, text=u"x\u00B3", command=lambda: self.btn_click('**3'))
        self.cube.grid(row=1, column=2)
        # to the power of function
        self.btn_power = tk.Button(bottom_frame, **btn_params, text="xʸ", command=lambda: self.btn_click('**'))
        self.btn_power.grid(row=1, column=3)
        # takes e to some exponent that you insert into the function
        self.btn_exp = tk.Button(bottom_frame, **btn_params, text="exp", command=lambda: self.btn_click('exp('))
        self.btn_exp.grid(row=1, column=4)
        self.btn_10_power = tk.Button(bottom_frame, **btn_params, text="10ⁿ", command=lambda: self.btn_click('10**'))
        self.btn_10_power.grid(row=1, column=5)
        # seven
        self.btn_7 = tk.Button(bottom_frame, **number_params, text="7", command=lambda: self.btn_click(7))
        self.btn_7.configure(activebackground="#4d4d4d")#, bg='#4d4d4d')
        self.btn_7.grid(row=1, column=6)
        # eight
        self.btn_8 = tk.Button(bottom_frame, **number_params, text="8", command=lambda: self.btn_click(8))
        self.btn_8.configure(activebackground="#4d4d4d")#, bg='#4d4d4d')
        self.btn_8.grid(row=1, column=7)
        # nine
        self.btn_9 = tk.Button(bottom_frame, **number_params, text="9", command=lambda: self.btn_click(9))
        self.btn_9.configure(activebackground="#4d4d4d")#, bg='#4d4d4d')
        self.btn_9.grid(row=1, column=8)
        # multiplication
        self.btn_mult = tk.Button(bottom_frame, **opertors_params, text="x", command=lambda: self.btn_click('*'))
        self.btn_mult.grid(row=1, column=9)

        # row 2
        self.btn_one_in_x =tk.Button(bottom_frame, **btn_params, text="1/x", command=self.one_in_x)
        self.btn_one_in_x.grid(row=2, column=0)
        # sqrt 2
        self.btn_sqrt_2 =tk.Button(bottom_frame, **btn_params, text=u"\u00B2\u221A"+"x", command=self.sqrt_2)
        self.btn_sqrt_2.grid(row=2, column=1)
        # sqrt 3
        self.btn_sqrt_3 =tk.Button(bottom_frame, **btn_params, text=u"\u00B3\u221A"+"x", command=self.sqrt_3)
        self.btn_sqrt_3.grid(row=2, column=2)
        # sqrt  y
        self.btn_sqrt_y =tk.Button(bottom_frame, **btn_params, text=u"\u02b8\u221A"+"x", command=lambda:self.btn_click('**1/' ))
        self.btn_sqrt_y.grid(row=2, column=3)
        # takes the natural log
        self.btn_ln = tk.Button(bottom_frame, **btn_params, text="ln", command=lambda: self.btn_click('log('))
        self.btn_ln.grid(row=2, column=4)
        #log10
        self.btn_log = tk.Button(bottom_frame, **btn_params, text=u"log\u2081\u2080", command=lambda: self.btn_click('log10('))
        self.btn_log.grid(row=2, column=5)
        # four
        self.btn_4 = tk.Button(bottom_frame, **number_params, text="4", command=lambda: self.btn_click(4))
        self.btn_4.configure(activebackground="#4d4d4d")
        self.btn_4.grid(row=2, column=6)
        # five
        self.btn_5 = tk.Button(bottom_frame, **number_params, text="5", command=lambda: self.btn_click(5))
        self.btn_5.configure(activebackground="#4d4d4d")
        self.btn_5.grid(row=2, column=7)
        # six
        self.btn_6 = tk.Button(bottom_frame, **number_params, text="6", command=lambda: self.btn_click(6))
        self.btn_6.configure(activebackground="#4d4d4d")
        self.btn_6.grid(row=2, column=8)
        # subtraction
        self.btnSub = tk.Button(bottom_frame, **opertors_params, text="-", command=lambda: self.btn_click('-'))
        self.btnSub.grid(row=2, column=9)

        # row 3
        # factorial function
        self.btn_fact = tk.Button(bottom_frame, **btn_params, text="x!", command=self.btn_factorial)#lambda: self.btn_click('factorial('))
        self.btn_fact.grid(row=3, column=0)
        # sin function that returns value from -1 to 1 by default
        self.btn_sin = tk.Button(bottom_frame, **btn_params, text="sin", command=lambda: self.btn_click('fsin('))
        self.btn_sin.grid(row=3, column=1)
        # cos function that returns value from -1 to 1 by default
        self.btn_cos = tk.Button(bottom_frame, **btn_params, text="cos", command=lambda: self.btn_click('fcos('))
        self.btn_cos.grid(row=3, column=2)
        # tan function
        self.btn_tan = tk.Button(bottom_frame, **btn_params, text="tan", command=lambda: self.btn_click('ftan('))
        self.btn_tan.grid(row=3, column=3)
        # e function
        self.btn_e = tk.Button(bottom_frame, **btn_params, text="e", command=self.btn_e)#lambda: self.btn_click('exp(1)'))
        self.btn_e.grid(row=3, column=4)
        # EE function
        self.btn_EE = tk.Button(bottom_frame, **btn_params, text="EE", command=lambda: self.btn_click('*10**'))
        self.btn_EE.grid(row=3, column=5)
        # one
        self.btn_1 = tk.Button(bottom_frame, **number_params, text="1", command=lambda: self.btn_click(1))
        self.btn_1.configure(activebackground="#4d4d4d")
        self.btn_1.grid(row=3, column=6)
        # two
        self.btn_2 = tk.Button(bottom_frame, **number_params, text="2", command=lambda: self.btn_click(2))
        self.btn_2.configure(activebackground="#4d4d4d")
        self.btn_2.grid(row=3, column=7)
        # three
        self.btn_3 = tk.Button(bottom_frame, **number_params, text="3", command=lambda: self.btn_click(3))
        self.btn_3.configure(activebackground="#4d4d4d")
        self.btn_3.grid(row=3, column=8)
        # addition
        self.btn_add = tk.Button(bottom_frame, **opertors_params, text="+", command=lambda: self.btn_click('+'))
        self.btn_add.grid(row=3, column=9)

        #row 4
        # changes trig function outputs to default back to radians
        self.btn_Rad = tk.Button(bottom_frame, **btn_params, text="Rad",
                                 command=self.convert_rad)
        self.btn_Rad.grid(row=4, column=0)
        # sin inverse function
        self.btn_sin_inverse = tk.Button(bottom_frame, **btn_params, text="sinh",
                                         command=lambda: self.btn_click('arcsin('))
        self.btn_sin_inverse.grid(row=4, column=1)
        # cos inverse function
        self.btn_cos_inverse = tk.Button(bottom_frame, **btn_params, text="cosh",
                                         command=lambda: self.btn_click('arccos('))
        self.btn_cos_inverse.grid(row=4, column=2)
        # tan inverse function
        self.btn_tan_inverse = tk.Button(bottom_frame, **btn_params, text="tanh",
                                         command=lambda: self.btn_click('arctan('))
        self.btn_tan_inverse.grid(row=4, column=3)
        # PI
        self.btn_pi = tk.Button(bottom_frame, **btn_params, text=u"\u03C0",
                                         command=lambda: self.btn_click('pi'))
        self.btn_pi.grid(row=4, column=4)
        # Rand
        self.Rand = tk.Button(bottom_frame, **btn_params, text="Rand",
                                         command=self.btn_rand)
        self.Rand.grid(row=4, column=5)
        # zero
        self.btn_0 = tk.Button(bottom_frame, **number_params, text="0", command=lambda: self.btn_click(0))
        self.btn_0.configure(  width=7,highlightbackground='#696969')
        self.btn_0.grid(row=4, column=6, columnspan=2)
        # decimal to convert to float
        self.btn_dec = tk.Button(bottom_frame, **number_params, text=".", command=lambda: self.btn_click('.'))
        self.btn_dec.grid(row=4, column=8)
        # equals button
        self.btn_eq = tk.Button(bottom_frame, **opertors_params, text="=", command=self.btn_equal)
        self.btn_eq.configure(activebackground='#ff9980')
        self.btn_eq.grid(row=4, column=9)
    # functions
    # allows button you click to be put into self.expression

    # sqrt_2 function
    def sqrt_2(self):
        self.expression=str(float(self.expression)**(1/2))
        self.text_input.set(self.expression)

    # sqrt_3 function
    def sqrt_3(self):
        self.expression=str(float(self.expression)**(1/3))
        self.text_input.set(self.expression)

    def btn_click(self, expression_val):
        if len(self.expression) >= 23:
            self.expression = self.expression
            self.text_input.set(self.expression)
        else:
            self.expression = self.expression + str(expression_val)
            self.text_input.set(self.expression)

    # clears memory_recall

    def memory_clear(self):
        self.recall = ""

    # adds whatever is on the screen to self.memory_recall

    def memory_add(self):
        self.recall = self.recall + '+' + self.expression

    # substract whatever is on the screen to self.memory_recall
    def memory_subtract(self):
        self.recall = self.recall + '-' + self.expression

    # uses whatever is stored in memory_recall

    def memory_recall(self):
        if self.expression == "":
            self.text_input.set('0' + self.expression + self.recall)
        else:
            self.text_input.set(self.expression + self.recall)

    # clears self.expression

    def btn_clear_all(self):
        global convert_constant
        global inverse_convert_constant
        convert_constant = pi / 180
        inverse_convert_constant = 180 / pi
        self.btn_Rad["foreground"] = 'white'
        self.expression = ""
        self.text_input.set("0")


    # adds in a negative sign

    def change_signs(self):
        self.expression =str(-float(self.expression))
        self.text_input.set(self.expression)
   # percentage of self.expression
    def make_percentage(self):
        self.text_input.set(self.expression+'%')
        self.expression =str( float(self.expression)/100)


    # btn_e
    def btn_e(self):
        self.text_input.set(self.expression+'e')
        self.expression=str(float(self.expression)*exp(1))
    # btn factorial
    def btn_factorial(self):
        self.expression = str(factorial(int(self.expression)))
        self.text_input.set(self.expression)
    # one in x function
    def one_in_x(self):
        self.expression =str(1/float(self.expression))
        self.text_input.set(self.expression)
    # sqrt_2 function
    def sqrt_2(self):
        self.expression=str(float(self.expression)**(1/2))
        self.text_input.set(self.expression)

    # sqrt_3 function
    def sqrt_3(self):
        self.expression=str(float(self.expression)**(1/3))
        self.text_input.set(self.expression)
    def convert_rad(self):
        global convert_constant
        global inverse_convert_constant
        convert_constant = 1
        inverse_convert_constant = 1
        self.btn_Rad["foreground"] = 'orange'
        #self.btn_Deg["foreground"] = 'white'


        #RAND(x) returns a computer-generated random number:
        #(a) when x < 1 then the result is a number between 0 and 1, or.
        #(b) when x > 1 then the result is a whole number between 1 and x (inclusive)
    def btn_rand(self):
        if int(self.expression) < 1 :
            self.expression =str(randint(0,1))#(int(self.expression))

        else:
            self.expression=str(randint(1,int(self.expression)))
        self.text_input.set(self.expression)
    # converts self.expression into a mathematical expression and evaluates it

    def btn_equal(self):
        self.sum_up = str(eval(self.expression))
        self.text_input.set(self.sum_up)
        self.expression = self.sum_up
    # switch to simple view



def switch():
    root.destroy()
    os.system('python simple.py')

root = tk.Tk()
b = Calculator(root)
root.resizable(0,0)
root.title(' ')
root.configure(background='#303030')
root.mainloop()
