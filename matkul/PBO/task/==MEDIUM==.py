class BangunRuang:
    phi = 22/7

    def __init__(self, panjang, lebar, tinggi, radius):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi
        self.radius = radius


class Balok(BangunRuang):

    def __init__(self, panjang, lebar, tinggi):
        super().__init__(panjang, lebar, tinggi)

    def volume(self):
        vol = self.panjang * self.lebar * self.tinggi
        return vol

    def luas(self):
        luaz = 2*((self.panjang * self.lebar) + (self.lebar *
                                                 self.tinggi) + (self.tinggi * self.panjang))
        return luaz


class Kubus(BangunRuang):
    def __init__(self, panjang):
        super().__init__(panjang)

    def volume(self):
        vol = self.panjang**3
        return vol

    def luas(self):
        luaz = (self.panjang**2)*6
        return luaz


class Tabung(BangunRuang):
    def __init__(self, radius, tinggi):
        super().__init__(radius, tinggi)

    def volume(self):
        vol = BangunRuang.phi*self.radius**2*self.tinggi
        return vol

    def luas(self):
        luaz = BangunRuang.phi*2*self.radius * (self.radius+self.tinggi)
        return luaz


class Listrik:
    def __init__(self, energi, waktu):
        self.energi = energi
        self.waktu = waktu


class DayaListik(Listrik):
    def __init__(self, energi, waktu):
        super().__init__(energi, waktu)

    def hitungDaya(self):
        P = self.energi/self.waktu
        return P


class HamdatanListik(Listrik):
    def __init__
