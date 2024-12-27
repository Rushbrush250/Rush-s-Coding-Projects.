from os import urandom
import secrets as sec
import token
import random as rd
from faker import Faker


#Creating numbers for the password
def password_part1():
    random_num1 = urandom(1)
    random_num1 = int.from_bytes(random_num1, byteorder='big')


    random_num2 = sec.randbits(8)

    
    random_dict = {}
    unique_num = set()
    three_digits = ""
    for i in range(9):
        random_dict[i] = rd.randint(0, 9)
    while True:
        choosing_num = sec.choice(list(random_dict.keys()))
        if choosing_num not in unique_num:
            unique_num.add(choosing_num)
            three_digits += str(random_dict[choosing_num])
            if len(unique_num) == 3:
                break
    random_num3 = int(three_digits)

#using string concentration to my advantage
    full_num = str(random_num1) + str(random_num2) + str(random_num3)
    return full_num


def password_part2():
    alphabet_string = "abcdefghijklmnopqrstuvwxyz"#♫Now I know my ABC's next time won't you sing with me?♫
    alphabet_list = list(alphabet_string)
    alphabet_set = set()
    three_letters = ""
    while True:
        choosing_letter = sec.choice(alphabet_list) #choosing three digits from the alphabet list
        if choosing_letter not in alphabet_set:
            alphabet_set.add(choosing_letter)
            three_letters += choosing_letter
            if len(alphabet_set) == 3:
                break
    random_letters1 = three_letters


#choosing three digits from a generated word to go towards the password
    fake = Faker()
    while True:
      fake.seed_instance(sec.randbelow(1000001)) #making the pseudo randomness true randomness
      word = fake.word()
      if len(word)>3:
        break

    random_letters2 = ""
    letters_of_word = list(word)
    while True:
        choosing_word_letter = sec.choice(letters_of_word)
        letters_of_word.remove(choosing_word_letter)
        if len(letters_of_word) == 3:
            rd.seed(sec.randbelow(1000001))
            rd.shuffle(letters_of_word)
            for i in letters_of_word:
                random_letters2 += i
            break


    loop = 0
    random_letters3 = ""
    while True:
        character = sec.randbelow(27)#ASCII code for the alphabet, only uppercase
        if character == 0:
            continue
        else:
           character =  chr(character + 64)
           random_letters3 += character
           loop += 1
           if loop == 3:
            break


    full_letters = random_letters1 + random_letters2 + random_letters3
    return full_letters

def final_password(pass1, pass2):
    order = sec.choice([str(pass1) + str(pass2), str(pass2) + str(pass1)])
    list_of_contents = list(order)
    rd.seed(sec.randbelow(1000001))#making the pseudo randomness true randomness
    rd.shuffle(list_of_contents)
    finishing_final_password = ""
    special_characters = [
    '!', '"', '#', '```, '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
    ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '{', '|', '}', '~',
    '+', '-', '*', '/', '=', '<', '>', '±', '÷', '×', '√', '≈', '≠', '≤', '≥',
    '```, '€', '£', '¥', '₹'] #special characters for the front and back of the password
    special_characters_saved = {}
    for i in range(3):
        special_characters_saved[f"SC{i}"] = sec.choice(special_characters) #saving the special characters
    length_of_contents = len(list_of_contents)
    start_of_contents = 0
    middle_of_contents = round(int(length_of_contents / 2))
    end_of_contents = length_of_contents - 1
    order_of_number_found = 0
    for i in range(length_of_contents): #alternating between adding the alphabet with numbers and adding the special characters for better password security
        if i == middle_of_contents or i == start_of_contents or i == end_of_contents:
            if order_of_number_found == 0:
                finishing_final_password += special_characters_saved["SC0"]
                order_of_number_found += 1
            elif order_of_number_found  == 2:
                finishing_final_password += special_characters_saved["SC1"]
                order_of_number_found += 3
            elif order_of_number_found == 4:
                finishing_final_password += special_characters_saved["SC2"]
                break
            else:
                if order_of_number_found == 1:
                    for i in range(middle_of_contents):
                        finishing_final_password += list_of_contents[i]
                    order_of_number_found += 1
                if order_of_number_found == 3:
                    for i in range(middle_of_contents, length_of_contents):
                        finishing_final_password += list_of_contents[i]
                        order_of_number_found += 1

    
    print(f"Your generated password: {finishing_final_password}")



#generating the password
final_password(password_part1(), password_part2())
