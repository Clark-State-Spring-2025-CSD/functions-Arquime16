#Write a function that takes two parameters: a prompt message and an error message.
#The function will prompt the user with the passed in prompt to enter an integer
#If the text entered cannot be cast to an int, display the error message.
#The function will continue to prompt the user to enter an integer until a proper integer is entered.
#The most direct way of doing this would be using a try block, which has not been covered yet. You will need to research this.
#Write supporting code to call the function, and then display the number that was entered.



def myFunctionMandE(message, error):
    user_num = None
    while user_num == None:
        user_input = input(message)
        try:
            user_num = int(user_input)
        except ValueError:
            print(error)
    print(user_num)


myFunctionMandE('Enter an integer: ', 'That is not a valid integer!')