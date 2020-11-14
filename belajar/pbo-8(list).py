class Matakuliah:
    def __init__(self,kd,nama,sks):
        self.kd=kd
        self.nama=nama
        self.sks=sks

#daftar
daftar=[]
mk=Matakuliah('mk1','agama',2)
daftar.append(mk)
print(mk.kd)
print(mk.nama)
mk=Matakuliah('mk2','pcl',3)
daftar.append(mk)