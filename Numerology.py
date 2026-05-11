# Start by defining the class

class Numerology:
    def __init__(self, sName, sDOB):
        self.__sName = sName
        self.__sDOB = sDOB

        # let's precompute everything at once
        birthdate = sDOB.replace('-', '').replace('/','')
        name = sName.lower()

        self.__attitude = self.__calculateAttitude(birthdate)
        self.__birthday = self.__calculateBirthday(birthdate)
        self.__lifepath = self.__calculateLifePath(birthdate)
        self.__personality = self.__calculatePersonality(name)
        self.__powerName = self.__calculatePowerName(name)
        self.__soul = self.__calculateSoul(name)

    def __reduce(self, num):
        while num > 9:
            num = num % 10 + num // 10
        return num

    def __calculateAttitude(self, birthdate):

        month = int(birthdate[0:2])
        day = int(birthdate[2:4])
        return self.__reduce(month + day)

    def __calculateBirthday(self, birthdate):

        day = int(birthdate[2:4])
        return self.__reduce(day)


    def __calculateLifePath(self, birthdate):
        total = sum(int(char) for char in birthdate)
        return self.__reduce(total)


    def __calculatePersonality(self, name):
       vowels = ['a', 'e', 'i', 'o', 'u']
       total = sum((ord(c) - 96) for c in name if c.isalpha() and c not in vowels)
       return self.__reduce(total)


    def __calculatePowerName(self, name):
        total = sum(ord(c) - 96 for c in name if c.isalpha())
        return self.__reduce(total)


    def __calculateSoul(self, name):
         vowels = ['a', 'e', 'i', 'o', 'u']
         total = sum((ord(c) - 96) for c in name if c.isalpha() and c in vowels)
         return self.__reduce(total)


# Set up the Getters
    @property
    def name(self):
        return self.__sName

    @property
    def birthdate(self):
        return self.__sDOB

    @property
    def lifepath(self):
        return self.__lifepath

    @property
    def personality(self):
        return self.__personality

    @property
    def powername(self):
        return self.__powerName

    @property
    def soul(self):
        return self.__soul

    @property
    def attitude(self):
        return self.__attitude

    @property
    def birthday(self):
        return self.__birthday
