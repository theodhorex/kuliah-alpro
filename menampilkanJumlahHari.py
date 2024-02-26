# Menampilkan jumlah hari dalam bulan yang diinginkan

import calendar

def menampilkanJumlahHari():
    try:
        bulanYangDiinginkan = input("Masukkan bulan berapa yang diinginkan (1-12): ")
        
        if not bulanYangDiinginkan.isdigit():
            raise ValueError("Masukkan value yang benar, value harus berupa angka dengan rentang 1-12")
        bulanYangDiinginkan = int(bulanYangDiinginkan)
        if bulanYangDiinginkan < 1 or bulanYangDiinginkan > 12:
            raise ValueError("Masukkan bulan yang benar, harus dalam rentang 1-12")
        
        print("Jumlah hari pada bulan", bulanYangDiinginkan, "adalah", calendar.monthrange(2020, bulanYangDiinginkan)[1])
    except ValueError as e:
        print(e)

try:
    menampilkanJumlahHari()
except Exception as e:
    print("Error ngab!", e)
