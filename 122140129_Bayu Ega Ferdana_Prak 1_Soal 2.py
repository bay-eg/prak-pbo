def luas(pi, r):
    return pi * r * r

def kel(pi, r):
    return 2 * pi * r

pi = 3.14
r = int(input("Jari Jari : "))
if r < 0:
    print("Jari Jari tidak boleh kurang dari 0!!!")
else :
    print("Luas :",luas(pi, r))
    print("Keliling :",kel(pi, r))
