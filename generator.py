import random
import array

def generate_password():
    MAX_LEN = 14
    
    #Characters that will make up the password
    DIGITS = ['0', '1', '2', '3', '4']
    LOWCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e']
    UPPCASE_CHARACTERS = ['Q', 'W', 'E', 'R', 'T']
    SYMBOLS = ['!', '@', '£', '$', '%']

    #The formation of how the chracters will be combined
    COMBINED_LIST = DIGITS + UPPCASE_CHARACTERS + SYMBOLS + LOWCASE_CHARACTERS

    #Randomly selecting a character from the lists above
    rand_digit = random.choice(DIGITS)
    rand_lower = random.choice(LOWCASE_CHARACTERS)
    rand_upper = random.choice(UPPCASE_CHARACTERS)
    rand_symbol = random.choice(SYMBOLS)

    #The formation of how the random characters will be combined
    temp_pass = rand_digit + rand_lower + rand_upper + rand_symbol

    #For loop to generate the amount of characters set = MAX_LEN
    for i in range(MAX_LEN):
        temp_pass = temp_pass + random.choice(COMBINED_LIST)

        #Convert list into an array
        temp_pass_list = array.array('u', temp_pass)
        random.shuffle(temp_pass_list)

    #Password to empty string
    password = ""
    for i in temp_pass_list:
        password = password + i

    return(password)


if __name__ == "__main__":
        print(generate_password())