#OWL SAY PYTHON SCRIPT:

import sys

def owl_say(str_value):
    
    file_name=open("owl_say.log",'a')
    sys.stdout = file_name
    _blank=" "*50
    print("{}            {}".format(_blank,_strvalue))
    
    print("{}          /".format(_blank))
    print("{}         / ".format(_blank))
    print("{}   ^  ^    ".format(_blank))
    print("             ".format(_blank))
    print("{} ( @  @ )  ".format(_blank))
    print("{}    __     ".format(_blank))
    print("{}/        \\".format(_blank))
    print("{}/        \\".format(_blank))
    print("{}/        \\".format(_blank))
    print("{}\   __   / ".format(_blank))
    print("{}  \/  \/   ".format(_blank))
    print('_'*170)
    sys.stdout = sys.__stdout__
    
    
    
rep=int(input("Enter number of inputs:\n"))

for i in range(0,rep):
    
    _strvalue=str(input("Enter word to say:"))
    len_val=len(_strvalue)
    
    print('_'*170)
    
    
    if len_val== 0:
        print ("Stoppping script")
        exit(0)
    
    elif len(_strvalue) >175:
        print ("\"Owl can not say anything\"")
        _strvalue="..........."
        owl_say(_strvalue)
        exit(1)
    
    else:
        owl_say(_strvalue)

    
print("Output are logged to file owl_say.log")
value_print=open("owl_say.log",'r')
print (value_print.read())
value_print.close()