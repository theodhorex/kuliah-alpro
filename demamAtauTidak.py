# Menentukan demam atau tidak dari suhu badan

def demamAtauTidak():
    try:
        suhuBadan = float(input("Masukkan suhu badan: "))
        
        if suhuBadan >= 38:
            print("Suhu badan anda", suhuBadan, "maka anda sedang demam!")
        else:
            print("Suhu badan anda", suhuBadan, "maka anda sedang tidak demam!")
    except ValueError:
        print("Masukkan suhu yang benar!")

try:
    demamAtauTidak()
except Exception as e:
    print("Error ngab!!", e)
