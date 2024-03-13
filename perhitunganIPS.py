def perhitunganIPS():
    nilaiMatkul = []
    jumlahMatkul = int(input("Masukan jumlah mata kuliah: "))
    
    for i in range(jumlahMatkul):
        inputNilai = input("Masukan nilai mata kuliah ke{} (A/B/C/D): ".format(i+1))
        if inputNilai.upper() == 'A':
            nilaiAngka = 4
        elif inputNilai.upper() == 'B':
            nilaiAngka = 3
        elif inputNilai.upper() == 'C':
            nilaiAngka = 2
        elif inputNilai.upper() == 'D':
            nilaiAngka = 1
        else:
            print("Nilai tidak valid!")
            return

        nilaiMatkul.append(nilaiAngka)

    bobot = sum(nilaiMatkul)
    sks = jumlahMatkul * 3

    return bobot / sks
    
    
if __name__ == "__main__":
    ips = perhitunganIPS()    
    print(f"IPS semester ini adalah: {ips:.2f}")