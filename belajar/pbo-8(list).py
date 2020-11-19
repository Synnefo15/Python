class Matakuliah:
    def __init__(self, kd, nama, sks):
        self.kd = kd
        self.nama = nama
        self.sks = sks


    # menampung list
daftar = []

# === entri manual===
# mk1 = Matakuliah('mk1', 'agama', 2)
# daftar.append(mk1)
# mk2 = Matakuliah('mk2', 'pcl', 3)
# daftar.append(mk2)

# === entri input===
# print('input 1')
# start=input('masukkan inisiasi program:') #tekan y/n
# while (start=='y'):
#     a=input('masukkan matkul:')
#     b=input('masukkan kode:')
#     c=input('masukkan sks:')
#     mk=Matakuliah(a,b,c)
#     daftar.append(mk)
#     start=input('lanjutkan program?')
#     if start=='n':
#         break

# print('input2')
# start = 'y'
# while start != 'n':
#     start = input('masukkan inisiasi program:')  # tekan y/n
#     if start=='n':
#         break
#     a=input('masukkan matkul:')
#     b=input('masukkan kode:')
#     c=input('masukkan sks:')
#     mk=Matakuliah(a,b,c)
#     daftar.append(mk)

print('input3')
start = 'y'
while start != 'n':
    a = input('masukkan matkul:')
    b = input('masukkan kode:')
    c = input('masukkan sks:')
    mk = Matakuliah(a, b, c)
    daftar.append(mk)
    start = input('apa ingin melanjjutkan? # press y/n...')

# ===opsi ngeprint===

# print('cara1===')
# for i in range(len(daftar)):
#     print(f'kd: {daftar[i].kd} nama: {daftar[i].nama} sks: {daftar[i].sks}')

print('cara2===')
for i in range(len(daftar)):
    print('nama: {},mk: {},sks: {}'.format(
        daftar[i].nama, daftar[i].kd, daftar[i].sks))

# print('cara3===')
# for i in range(len(daftar)):
#     print('nama: %s kd: %s sks: %i' %
#           (daftar[i].nama, daftar[i].kd, daftar[i].sks))

# print('cara4===')
# for Matakuliah in daftar:
#     print('kd', Matakuliah.kd, 'nama', Matakuliah.nama,
#           'sks', Matakuliah.sks, sep=';')
