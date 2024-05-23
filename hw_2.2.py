def flip_input(user_input: str):
    if len(user_input) < 5 or len(user_input) > 5:
        print('Please, enter 5-digit number')
    else:
        return user_input[::-1]


my_input = input('Enter: ')
print(flip_input(my_input))