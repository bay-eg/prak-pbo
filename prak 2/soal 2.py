class Login:
    admin_acc_username = 'Jotaro !!'
    admin_acc_password = 'NOOB DIO'
    user1_acc_username = 'Dandy Geming'
    user1_acc_password = 'sushi gantung 123'

    def __init__(self):
        self.username = 'default'
        self.password = 'default'
        self.try_ = 0
        print("__________________________")
        print("Masukkan Username dan Password!")
        print("Anda Punya 3 Kali Kesempatan")

    def try_input(func):
        def ulang(self, *args):
            if self.try_ < 3:
                return func(self, *args)
            else:
                return f"Anda telah mencoba sebanyak {self.try_} Tidak Dapat Melanjutkan !"
        return ulang

    @try_input
    def cek(self, username, password):
        self.try_ += 1
        if username == self.admin_acc_username and password == self.admin_acc_password:
            return f"Selamat Datang Kembali Admin Jotaro !"
        elif username == self.user1_acc_username and password == self.user1_acc_password:
            return f"Selamat Datang!"

    def run_(self):
        while True:
            username = input("Masukkan Username : ")
            password = input("Masukkan Password : ")
            self.cek(username, password)
            if self.try_ == 3:
                break

Login = Login()
Login.run_()