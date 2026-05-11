# Start by defining the class

from Numerology import Numerology

class NumerologyLifePathDetails(Numerology):



    @property
    def lifepathdescription(self):
        descriptions = {
            1: "The Independent: Wants to work, think for themselves.",
            2: "The Mediator: Avoids conflict and wants love and Harmony.",
            3: "The Performer: Likes music, art, and to perform or get attention.",
            4: "The Teacher/Truth Seeker: You're meant to be a teacher or mentor and is truthful.",
            5: "The Adventurer: Likes to travel ad meet others, often an extrovert.",
            6:  "The Inner Child: Is meant to be a parent and/ or is one at heart.",
            7:  "The Naturalist: Enjoys nature and water and alternative life paths, open to spirituality.",
            8: "The Executive: Gravitates to money and power.",
            9: "The Humanitarian: Helps others and/or experiences pain and learns the hard way."

        }

        return descriptions[self.lifepath]






#Nicholas Diaz

#Numerology inheritance

#What did I struggle with?
    # I was confused if I had to change the properties in Numerology or write them again in NumerologyPathDetails.py

#How does a decoration work
    #A decoration is a little tagline that tells python to treat the string as the method the decorator is chosen as. Like its a sign telling something of a certain rule like a wet floor for example.

#What did I learn?
    #1.How to modify my code for inheritance
    #2.How easy it was to dot this assignment after reading the instructions carefully and not overthink it.
