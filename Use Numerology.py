#Now lets use our Numerology Python class so we don't have to spheal out a bunch of code

from Numerology import Numerology

def main():
    name = input("Enter your name: ")
    dob= input("Enter your Date of birth (must be in mm-dd-yyyy format): ")
    while len(dob) !=10 or dob[2] != '-' or dob[5] != '-':
        dob= input("Invalid format, please enter again in mm-dd-yyyy format: ")

    numerology = Numerology(name,dob)
    print("Name:", numerology.getName())
    print("Birthdate:", numerology.getBirthdate())
    print("Life Path Number:", numerology.getLifePath())
    print("Birthday Number", numerology.getBirthday())
    print("Attitude Number", numerology.getAttitude())
    print("Soul Number:", numerology.getSoul())
    print("Personality Number:", numerology.getPersonality())
    print("Power Name Number:", numerology.getPowerName())



if __name__ == "__main__":
    main()





#Summary questions

#Name: Nicholas Diaz

#Assignment: Numerology Classes

#1.What did I struggle with?
    
#I struggled the most with the math as it was a bit hard at first to set up but I managed to find a way to get the math right and put it in a function to save time and space on my code
#Also I realized that formatting is my biggest problem out of all in Python.
    
#2.How could I use classes to help with a previous assignment
    
#In our previous assignments I feel we could of used a class for the Planetary Weights assignment and set up a class that does all the math.

#3.What are two things I learned doing this assignment?

#1. Classes come in handy when dealing with multiple lines of code or redundance.

#2. I learned how classes help when coding python and how I might have done my love live program differently if I knew how to do classes at the time.
