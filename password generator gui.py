
from tkinter import * #GUI
import string #imports string module for all characters used (letters, punctuation, and numbers)
from random import * #imports random module to randomize the character input


root = Tk() #root window

#sets the root window to fullscreen
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))

header = StringVar() #creates a string variable
header.set("WELCOME TO YOUR PASSWORD GENERATOR") #sets the string value

#booleans for each character type while loop
letter = False
symbol = False
number = False

#booleans for each character type(kind of like an on/off switch)
l = False
n = False
s = False

empty = True



#function for start button thant bring up the new page and all of it's components and their functions
def start():
    print ("Start")
        
    def generate():
        print ("Generate")
        length = (length_slider.get())
        print (length_slider.get())#gets number from slider
        choice_1.pack_forget()
        length_slider.pack_forget()
        choice_2.pack_forget()
        letter1.pack_forget()
        letter2.pack_forget()
        choice_3.pack_forget()
        symbol1.pack_forget()
        symbol2.pack_forget()
        choice_4.pack_forget()
        number1.pack_forget()
        number2.pack_forget()
        generate_button.pack_forget()

        characters = "" #string that will eventually be added to and printed at the end

        #adds letters to 'characters'
        if l == True:
            characters = characters + string.ascii_letters
        #adds punctuation to 'characters'
        if s == True:
            characters = characters + string.punctuation
        #adds numbers to 'characters'
        if n == True:
            characters = characters + string.digits

        password = "".join(choice(characters) for x in range(length)) #puts together
        
        header.set("Your new password" + password)
    
    start_button.pack_forget() #removes start button
    header.set("Choose your settings") #changes welcome_label
    
    choice_1 = Label(root,text="How long would you like your password?", fg="black", font=("Helvetica", 25))
    choice_1.pack()
    length_slider = Scale(root, from_=0, to=50, orient=HORIZONTAL, length=300)
    length_slider.pack()

    
    choice_2 = Label(root,text="Would you like letters in your password?", fg="black", font=("Helvetica", 25))
    choice_2.pack()
    letter1 = Button(root, text="Yes", command=yes_letter, font=("Helvetica", 20))
    letter1.pack()
    letter2 = Button(root, text="No", command=no_letter, font=("Helvetica", 20))
    letter2.pack()
    
    choice_3 = Label(root,text="Would you like symbols in your password?", fg="black", font=("Helvetica", 25))
    choice_3.pack()
    symbol1 = Button(root, text="Yes", command=yes_symbol, font=("Helvetica", 20))
    symbol1.pack()
    symbol2 = Button(root, text="No", command=no_symbol, font=("Helvetica", 20))
    symbol2.pack()
    
    choice_4 = Label(root,text="Would you like numbers in your password?", fg="black", font=("Helvetica", 25))
    choice_4.pack()
    number1 = Button(root, text="Yes", command=yes_number, font=("Helvetica", 20))
    number1.pack()
    number2 = Button(root, text="No", command=no_number, font=("Helvetica", 20))
    number2.pack()
    
    generate_button = Button(root, text="Generate", command=generate, font=("Helvetica", 25))
    generate_button.pack()
    

def yes_letter():
    print ("yes")
    letter = True
    empty = False
    
def no_letter():
    print ("no")
        
def yes_symbol():
    print ("yes")
    symbol = True
    empty = False
    
def no_symbol():
    print ("no")
    
def yes_number():
    print ("yes")
    number = True
    empty = False
    
def no_number():
    print ("no")
       

welcome_label = Label(root,textvariable=header, fg="black", font=("Helvetica", 40)) #welcome label
welcome_label.pack() #packs the label into the GUI

start_button = Button(root, text="Start", font=("Helvetica", 40), command=start) #creates srtart button
start_button.pack() #packs button

root.mainloop() #creates window and keeps it open
