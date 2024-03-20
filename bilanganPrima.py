def cekPrima(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def primaTerdekat(n):
    if n <= 2:
        return None

    closest_prime = None
    for i in range(n - 1, 1, -1):
        if cekPrima(i):
            closest_prime = i
            break

    return closest_prime

n = int(input("Masukkan bilangan: "))

closest_prime = primaTerdekat(n)
if closest_prime:
    print(f"Bilangan prima terdekat dari {n} adalah {closest_prime}.")
else:
    print(f"Tidak ada bilangan prima terdekat yang kurang dari {n}.")
