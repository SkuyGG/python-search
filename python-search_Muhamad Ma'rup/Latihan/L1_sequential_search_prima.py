# Terdapat daftar bilangan [7, 10, 13, 6, 17, 22, 19]. 
# Temukan bilangan prima dalam daftar tersebut menggunakan sequential search.

def sequential_search_primes(angka):
    prima = []
    for num in angka:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime and num > 1:
            prima.append(num)
    return prima

angka = [7, 10, 13, 6, 17, 22, 19]
angka_prima = sequential_search_primes(angka)
print("Bilangan prima dalam daftar:", angka_prima)