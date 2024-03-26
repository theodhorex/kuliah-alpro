def cariKataTerpendekTerpanjang(kalimat):
    kataKalimat = kalimat.split()
    kataTerpendek = min(kataKalimat, key=len)
    kataTerpanjang = max(kataKalimat, key=len)
    return kataTerpendek, kataTerpanjang

kalimatInput = input("Masukkan kalimat: ")

kataTerpendek, kataTerpanjang = cariKataTerpendekTerpanjang(kalimatInput)

print(f"Terpendek: {kataTerpendek}, Terpanjang: {kataTerpanjang}")




