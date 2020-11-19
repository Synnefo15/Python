class Karyawan:
    uangTransportPerhari = 50000
    uangMakanPerhari = 50000

    def __init__(self,  gajiPokok, tunjanganKeluarga, jumlahKehadiran):

        self.gajiPokok = gajiPokok
        self.tunjanganKeluarga = tunjanganKeluarga
        self.jumlahKehadiran = jumlahKehadiran

    def uangTransport(self):
        totalUangTransport = Karyawan.uangTransportPerhari * self.jumlahKehadiran
        return totalUangTransport

    def uangMakan(self):
        totalUangMakan = Karyawan.uangMakanPerhari*self.jumlahKehadiran
        return totalUangMakan

    def gajiKaryawan(self):
        totalGajiKaryawan = self.gajiPokok+self.tunjanganKeluarga + self.uangMakan() + self.uangTransport()
        return totalGajiKaryawan


Karyawan1 = Karyawan(2500000, 1000000, 20)
Karyawan2 = Karyawan(2750000, 1100000, 22)
Karyawan3 = Karyawan(200000, 0, 25)
Karyawan4 = Karyawan(3000000, 1250000, 18)

print('Gaji karyawan 1')
print('Gaji pokok:{:,}'.format(Karyawan1.gajiPokok))
print('Tunjangan Keluarga:{:,}'.format(Karyawan1.tunjanganKeluarga))
print('Uang Transport:{:,}'.format(Karyawan1.uangTransport()))
print('Uang Makan:{:,}'.format(Karyawan1.uangMakan()))
print('Total:{:,}'.format(Karyawan1.gajiKaryawan()))
