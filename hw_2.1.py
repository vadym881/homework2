'hw_2.1'
number = int(input('Enter 4-digit number: '))

div1000, mod1000 = divmod(number, 1000)
print(div1000)
div100, mod100 = divmod(mod1000, 100)
print(div100)
div10, mod10 = divmod(mod100, 10)
print(div10)
print(mod10)