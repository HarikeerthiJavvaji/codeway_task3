import random

uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase = "abcdefghijklmnopqrstuvwxyz"
digits = '1234567890'
symbols = "!@#$$%^&*()?><.,{}/\\;'+-=_ "

upper,lower,nums,syms = True,True,True,True

all = ""

if upper:
    all+=uppercase
if lower:
    all+=lowercase
if nums:
    all+=digits
if syms:
    all+=symbols

length = int(input('Enter length of password:'))


password = "".join(random.sample(all,length))
print(password)
