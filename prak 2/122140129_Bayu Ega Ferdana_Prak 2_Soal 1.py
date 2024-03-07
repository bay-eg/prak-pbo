class mahasiswa :
    def __init__(self, nim, nama, angkatan, isMahasiswa = False):
      self.nama = nama
      self.nim = nim
      self.angkatan = angkatan
      self.isMahasiswa = isMahasiswa

    def input_nama(self, Nnama):
      self.nama = Nnama
    def input_angkatan(self, Aangkatan):
      self.angkatan = Aangkatan
    def input_nim(self, Nnim):
      self.nim = Nnim
    def show_nama(self):
      return f"name : {self.nama}"
    def show_nim(self):
      return f"nim  : {self.nim}"
    def show_angkatan(self):
      return self.angkatan
    def trueMahasiswa(self):
      if len(self.nim) == 9 and self.angkatan >= 2015 and self.angkatan < 2025 or self.isMahasiswa == True:
        return True
      else :
        return False
    def returnMahasiswa(self):
      if self.trueMahasiswa() :
        return f"Nama : {self.nama}\nNIM  : {self.nim}\nMerupakan Mahasiswa Angkatan {self.angkatan}\n__________________"
      else:
        return f"DATA TIDAK SESUAI / BUKAN MAHASISWA!!\n__________________"
    
mahasiswa_1 = mahasiswa(nim = '122140129', nama = 'Bayu Ega Ferdana', angkatan = 2022)
mahasiswa_2 = mahasiswa(nim = '122140127', nama = 'Rizky Abdillah', angkatan = 2022, isMahasiswa = True)
mahasiswa_3 = mahasiswa(nim = '12222233339', nama = 'King Fulan Tzy', angkatan = 2014)
print(mahasiswa_1.returnMahasiswa())
print(mahasiswa_2.returnMahasiswa())
print(mahasiswa_3.returnMahasiswa())

mahasiswa_4 = mahasiswa(nim = '2213052062', nama = 'Bintot I miss her', angkatan = 2022)
print(mahasiswa_4.returnMahasiswa())
print(mahasiswa_4.show_nama())
print(mahasiswa_4.show_nim())
print("__________________")
Nnama = 'Bintar Arba Purbaya'
Nnim = '122250555'
mahasiswa_4.input_nama(Nnama)
mahasiswa_4.input_nim(Nnim)
print(f"new {mahasiswa_4.show_nama()}")
print(f"new {mahasiswa_4.show_nim()}")
print("__________________")
print(mahasiswa_4.returnMahasiswa())






    

