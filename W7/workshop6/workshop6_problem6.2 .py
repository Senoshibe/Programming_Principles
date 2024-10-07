pens_stock = int(input("Number of pens in stock: "))
books_stock = int(input("Number of books in stock: "))

pens_requested = int(input("Number of pens requested by customer: "))
books_requested = int(input("Number of books requested by customer: "))

while pens_stock > 0 and books_stock > 0:
    pens_stock -= pens_requested
    books_stock -= books_requested
    print("Number of pens in stock: ", pens_stock)
    print("Number of books in stock: ", books_stock)
    pens_requested = int(input("Number of pens requested by customer: "))
    books_requested = int(input("Number of books requested by customer: "))