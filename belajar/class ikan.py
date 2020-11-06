class ikan:

    def __init__(self, nama, jenis, warna, harga, usia):
        self.nama = nama
        self.jenis = jenis
        self.harga = harga
        self.usia = usia
        # usia dlm bulan
        self.warna = warna


ikan_1 = ikan('cupang', 'tawar', 'biru-merah', 1000, 5)
ikan_2 = ikan('lohan', 'tawar', 'merah-putih', 3000, 10)

print('ikan1:', ikan_1.__dict__)
