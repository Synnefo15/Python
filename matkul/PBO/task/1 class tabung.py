class Tabung:

    phi = 22/7
    jml_tabung = 0

    def __init__(self, tinggi, radius):

        self.t = tinggi
        self.r = radius

        Tabung.jml_tabung += 1

    def luasPermukaan(self):

        lp = Tabung.phi*2*self.r * (self.r+self.t)
        return lp

    def volume(self):

        vol = Tabung.phi*self.r**2*self.t
        return vol


tabung1 = Tabung(18, 7)
tabung2 = Tabung(21, 14)
print('Luas Permukaan tabung 1:', tabung1.luasPermukaan())
print('Vol tabung 1:', tabung1.volume())
print('vol tabung 2:', tabung2.volume())
print('jml tabung:', Tabung.jml_tabung)
