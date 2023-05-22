# Rani adalah seorang siswa yang rajin belajar dan sangat tertarik dengan kamus. Suatu hari, 
# Rani menemukan kamus ajaib di perpustakaan sekolahnya. Kamus tersebut memiliki kemampuan 
# untuk langsung memberikan definisi kata yang dicari. Rani ingin mencoba keajaiban kamus 
# tersebut dengan mencari definisi kata yang diinginkan. Berdasarkan kamus ajaib di bawah ini, 
# temukan definisi kata menggunakan binary search.

# Kata                          Definisi
#Apple                          Buah Apel
#Banana                         Buah Pisang
#Cat                            Kucing
#Duck                           Bebek
#Elephant                       Gajah

def binary_search_definition(data, target_word):
    left = 0
    right = len(data) - 1

    while left <= right:
        mid = (left + right) // 2

        if data[mid][0] == target_word:
            return data[mid][1]
        elif data[mid][0] < target_word:
            left = mid + 1
        else:
            right = mid - 1

    return "Definisi kata tidak ditemukan."

data = [
    ["Apple", "Buah Apel"],
    ["Banana", "Buah Pisang"],
    ["Cat", "Kucing"],
    ["Duck", "Bebek"],
    ["Elephant", "Gajah"]
]

target_word = input("Masukan kata/kalimat : ")

kata = binary_search_definition(data, target_word)
if kata != "Definisi kata tidak ditemukan.":
    print("Definisi kata", target_word + ":", kata)
else:
    print(kata)