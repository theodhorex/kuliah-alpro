def bmiCalc(bmi, tinggi):
    berat_diperlukan = bmi * (tinggi ** 2)
    return berat_diperlukan

def main():
    tinggi = float(input("Masukkan tinggi badan (meter): "))
    bmi_diharapkan = float(input("Masukkan nilai BMI yang diharapkan: "))
    
    berat_diperlukan = bmiCalc(bmi_diharapkan, tinggi)
    print("Berat badan yang diperlukan:", berat_diperlukan, "kg")

if __name__ == "__main__":
    main()