'hw_2.2'
# 56873 = 5 * 10000 + 6 * 1000 + 8 * 100 + 7 * 10 + 3 * 1
reverse_number = 0
number = int(input('Enter 5-digit number: '))
div10000, mod10000 = divmod(number, 10000)
reverse_number = div10000 * 1
div1000, mod1000 = divmod(mod10000, 1000)
reverse_number += div1000 * 10
div100, mod100 = divmod(mod1000, 100)
reverse_number += div100 * 100
div10, mod10 = divmod(mod100, 10)
reverse_number += div10 * 1000
reverse_number += mod10 * 10000
print(f'{number} -> {reverse_number}')