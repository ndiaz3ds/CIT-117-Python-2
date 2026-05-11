#Now let's use our Numerology Python class so we don't have to spheal out a bunch of code

from NumerologyLifePathDetails import NumerologyLifePathDetails


def main():
    name = input("Enter your name: ").strip()
    while name=="":
        name = input("Name can't be empty. Enter your name: ").strip()
    dob= input("Enter your Date of birth (must be in mm-dd-yyyy or mm/dd/yyyy format): ").strip()
    while (
        len(dob) !=10
        or dob[2] not in "-/"
        or dob[5] != dob[2]
        or not dob[:2].isdigit()
        or not dob[3:5].isdigit()
        or not dob[6:].isdigit()
    ):
        dob= input("Invalid format, enter again using mm-dd-yyyy or mm/dd/yyyy format: ").strip()

    numerology = NumerologyLifePathDetails(name,dob)
    print("Name:", numerology.name)
    print("Birthdate:", numerology.birthdate)
    print("Life Path Number:", numerology.lifepath)
    print("Birthday Number", numerology.birthday)
    print("Attitude Number", numerology.attitude)
    print("Soul Number:", numerology.soul)
    print("Personality Number:", numerology.personality)
    print("Power Name Number:", numerology.powername)

    print(numerology.lifepathdescription)




if __name__ == "__main__":
    main()
