from random import randint

g_success=True
g_count=0
while g_success:
    g_rand=randint(0,10)
    print("{} is to be guessed".format(bin(int(g_rand))))
    try :
        g_num=int(input("Guess a number"))
        g_count+=1
    except ValueError:
        print("Enter valid guess number\n")
        break

    if (g_num==g_rand):
        print("Guess is correct!!!!")
        print("You guessed in %s attempt"%g_count)
        g_con=input("Do you want to play Again!!![Y]")
        g_count=0
        if(g_con.upper() == "Y"):
            continue;
        else:
            print("Thanks for playing game!!!!")
            break
    elif g_num < g_rand:
        print("Guess is Low!!")
    else:
        print("Guess is High!!")
