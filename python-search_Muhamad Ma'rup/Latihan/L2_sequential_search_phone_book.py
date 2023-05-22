# John, Jane, Michael, dan Emily adalah empat teman yang tinggal dalam satu kompleks perumahan.
# Mereka memiliki nomor telepon masing-masing yang tersimpan dalam buku telepon. John sering kali
# lupa menyimpan nomor telepon teman-temannya dan sering kali harus meminta nomornya lagi.
# Kali ini, John ingin mencari nomor telepon Jane. Berdasarkan tabel buku telepon berikut:

#       Nama                           No. Telepon
#       John Doe           -           081234567890
#       Jane Smith         -           089876543210
#       Michael Johnson    -           087811223344
#       Emily Davis        -           082122232425

def is_similar(title1, title2):
    title1 = title1.lower()
    title2 = title2.lower()
    
    if title1[0] == title2[0]:
        return True
    
    return False

def sequential_search(books, book_title):
    for book in books:
        if is_similar(book['name'], book_title):
            return book['phone_num']
        
    return "Nomer tidak ditemukan"

books = [
    {'name' : 'John Doe', 'phone_num' : '081234567890'},
    {'name' : 'Jane Smith', 'phone_num' : '089876543210'},
    {'name' : 'Michael Jhohnson', 'phone_num' : '087811223344'},
    {'name' : 'Emily Davis', 'phone_num' : '082122232425'}
]

phone_book = input("Masukan nama yang ingin dicari: ")
nomer = sequential_search(books, phone_book)
print(nomer)