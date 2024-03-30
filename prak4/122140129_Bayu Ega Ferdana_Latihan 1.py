class hewan:
    def _init_(self, nama, jenis_kelamin):
        self.nama = nama
        self.jenis_kelamin = jenis_kelamin
    def bersuara(self):
        pass
    def makan(self):
        pass
    def minum(self):
        pass
    
class kucing(hewan):
    def bersuara(self):
        print(f"kucing {self.nama} bersuara: Meong!")
    def makan(self):
        print(f"kucing {self.nama} sedang makan: tulang")
    def minum(self):
        print(f"kucing {self.nama} sedang minum: susu")
class anjing(hewan):        
    def bersuara(self):
        print(f"anjing {self.nama} bersuara: Guk Guk!")
    def makan(self):
        print(f"anjing {self.nama} sedang makan: tulang")
    def minum(self):
        print(f"anjing {self.nama} sedang minum: air")    
        
hewan1 = Kucing("kiki", "betina")
hewan2 = Anjing("ichi", "jantan")
print(hewan1.nama)
print(hewan2.nama)
hewan1.bersuara()
hewan1.makan()
hewan1.minum()
hewan2.bersuara()
hewan2.makan()
hewan2.minum()