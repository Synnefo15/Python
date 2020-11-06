class Hero:
    
    def __init__(self, name, health, attackPower, armorNumber):
        self.name=name
        self.health=health
        self.attackPower=attackPower
        self.armorNumber=armorNumber
    
    def serang(self,lawan):
        print(self.name, 'menyerang', lawan.name)
        lawan.diserang(self, self.attackPower)
    
    def diserang(self,lawan):
        print(self.name, 'diserang', lawan.name)
        

sniper=Hero('sniper',100,10,5)
gun=Hero('gun',120,15,2)

sniper.serang(gun)