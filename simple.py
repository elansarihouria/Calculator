import tkinter
import os
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
menu_params={

    'fg': 'orange',
    'bg': '#303030',
    'font': ('arial', 12),
    'bd':0

}

# Calculation
def calculate():
    # Calculation
    # equ.get() gets the equ content at this time
    # eval computing
    result = eval(equ.get())
    # Splicing
    equ.set(str(result))


#function for +/- button
def bare():
    result=-float((equ.get()))
    equ.set(result)#equ.get() + "=\n" + str(result))

# Put our numbers in the text box
def show(buttonString):
    # Get content
    content = equ.get()
    # Judge if the content is 0, it is equivalent to no calculation, so null string splicing, or 0
    # If the content is 10, the content is 10, and then the numbers we press are spliced
    if content == "0":
        content = ""
    equ.set(content + buttonString)


# Clear, set to 0
def clear():
    equ.set("0")

# switch to scientific view
def switch():
    root.destroy()
    os.system('python scientific.py')

# Abdication
def backSpace():
    # Delete previous character
    equ.set(str(equ.get()[:-1]))

# porcentage of a number
def btn_percentage():
    content=equ.get()
    equ.set(str(float(content)/100))
# main program
root = tkinter.Tk()
# Set program title
root.title(" ")
text = tkinter.Text(root)
menubar=tkinter.Menu(root, **menu_params)

menubar.add_command(label="scientific",command=switch)
#menubar.pack(side=tkinter.TOP)
root.config(menu=menubar)
#tkinter.Button(text="+/-",command=switch)
#myFont=Font(family="Times", size=10, weight=tkFont.BOLD)
#myFont = Font(family="Times New Roman", size=14)
# The frame can be dragged, 0,0 means it cannot be dragged
root.resizable(0, 0)
root.configure(background='#303030')
top_frame = tkinter.Frame(root, width=42, height=5, relief='flat', bg='#303030')
top_frame.pack(side=tkinter.TOP)
bottom_frame = tkinter.Frame(root, width=2, height= 5,relief='flat', bg='#666666')
bottom_frame.pack(side=tkinter.BOTTOM)
#self.text_input.set("0")
#root.background("black")
# equ is the number of display area
equ = tkinter.StringVar()
# The default is 0.
equ.set("0")
label = tkinter.Entry(top_frame,font=('arial',34),relief='flat',
bg="#303030",fg='white', justify='right',width=14, bd=2, textvariable=equ,highlightbackground ='#303030')
label.pack()
# Button for row1

# Clear display area button AC
# Text text on button
# bg background color
# command execute the clear function when the button is clicked
buttonClear = tkinter.Button(bottom_frame,**btn_params, text="AC",command=clear)
buttonClear.grid(row=1, column=0)

# Exit button
buttonBack = tkinter.Button(bottom_frame,**btn_params,text="+/-",command=bare) #lambda:show("-"))#backSpace)
buttonBack.grid(row=1, column=1)

# Remaining button
# You need to use the lambda function to pass parameters
buttonYu = tkinter.Button(bottom_frame,**btn_params, text="%",command=btn_percentage)
buttonYu.grid(row=1, column=2)

# Except button
buttonDivision = tkinter.Button(bottom_frame,**opertors_params, text=u"\u00F7",command=lambda: show("/"))
buttonDivision.grid(row=1, column=3)

# Button for row2

# Number 7
button7 = tkinter.Button(bottom_frame,**number_params, text="7", command=lambda: show("7"))
button7.grid(row=2, column=0)

# Number 8
button8 = tkinter.Button(bottom_frame,**number_params,text="8",command=lambda: show("8"))
button8.grid(row=2, column=1)

# Number 9
button9 = tkinter.Button(bottom_frame,**number_params, text="9", command=lambda: show("9"))
button9.grid(row=2, column=2)

# Multiplication button
buttonMultiplication = tkinter.Button(bottom_frame,**opertors_params,text="x",command=lambda: show("*"))
buttonMultiplication.grid(row=2, column=3)

# Button for row3

# Number 4
button4 = tkinter.Button(bottom_frame,**number_params, text="4", command=lambda: show("4"))
button4.grid(row=3, column=0)

# Number 5
button5 = tkinter.Button(bottom_frame,**number_params, text="5", command=lambda: show("5"))
button5.grid(row=3, column=1)

# Number 6
button6 = tkinter.Button(bottom_frame,**number_params, text="6", command=lambda: show("6"))
button6.grid(row=3, column=2)

# Subtraction button
buttonSubtraction = tkinter.Button(bottom_frame,**opertors_params, text="-",command=lambda: show("-"))
buttonSubtraction.grid(row=3, column=3)

# Button for row4

# Number 1
button1 = tkinter.Button(bottom_frame,**number_params,text="1",command=lambda: show("1"))
button1.grid(row=4, column=0)

# Number 2
button2 = tkinter.Button(bottom_frame,**number_params, text="2",command=lambda: show("2"))
button2.grid(row=4, column=1)

# Number 3
button3 = tkinter.Button(bottom_frame,**number_params,text="3",command=lambda: show("3"))
button3.grid(row=4, column=2)

# Add button
buttonAdd = tkinter.Button(bottom_frame,**opertors_params, text="+", command=lambda: show("+"))
buttonAdd.grid(row=4, column=3)

# Button for row5
# Number 0
button0 = tkinter.Button(bottom_frame,**number_params, text="0", command=lambda: show("0"))
#button0.grid(row=5, column=0)
button0.grid(row=5, column=0, columnspan=2)
button0.configure( width=7,highlightbackground='#696969')
# Decimal button
buttonPoint = tkinter.Button(bottom_frame,**number_params, text=".", command=lambda: show("."))
buttonPoint.grid(row=5, column=2)


# Be equal to
buttonEqual = tkinter.Button(bottom_frame,**opertors_params,text="=",command=calculate)
buttonEqual.grid(row=5, column=3)#, columnspan=2)

# Program cycle
root.mainloop()
