class Mahasiswa:

    def __init__(self, nama, nim, ipk, ukt):
        self.nama = nama
        self.nim = nim
        self.ipk = ipk
        self.ukt = ukt

    def cekNim(self):
        data = self.nim
        if anak1.nim == 1010:
            print('data:', anak1.__dict__)
        elif anak2.nim == 1020:
            print('data', anak2.__dict__)
        elif anak3.nim == 1129:
            print('data', anak3.__dict__)
        else:
            None
        return data


anak1 = Mahasiswa('Zayn', 1010, 3.2, 2000000)
anak2 = Mahasiswa('Josh', 1020, 3.7, 4000000)
anak3 = Mahasiswa('ACel', 1129, 2.3, 5000000)


data = input('masukkan nim:')
print(anak1.cekNim())
