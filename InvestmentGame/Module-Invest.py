from random import choice

def unique_compname(companynames):
    companynames_copy = companynames.copy()
    compn1 = choice(companynames_copy)
    companynames_copy.remove(compn1)
    compn2 = choice(companynames_copy)
    companynames_copy.remove(compn2)
    compn3 = choice(companynames_copy)
    companynames_copy.remove(compn3)
    compn4 = choice(companynames_copy)
    companynames_copy.remove(compn4)

    return compn1, compn2, compn3, compn4

import random

def luck(investor):
    lucky = ["10%", "20%", "30%", "50%", "100%", "-10%", "-20%", "-30%", "-50%", "-100%"]
    
    lucky_percentage = random.choice(lucky)

    if lucky_percentage == "10%":
        investor *= 1.1
        print("The company saw some steady growth today. Your investment increased by 10%!")
    elif lucky_percentage == "20%":
        investor *= 1.2
        print("The company made some decent profit today. Your investment grew by 20%!")
    elif lucky_percentage == "30%":
        investor *= 1.3
        print("The company had a good day with solid growth. Your investment increased by 30%!")
    elif lucky_percentage == "50%":
        investor *= 1.5
        print("The company had an excellent day! Your investment soared by 50%!")
    elif lucky_percentage == "100%":
        investor *= 2.0
        print("The company was bought out by an extremely wealthy investor! Your investment has doubled!")
    elif lucky_percentage == "-10%":
        investor *= 0.9
        print("The company faced some minor setbacks today. Your investment dropped by 10%.")
    elif lucky_percentage == "-20%":
        investor *= 0.8
        print("The company had a rough day. Your investment lost 20%.")
    elif lucky_percentage == "-30%":
        investor *= 0.7
        print("The company suffered some serious losses. Your investment dropped by 30%.")
    elif lucky_percentage == "-50%":
        investor *= 0.5
        print("The company experienced major losses. Your investment is down by 50%.")
    elif lucky_percentage == "-100%":
        investor = 0
        print("Disaster struck! The company went bankrupt, and your investment is completely wiped out.")

    return investor
