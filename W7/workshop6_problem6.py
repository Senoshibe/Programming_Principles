pens_stock = int(input("Number of pens in stock: "))
books_stock = int(input("Number of books in stock: "))

pens_requested = int(input("Number of pens requested by customer: "))
books_requested = int(input("Number of books requested by customer: "))

while pens_stock > 0 or books_stock > 0:
    pens_stock -= pens_requested
    books_stock -= books_requested
    print("Number of pens in stock: ", pens_stock)
    print("Number of books in stock: ", books_stock)

    pens_requested = int(input("Number of pens requested by customer: "))
    while True:    
        if pens_requested > pens_stock:
            low_stock_pens = input(f"There are only {pens_stock} pens in stock. Do you want to but the {pens_stock} pens? Y/N:")
            if low_stock_pens == "Y" or "y": 
                pens_requested = pens_stock
                break
            elif low_stock_pens == "N" or "n": 
                print("New pens must be ordered.")
                break
            else: 
                continue
        elif pens_stock == 0: 
            break
        else:
            break
    
    books_requested = int(input("Number of books requested by customer: "))
    while True:    
        if books_requested > books_stock:
            low_stock_books = input(f"There are only {books_stock} books in stock. Do you want to but the {books_stock} books? Y/N:")
            if low_stock_books == "Y" or "y": 
                books_requested = books_stock
                break
            elif low_stock_books == "N" or "n": 
                print("New books must be ordered.")
                break
            else: 
                continue
        elif books_stock == 0: 
            break
        else:
            break
    
