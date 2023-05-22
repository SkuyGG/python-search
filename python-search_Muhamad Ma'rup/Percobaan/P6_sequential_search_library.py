def is_similar(title1, title2):
    title1 = title1.lower()
    title2 = title2.lower()
    
    if title1[0] == title2[0]:
        return True
    
    return False

def sequential_search(books, book_title):
    for book in books:
        if is_similar(book['title'], book_title):
            return book['shelf']
        
    return "Buku tidak ditemukan"

books = [
    {'title' : 'Python', 'shelf' : 'A1'},
    {'title' : 'Javascript', 'shelf' : 'B2'},
    {'title' : 'PHP', 'shelf' : 'C3'},
    {'title' : 'CSS', 'shelf' : 'D4'}
]

book_title = input("Masukan judul buku yang ingin dicari: ")
shelf_location = sequential_search(books, book_title)
print(shelf_location)