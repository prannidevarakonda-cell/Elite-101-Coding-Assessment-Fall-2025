from library_books import library_books
from datetime import datetime, timedelta

# -------- Level 1 --------
# TODO: Create a function to view all books that are currently available
# Output should include book ID, title, and author
def available_books(books):
    # Let's show what books we have in stock
    print("Available_books:")
    print("---------------------------------------------------------")
    for book in books:
        if book["available"]:
            print(f"{book['id']} - {book['title']} by {book['author']}")
        # TODO: maybe add a counter for total available books later?


# -------- Level 2 --------
# Search function - works for both author and genre (case doesn't matter)
def search_books(books, search_term):
    search_term = search_term.lower()  # making it lowercase so we can match anything
    print("Search Results For:")
    print("-----------------------")

    books_found = False  # keeping track if we found anything

    for book in books:
        book_author = book["author"].lower()
        book_genre = book["genre"].lower()
        
        # Check if our search term appears in either author or genre
        if search_term in book_author or search_term in book_genre:
            print(f"{book['id']} {book['genre']} - {book['title']} by {book['author']}")
            books_found = True

    # Let them know if we didn't find anything
    if not books_found:
        print("Sorry, we couldn't find any books based on your search.")

            
# Note: might want to add title searching too in the future

# -------- Level 3 --------
# Checkout function - handles the whole checkout process
from datetime import datetime, timedelta

def checkout_book(books, book_id):
    print("Potential Checkout List:", book_id)  # probably should rename this print statement
    print("---------------------------------------------------")

    book_found = False
    
    for book in books:
        if book["id"] == book_id:
            book_found = True
            if book["available"] == True:  # being explicit here
                book["available"] = False
                # Set due date to 2 weeks from now
                today = datetime.now()
                due_date = today + timedelta(days=14)
                book["due_date"] = due_date.strftime("%Y-%m-%d")
                book["checkouts"] = book["checkouts"] + 1  # increment checkout counter
                print(f"You checked out '{book['title']}'. Be careful as the due date is: {book['due_date']}")
                break  # we found it, so let's get out of here
            else:
                print(f"Sorry, the book '{book['title']}' is already checked out. However, the due date is: {book['due_date']}")
                break

    if not book_found:
        print("Book ID not found! Please try again.")
            
        

# -------- Level 4 --------
# TODO: Create a function to return a book by ID
# Set its availability to True and clear the due_date

# TODO: Create a function to list all overdue books
# A book is overdue if its due_date is before today AND it is still checked out


# -------- Level 5 --------
# TODO: Convert your data into a Book class with methods like checkout() and return_book()
# TODO: Add a simple menu that allows the user to choose different options like view, search, checkout, return, etc.

# -------- Optional Advanced Features --------
# You can implement these to move into Tier 4:
# - Add a new book (via input) to the catalog
# - Sort and display the top 3 most checked-out books
# - Partial title/author search
# - Save/load catalog to file (CSV or JSON)
# - Anything else you want to build on top of the system!

if __name__ == "__main__":
   
    pass
