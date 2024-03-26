def hapusSpasiBerlebih(kalimat):
    kalimat = ' '.join(kalimat.split())
    return kalimat

kalimat = input("Masukkan kalimat: ")

yangSudahDihapusSpasinya = hapusSpasiBerlebih(kalimat)

print(yangSudahDihapusSpasinya)



