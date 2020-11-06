import datetime


class Buku:
    denda = 2000

    def __init__(self, id, judul, tglPinjam, tglKembali, lamaPinjam):
        self.id = id
        self.judul = judul
        self.tglPinjam = tglPinjam
        self.tglKembali = tglKembali
        self.lamaPinjam = lamaPinjam

    def HitungTerlambat(self):
        totalTerlambat = (self.tglKembali-(self.lamaPinjam+self.tglPinjam))
        print('total hari terlambat:', totalTerlambat)
        return totalTerlambat

    def TotalDenda(self):
        totalDenda = self.HitungTerlambat()*Buku.denda
        if self.HitungTerlambat() > 3:
            print('\n total denda:', totalDenda)
        else:
            None
        return totalDenda


buku1 = Buku(1, 'jojo', 2, 10, 3)

print(buku1.__dict__)
print(buku1.judul)
print(buku1.HitungTerlambat())
