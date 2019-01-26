import string #imports string module for all characters used (letters, punctuation, and numbers)
from random import * #imports random module to randomize the character input
import pyperclip #used to copy password to clipboard

#Booleans for each character type while loop
c1 = False
c2 = False
c3 = False

#Booleans for each character type(kind of like an on/off switch)
l = False
n = False
s = False

empty = True

characters = "" #string that will eventually be added to and printed at the end

print ("\nWELCOME TO YOUR PASSWORD GENERATOR\nEnter your preferred length of password to begin")

#empty will always be true unless at least one of the choices is choosen. If none are chosen, it will be looped back to the beginning.
while empty == True:
    length = int(input("Length of password: "))
   
    while c1 == False: #loops unless 'y' or 'n' is entered
        print ("\nDo you want letters?")
        letters = input("'y' or 'n': ")
        if letters == "y":
            l = True #turns the character switch on
            c1 = True #ends small loop
            empty = False #shows that the 'characters' variable won't be empty
        if letters == "n":
            c1 = True #ends small loop
            
    while c2 == False: #loops unless 'y' or 'n' is entered
        print ("\nDo you want symbols?")
        punctuation  = input("'y' or 'n': ")
        if punctuation == "y":
            s = True #turns the character switch on
            c2 = True #ends small loop
            empty = False #shows that the 'characters' variable won't be empty
        if punctuation == "n":
            c2 = True #ends small loop
            
    while c3 == False: #loops unless 'y' or 'n' is entered
        print ("\nDo you want numbers?")
        numbers  = input("'y' or 'n': ")
        if numbers == "y":
            n = True #turns the character switch on
            c3 = True  #ends small loop
            empty = False #shows that the 'characters' variable won't be empty
        if numbers == "n":
            c3 = True #ends small loop
    
    if empty == True:#if no choices are choosen, it loops it back to the beginning
        print ("\nYou have to have some text in your password. -_- Try again.")
        c1 = False
        c2 = False
        c3 = False

#adds letters to 'characters'
if l == True:
    characters = characters + string.ascii_letters
#adds punctuation to 'characters'
if s == True:
    characters = characters + string.punctuation
#adds numbers to 'characters'
if n == True:
    characters = characters + string.digits

password = "".join(choice(characters) for x in range(length)) #puts together random series of characters set by the number put in for 'input'

print ("\nPassword: " + password)#prints completed password
pyperclip.copy(password)#copies password to clipboard
print ('\nPassword has been copied to clipboard')

