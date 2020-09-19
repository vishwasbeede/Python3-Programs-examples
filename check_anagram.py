# Program used to check two strings is anagram or not.
# An anagram is a word or phrase formed by rearranging the letters of a different word or phrase
#typically using all the original letters exactly once.
#the word anagram can be rearranged into nag a ram, or the word binary into brainy or the word adobe into abode.

str1=input("Enter First string:")
str2=input("Enter Second string:")

# str1="VishwasBeede"
# str2="BeedeVishwas"
#Str2="BedeVishwas"

def anagram(str1,str2):
    if (len(str1)!=len(str2)):
        return False
    elif (''.join(sorted(str1)) == ''.join(sorted(str2))):
        return True
    else:
        return False

output=anagram(str1,str2)
if output:
    print ("String is anagram")
else:
    print ("String is not an anagram")
