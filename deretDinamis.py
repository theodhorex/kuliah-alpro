def faktor(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * faktor(num - 1)

def baris(n):
    for i in range(n, 1, -1):
        result = faktor(i)
        print(result, end=" ")
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()

nilai = int(input("Masukan nilai: "))
baris(nilai)
