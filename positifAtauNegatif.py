# Mencari nilai Positif atau Negatif

def positifAtauNegatif():
    try:
        nilai = int(input("Masukan nilai: "))
        if nilai > 0:
            print(nilai, "adalah sebuah bilangan positif!")
        else:
            print(nilai, "adalah sebuah bilangan negatif!")
    except ValueError:
        print("Masukan nilai yang benar!")

try:
    positifAtauNegatif()
except Exception as e:
    print("Error ngab!!", e)