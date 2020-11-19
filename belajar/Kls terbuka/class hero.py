class hero:
    #class variabel
    jumlah_hero=0
    
    def __init__(self, inputName, inputHealth, inputPower, inputArmor ):
        self.name=inputName
        self.health=inputHealth
        self.power=inputPower
        self.armor=inputArmor
        hero.jumlah_hero+=1
    
    #void func, method tanpa return dan argumen
    def siapa(self):
        print('namaku adalah ', self.name)
        
    #method dgn argumen, tanpa return
    def healthUp(self,up):
        self.health+=up
        
    #method dengan return
    def getHealth(self):
        return self.health

hero1=hero('sniper',100,20,30)
hero2=hero('gun',90,88,23)

print('hero 1:',hero1.__dict__)
print('hero 2:',hero2.__dict__)

hero2.siapa()
hero2.healthUp(20)
print(hero2.getHealth())