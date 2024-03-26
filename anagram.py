def anagram(kata1, kata2):
    kata1 = kata1.lower()
    kata2 = kata2.lower()
    
    x1 = sorted(kata1)
    x2 = sorted(kata2)
    
    if x1 == x2:
        return True
    else:
        return False

kata1 = input("Masukkan kata pertama: ")
kata2 = input("Masukkan kata kedua: ")

if anagram(kata1, kata2):
    print(f"{kata1} dan {kata2} adalah anagram.")
else:
    print(f"{kata1} dan {kata2} bukan anagram.")