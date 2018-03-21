import string #imports string module for all characters used (letters, punctuation, and numbers)
from random import * #imports random module to randomize the character input
length = int(raw_input("Length of password: "))
characters = string.ascii_letters + string.punctuation + string.digits
password =  "".join(choice(characters) for x in range(randint(length, length))) #puts together random series of characters set by the number put in for raw_input
print password #prints completed password