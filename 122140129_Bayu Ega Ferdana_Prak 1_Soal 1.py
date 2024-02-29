# Bayu Ega Ferdana
# 122140129
def bGanjil(n, m):
    total = 0
    for i in range (n, m):
        if i % 2 != 0:
            total += i
    return total        


n = int (input("Batas Atas : "))
m = int (input("Batas Bawah : "))
if n <= 0 or m <= 0:
    print("Batas Atas / Bawah tidak boleh dibawah nol!")
else:
    print("Total :",bGanjil(n,m))
