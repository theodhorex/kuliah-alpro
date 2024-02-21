def functionCalc(x):
    return 2 * x ** 3 + 2 * x + 15 / x
def main():
    nilaiX = int(input("Masukan nilai dari x : "))
    hasilDariFungsi = functionCalc(nilaiX)
    print("Hasil dari perhitungan fungsi diatas adalah ", hasilDariFungsi)
    
if __name__ == "__main__":
    main()