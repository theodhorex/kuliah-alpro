# Mencari Nilai Terbesar

def nilaiTerbesar():
    try:
        a = int(input("Masukan nilai a: "))
        b = int(input("Masukan nilai b: "))
        c = int(input("Masukan nilai c: "))

        if (a > b) and (a > c):
            print(a, "adalah bilangan terbesar!")
        elif (b > a) and (b > c):
            print(b, "adalah bilangan terbesar!")
        elif (c > a) and (c > b):
            print(c, "adalah bilangan terbesar!")
    except ValueError:
        print("Masukan bilangan bulat bukan bilangan pecahan")
        
try:
    nilaiTerbesar()
except Exception as e:
    print("Error ngab!", e)