# Pengecekan kesamaan sisi

def pengecekanKesamaanSisi():
    try:
        sisiA, sisiB, sisiC = int(input("Masukan sisi A: ")), int(input("Masukan sisi B: ")), int(input("Masukan sisi C: "))

        if sisiA == sisiB and sisiB == sisiC:
            print("3 sisi sama!")
        elif sisiA == sisiB or sisiA == sisiC or sisiB == sisiC:
            print("2 sisi sama!")
        else:
            print("Tidak ada yang sama!")
    except ValueError as e:
        print("Masukan value yang benar! harus berupa bilangan dan bukan huruf!")
        
try:
    pengecekanKesamaanSisi()
except Exception as e:
    print("Error ngab!", e)
        