def deret(tinggi, lebar):
    start = 1
    for i in range(tinggi):
        for j in range(lebar):
            print(start, end=" ")
            start += 1
        print()

tinggi = int(input("Masukkan tinggi deret: "))
lebar = int(input("Masukkan lebar deret: "))
deret(tinggi, lebar)
