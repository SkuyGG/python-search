# Buatlah sebuah fungsi yang menggunakan binary search untuk mencari posisi sisipan sebuah 
# elemen dalam sebuah daftar yang sudah diurutkan secara menaik. Jika elemen sudah ada dalam
# daftar, fungsi akan mengembalikan indeksnya. Jika elemen tidak ada dalam daftar, fungsi
# akan mengembalikan indeks tempat elemen tersebut dapat disisipkan untuk menjaga urutan

# daftar tetap terurut.
# ➢ Contoh Input
# data = [2, 4, 6, 8, 10, 12, 14]
# target = 7
# ➢ Contoh Output
# Elemen 7 dapat disisipkan pada indeks 3 untuk menjaga daftar tetap terurut.

def binary_search_insert_position(data, target):
    left = 0
    right = len(data) - 1

    while left <= right:
        mid = (left + right) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left

my_list = [2, 4, 6, 8, 10, 12, 14]
target = 7
insert_position = binary_search_insert_position(my_list, target)
print(f"Posisi sisipan elemen {target} adalah {insert_position}.")