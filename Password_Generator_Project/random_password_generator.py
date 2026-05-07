import random #used for random selection of characters , to ensure unpredicatbale password
import string #provide predefines character set of all characters i.e letters(a-zA-Z), digit(0-9), punctuations (all special char)

#taking no. and special-char bydefault true, but if it's given false, it'll be overridden
def genarate_password(min_length, numbers=True, special_char = True): 
    letters = string.ascii_letters              #store only char from a-zA-Z
    digits = string.digits                      #stores only numeral values

    #special = string.punctuation                #stores all special char only 

    #safer special characters (real-world style)
    special = "!@#$%^*()-_=+?"

    characters = letters                        #initially copied letters, as letters are always included in pass
    
    if numbers :                                #means password must contain atleast single digit
        characters += digits
    if special_char:                            #i.e pass must contain atleast one special char
        characters += special

    #by default, taking all flag's false, to track accurately

    pwd = ""                                    #password generated will be stored here
    has_numbers = False                         #track whether the pass satisfies condition for digit & special-cjhar
    has_special = False
    meets_criteria = False                      #track all conditions given , met for password generation or not

    while not meets_criteria or len(pwd) <= min_length:     #only false when both condition gets true i.e criteria met & pass of min len is generated
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:                   #if digits found, numbers in password condition gets true
            has_numbers = True 
        elif new_char in special:
            has_special = True

        meets_criteria = True

        if numbers:
            meets_criteria = has_numbers         #if digit condition satisfied, meet-criteria will be true else if digit required but not found currently, gets false
        if special_char:
            meets_criteria = meets_criteria and has_special

    return pwd

min_length = (int)(input("Enter the minimum-length password you need to set :"))
has_number = input("Do you want to include numbers in your password (y/n)?").lower()=="y"    #convert the input into boolean & ensure case-sensitive comparison
has_special = input("Dp you want to include special-characters in your password (y/n)?").lower()=="y"

pwd = genarate_password(min_length, has_number, has_special)
print("Generated Password :" , pwd)

        





