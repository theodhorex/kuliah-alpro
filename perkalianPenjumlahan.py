def perkalian(angkaSatu, angkaDua):
    hasil = 0
    for i in range(angkaDua):
        hasil += angkaSatu
        if i != 0:
            print("+", angkaSatu, end=" ")
        else:
            print(angkaSatu, end=" ")
            
    print(f"= {hasil}")

perkalian(2, 5)