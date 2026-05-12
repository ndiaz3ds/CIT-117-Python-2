#Password Validator by Nicholas Diaz
def main():
    #Ask user to type in their full name

    sName=input("Enter your full name: ")



    #Split their name into initials
    sNameParts = sName.split(" ")
    sInitials = sNameParts[0][0] + sNameParts[1][0]



    #Ask the user for their password and loop it until they print a valid password
    while True:
        bValidation = True
        sPassword = input("Enter a brand new password: ")

        #Check for length

        if len(sPassword)<8  or len(sPassword)>12:
            print("Password must be between 8 and 12 characters")
            bValidation = False

        # Don't you DARE make it Password, or Else!
        if sPassword.lower().startswith("pass"):
            print("Password can't start with Pass.")
            bValidation = False

        #Check for at LEAST 1 capital letter,  1 lowercase letter,a special character, and a number
        sHasUpper = False
        sHasLower = False
        sHasSpec  = False
        sHasNumb  = False

        sSpeChan= "!@#$%^"
        sNumb= "1234567890"
        for c in sPassword:
            if c.isupper():
                sHasUpper=True
            elif c.islower():
                sHasLower=True
            elif c in sSpeChan:
                sHasSpec=True
            elif c in sNumb:
                sHasNumb=True


        bValidation = True

        if not sHasUpper:
            print("Password must contain at least 1 uppercase letter.")
            bValidation = False

        if not sHasLower:
            print("Password must contain at least 1 lowercase letter")
            bValidation = False

        if not sHasSpec:
            print("Password must contain at least 1 of these special characters:(! @ # $ % ^)")
            bValidation = False

        if not sHasNumb:
            print("Password must contain at least 1 number.")
            bValidation = False



        #ARR matey, there shall be no initials for ye password landlubber
        if sInitials.lower() in sPassword.lower():
            print("Password must not contain user initials.")
            bValidation = False

        #No character shall appear more than once (Better use a dictionary here if you ask me)

        sPasswordLower= sPassword.lower()
        dWordcount={}


        #Count all your occurrences
        for c in sPasswordLower:
            if c in dWordcount:
                dWordcount[c]+=1
            else:
                dWordcount[c]=1

         #Check for "Dupes" as the young folks call them
        bDupesFound=False
        for key in dWordcount:
            if dWordcount[key]>1:
                if not bDupesFound:
                 print("These characters appear more than once:\n")
                bDupesFound=True
                print(f"{key}: {dWordcount[key]} times!")
                bValidation = False

        #So ya did everything as intended

        if bValidation:
            print("Password is valid and OK to be used!")
            break


#run the program
main()


# Reflection Questions

#1. What did I like about this assignment?
#I liked getting to see how it all turned out after I finished coding it and working out all the parts I messed up.

#2.What did I struggle with?
#I struggled with doing the assignment as a whole in general since my mind wanted to rush through it. As I got help from two of my classmates,
#I realized that I needed to do the project step by step and that helped a lot. It all made sense as I went through it slowly using material from our past classes
#and how to apply it to my code.

#3.How did I make my code efficent and reduced redundancy
#I made my code efficient by making the checks up to the occurences consist of 2-3 lines.
#I made my code redundant by having the letter, special character, and number check all be on the same loop than having it on different loops.

#4.Two things I learned from this assignment
#1.I learned to go slow when coding things and do them step by step
#2.I learned another way on how dictionaries work and how to use them to check for things.
# I came into this class only knowing dictionaries through my Love Live dictionary code (Please let me share it with the class one day!).
