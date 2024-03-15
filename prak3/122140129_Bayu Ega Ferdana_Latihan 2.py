class Dagangan:
    jumlah_barang = 0
    list_barang = []

    def __init__(self, nama, stok, harga):
        self.__nama = nama
        self.__stok = stok
        self.__harga = harga
        Dagangan.jumlah_barang += 1
        Dagangan.list_barang.append((nama, stok, harga))
    
    @classmethod
    def liat_barang(self):
        print(f"Jumlah barang dagangan pada toko: {Dagangan.jumlah_barang} buah")
        for i in range(len(Dagangan.list_barang)):
            nama, stok, harga = Dagangan.list_barang[i]
            print(f"{i+1}. {nama} seharga Rp {harga} (stok: {stok})")
    
    def __del__(self):
        Dagangan.jumlah_barang -= 1
        for i in range(len(Dagangan.list_barang)):
            if Dagangan.list_barang[i][0] == self.__nama:
                del Dagangan.list_barang[i]
                break

Dagangan1 = Dagangan("Galon Aqua 19L", 32, 17000)
Dagangan2 = Dagangan("Gas LPG 5 kg", 22, 88000)
Dagangan3 = Dagangan("Beras Ramos 5 kg", 13, 68000)
Dagangan.liat_barang()
del Dagangan1
Dagangan.liat_barang()

