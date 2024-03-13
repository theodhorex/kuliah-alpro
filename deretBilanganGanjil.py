def ganjil(batasAtas, batasBawah):
    if batasAtas > batasBawah:
        for i in range(batasBawah + 1, batasAtas, 2):
            print(i)
    elif batasBawah > batasAtas:
        for i in range(batasBawah, batasAtas - 1, -2):
            print(i)
    
# ganjil(5, 15)
ganjil(15, 5)