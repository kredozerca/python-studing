import random
import sys


lower_case = "abcdefghijklmnoprqstuwyxz"
upper_case = lower_case.upper()
symbols = '''@#$_&-+()/*"':;!"'''
numbers = "1234567890"
all_signs = str(lower_case + upper_case + symbols + numbers)

def password_gen():
 password = []
 password_lenght = int(input("Jak długie ma być hasło?"))
 for _ in range(0,password_lenght):
       password_sign = random.choice(all_signs)
       password.append(password_sign)
 print("".join(password))
   
password_gen()




while True:
    next_try = input("Wygenerować nowe hasło? Y/N")
    next_try_upper = next_try.upper()
    if next_try_upper == "Y":
 	    password_gen()
    elif next_try_upper == "N":
        sys.exit(0)
    else:
        print("Symbol niepoprawny")