import pickle


#set up the file system to store our results
def load_history(DB_FILE_NAME):
    try:
        with open(DB_FILE_NAME, "rb") as f:
            dictPlanetHistory = pickle.load(f)
        print(f"Loaded previous history from {DB_FILE_NAME} successfully")
        return dictPlanetHistory
    except FileNotFoundError:
        print(f"No history file found at {DB_FILE_NAME}")
    except Exception as e:
        print(f"An error occurred while loading the history file: {e}\n")

    return {}

#set up our main function and take on all the weights
def main():
    DB_FILE_NAME = "ndPlanetary Weights.db"


#start our planet weights dictionary

    dictPlanetFactors = {
    "Mercury": 0.38,
    "Venus": 0.91,
    "Moon": 0.165,
    "Mars": 0.38,
    "Jupiter": 2.34,
    "Saturn": 0.93,
    "Uranus": 0.92,
    "Neptune": 1.12,
    "Pluto": 0.066,
    }

#Load History
    dictPlanetHistory = load_history(DB_FILE_NAME)




#Prompt the user for their history.
    if dictPlanetHistory:
        while True:
            strShowHistory= input("Would you like to see your history? Y/N").strip().lower()
            if strShowHistory == "y":
                print("\n-------Planetary Weights History-------")
                for strName, weights in dictPlanetHistory.items():
                    print(f"\nName: {strName}")
                    for planet, weight in weights.items():
                        print(f"  {planet:<10}:  {weight:10.2f}")
                print("----------------------------------\n")
                break
            elif ShowHistory == "n":
                break
            else:
                print("Invalid input, please enter Y/N")

 #Make a loop that calculates takes your name and makes sure others don't do it as well
    while True:
        strName= input("What is your name? (or leave it blank to finish)").strip().title()

        if not strName:
            print("Thank you for using the Planetary Weights Database")
            break

#will the same name be in the history?
        if strName in dictPlanetHistory:
            print(f"{strName} is already in the history file")
            continue
#Prompt for the user's weight on Earth and make sure its validated
        while True:
            try:
                fltWeightInput = float(input("What is your earth weight? (in kg)").strip())

                if fltWeightInput <= 0:
                 print("Invalid input, please enter a positive number")
                else:
                    break
            except ValueError:
                print("Invalid input, please enter a number for weight.")


#We'll need another dictionary for the user's weights
        dictPersonsWeights={}

#Now we can set up the weight calculator
        print(f"\n{strName}, here are your weights on our Solar System's planets.")
        for planet, factor in dictPlanetFactors.items():
            fltPlanetWeight= fltWeightInput * factor
        #add the results to dictPersonsWeight
            dictPersonsWeights[planet] = fltPlanetWeight

        #Output those results and format it properly
            print(f" {planet:<10}:  {fltPlanetWeight:10.2f}")

    #Add everything to dictPlanetHistory
        dictPlanetHistory[strName] = dictPersonsWeights
        print(f"History has been updated for \n{strName}.")
        print("-" *30, "\n")



#Now, let's exit our loop
    try:
        with open(DB_FILE_NAME,"wb") as f:
            pickle.dump(dictPlanetHistory, f)
            print(f"Saved history to {DB_FILE_NAME} successfully")
    except Exception as e:
        print(f"An error occurred while saving the history file: {e}\n")

#call the file
main()





#Name: Nicholas Diaz
#Assignment: Planetary Weights Dictionaries

#What did I like about the assignment?

#I liked getting to create dictionaries and making my LoveLive sim helped a bit with this assignment

#What did I struggle with?

#I struggled with looping the end properly as it would always exit after doing one input.

#Did I like working with dictionaries and pickling?

#I think this was ok but I think my LoveLive sim was more fun to code. I learned that I really learn to code well when I'm just allowed to code freely and not have it be up to certain standards. But this assignment also showed me how fun pickling is and how you can recall your history.

#2 things I learned from the assignment

# 1. I need to work more on my alignment. My code failed many times at first because some of the inputs and prints were misaligned with their respective tabs.

# 2. I learned the true importance of functions as I used two to make this code work.
