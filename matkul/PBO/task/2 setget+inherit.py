class Ikan:

    jumlah = 0

    def __init__(self, name, age):
        self.__nama = name
        self.__usia = age
        Ikan.jumlah += 1

    @property
    def setnama(self):
        pass

    @property
    def getnama(self):
        pass

    @property
    def setusia(self):
        pass

    @property
    def getusia(self):
        pass

    @setnama.setter
    def setnama(self, value):
        self.__nama = value

    @getnama.getter
    def getnama(self):
        return self.__nama

    @setusia.setter
    def setusia(self, value):
        self.__usia = value

    @getusia.getter
    def getusia(self):
        return self.__usia


class IkanHias(Ikan):

    def __init__(self, name, age, color, price):
        super().__init__(name, age)
        self.__warna = color
        self.__harga = price

    @property
    def setwarna(self):
        pass

    @property
    def getwarna(self):
        pass

    @property
    def setharga(self):
        pass

    @property
    def getharga(self):
        pass

    @setwarna.setter
    def setwarna(self, value):
        self.__warna = value

    @getwarna.getter
    def getwarna(self):
        return self.__warna

    @setharga.setter
    def setharga(self, value):
        self.__harga = value

    @getharga.getter
    def getharga(self):
        return self.__harga

    # def rumus(self):
    #     if IkanHias2.getnama == IkanHias2.nama:
    #         print(IkanHias2.__dict__)
    #     else:
    #         None


IkanHias1 = IkanHias('Cupang', 3, 'kuning', 4000)
IkanHias2 = IkanHias('Lohan', 8, 'merah', 20000)


# print('\n banyak ikan:', IkanHias.jumlah, '\n yaitu:',
#       IkanHias1.getnama, 'dan', IkanHias2.getnama)
# print(IkanHias2.__dict__)
# print('\n Update data...')
# IkanHias2.rumus = input('nama ikan:')
# IkanHias2.setusia = int(input('usia update:'))
# IkanHias2.setwarna = input('warna update:',)
# IkanHias2.setharga = int(input('harga update:'))
# print('hasil update:\n', IkanHias2.__dict__)

print(IkanHias2.nama)
