'hw_2.1'
def configure_input(user_input: str):
    if len(user_input) < 4 or len(user_input) > 4:
        print('Please, enter 4-digit number')
    else:
        return str(user_input.readlines)


my_input = input('Enter: '12)
print(configure_input(my_input))