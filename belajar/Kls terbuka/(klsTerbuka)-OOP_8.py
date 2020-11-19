class Hero:

    def __init__(self, name, health, attPow):
        self.__name = name
        self.__health = health
        self.__attPow = attPow

    # getter
    def getName(self):
        return self.__name

    def getHealth(self):
        return self.__health

    # setter
    def diserang(self, serangPow):
        self.__health -= serangPow


rafi = Hero('rafi', 100, 15)

print(rafi.getName())
print(rafi.getHealth())
rafi.diserang(10)
print(rafi.getHealth())
