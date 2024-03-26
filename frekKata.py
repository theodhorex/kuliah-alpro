import re

def mencariFrekuensiKata(kalimat, kata):
    kalimat = re.sub(r'[^\w\s]', '', kalimat)
    kataKalimat = kalimat.lower().split()
    frekuensi = sum(1 for word in kataKalimat if word == kata.lower())
    return frekuensi

kalimat = "Saya mau makan. Makan itu wajib. Mau siang atau malam saya wajib makan"
kataYangDicari = input("Masukan kata yang ingin dicari: ")

jumlahKataYangMuncul = mencariFrekuensiKata(kalimat, kataYangDicari)

print(f"Kata '{kataYangDicari}' muncul sebanyak {jumlahKataYangMuncul} kali dalam kalimat.")
