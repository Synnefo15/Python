class orang:

    def __init__(self, name, age, gender, tb, bb):
        self.nama = name
        self.umur = age
        self.kelamin = gender
        self.tinggibadan = tb
        self.beratbadan = bb

    def hasildatari(self):
        print(self)
        return "Nama pasien {} \n\t Umur Pasien = {} \n\t Kelamin = {} ".format(self.nama,self.umur,self.kelamin)

    def cekideal(self):
        ideal = self.tinggibadan - 110
        if(self.beratbadan < ideal):
            print("Anda kurus")
        elif(self.beratbadan == ideal ):
            print("Anda ideal")
        else:
            print("Anda Gemuk")
        return ideal

manusia1 = orang("Chinta", 19, "female", 160, 40)
manusia2 = orang("yopy", 18, "female", 150, 60)


print(manusia1.nama)

print(manusia2.hasildatari())
print(manusia2.cekideal())
print()

