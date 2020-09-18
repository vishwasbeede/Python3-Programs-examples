#Used random module to select a number from your input and this will match to yours input
import random
list_int = []
char_sep='-'
for i in range(0,6):
    list_int.append(i)
print ("{:<30} {} ".format(" ",(char_sep*100)))
print ("\n\n{:<30} Enter charecters for input to stop execution\n\n".format(" "))
print ("{:<30} Enter numbers in range of 1 to 5 \n\n".format(" "))
print ("{:<30} {} \n\n".format(" ",(char_sep*100)))
while True:
    # user_input = input("Would you like to play? (Y/n):")
    user_number = random.choice(list_int)
    # if user_input == "n":
    #     break

    try:
        user_input_guess=int(input("Enter the number you guess: "))
    except:
        print ("{:<30}Enter only numbers as input charecters".format(""))
        print ("{:<30}Stopping execution".format(""))
        exit(1)

    if user_number == user_input_guess:
        print ("{:<30}Congratulations guessed number correctly!!!!".format(" "))
    else:
        print ("{:<30}Sorry!!, you need to guess {}".format(" ",user_number))
