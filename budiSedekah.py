def perhitunganTotalGaji(gajiPerjam, jamKerjaPerminggu):
    gajiSebelumPajak = gajiPerjam * jamKerjaPerminggu * 5

    pajak = 0.14 * gajiSebelumPajak
    gajiSetelahDipajak = gajiSebelumPajak - pajak

    baju = 0.10 * gajiSetelahDipajak
    alatTulis = 0.01 * gajiSetelahDipajak

    sisaUangGaji = gajiSetelahDipajak - baju - alatTulis
    sedekah = 0.25 * sisaUangGaji
    yatim = 0.30 * sedekah
    dhuafa = sedekah - yatim

    return gajiSebelumPajak, gajiSetelahDipajak, baju, alatTulis, sedekah, yatim, dhuafa

def main():
    gajiPerJam = float(input("Masukkan gaji per jam yang Anda inginkan: "))
    jamKerjaPerMinggu = float(input("Masukkan jumlah jam kerja per minggu: "))

    gajiSebelumPajaks, gajiSetelahPajaks, bajus, alatTuliss, sedekah, yatims, dhuafas = perhitunganTotalGaji(gajiPerJam, jamKerjaPerMinggu)

    print("1. Pendapatan Budi selama libur musim panas sebelum pajak: Rp.", gajiSebelumPajaks)
    print("2. Pendapatan Budi selama libur musim panas setelah pajak: Rp.", gajiSetelahPajaks)
    print("3. Uang yang akan dihabiskan untuk membeli pakaian dan aksesoris: Rp.", bajus)
    print("4. Uang yang akan dihabiskan untuk membeli alat tulis: Rp.", alatTuliss)
    print("5. Uang yang akan disedekahkan: Rp.", sedekah)
    print("6. Uang yang akan diterima anak yatim: Rp.", yatims)
    print("7. Uang yang akan diterima kaum dhuafa: Rp.", dhuafas)

if __name__ == "__main__":
    main()