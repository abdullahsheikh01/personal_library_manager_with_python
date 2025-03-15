from InquirerPy import prompt 
# Last Menu Function 
def last_menu():
    last_menu = prompt(
            {
                "name":"option",
                "message":"",
                "type":"list",
                "choices":["Menu","Exit"]
            }
        )
    if last_menu["option"]=="Menu":
        menu()
    else:
        print("Goodbye!")
# New Book Addinng
def add_book():
    print("Enter the info about book")
    # New Book Info Questions
    new_book = prompt(
        [
            {
                "name":"title",
                "message":"Enter Title of book📗",
                "type":"input"
            },
            {
                "name":"author",
                "message":"Enter the name of author of book📗",
                "type":"input"
            },
            {
                "name":"publication_year",
                "message":"Enter the publication year of book📗",
                "type":"input",
            },
            {
                "name":"genre",
                "message":"Enter the genre(type) of book📗",
                "type":"input",
            },
            {
                "name":"read_status",
                "message":"Have you read this book📖❓",
                "type":"confirm"
            }
    ]
    ),
    # Books Adding 
    books.append(new_book[0])
    last_menu()
# Function for removing a book
def remove_book():
    if len(books)>0:
        book_remove_options : list[str] = []
        for book in books:
            if book["read_status"]:
                book_remove_options.append(book["title"])
            else:
                book_remove_options.append(book["title"])
        remove_book_title = prompt(
            {
                "name":"title",
                "message":"Choose Your Book to Remove",
                "type":"list",
                "choices":book_remove_options
            }
            )
        for book in books:
            if remove_book_title["title"] == book["title"]:
                books.remove(book)
    else:
        print("Library is empty")
    last_menu()
# Search Book Function for Searching a Book
def search_book():
    if len(books)>0:
        search_option = prompt(
            [
                {
                    "name":"option",
                    "message":"input",
                    "type":"list",
                    "choices":["Title","Author"]
                }
            ]
        )
        names : list[str] = []
        for book in books:
            names.append(book[search_option["option"].lower()])
        choose_names = prompt(
                {
                    "name":"name",
                    "message":f"Choose Name of {search_option['option']}",
                    "type":"list",
                    "choices":names
                }
        )
        for book in books:
            if book[search_option["option"].lower()] == choose_names["name"]:
                print("Book Details:")
                if book["read_status"]:
                    print(f"""{books.index(book)+1}. {book["title"]} by {book["author"]}({book["publication_year"]}) - {book["genre"]} - Read""")
                else:
                    print(f"""{books.index(book)+1}. {book["title"]} by {book["author"]}({book["publication_year"]}) - {book["genre"]} - Unread""")
        last_menu()   
    else:
        print("You can't search for a book because Library is empty")
        last_menu()
# Function for Display all books
def display_all_books():
    if len(books)>0:
        print("Books:")
        for book in books:
            if book["read_status"]:
                print(f"""{books.index(book)+1}. {book["title"]} by {book["author"]}({book["publication_year"]}) - {book["genre"]} - Read""")
            else:
                print(f"""{books.index(book)+1}. {book["title"]} by {book["author"]}({book["publication_year"]}) - {book["genre"]} - Unread""")
    else:
        print("Book Library is Empty")
    last_menu()
# Function to Display Statistics 
def display_statistics():
    if len(books)>0:
        read_score:int = 0
        for book in books:
            if book["read_status"]:
                read_score+=100
            else:
                read_score+=0
        print(
            f"Total Books: {len(books)}\nPercentage Of Read: {read_score/len(books)}%"
        )
    else:
        print("Library is Empty")
    last_menu()
# Books List
books : list[
    dict[str,any]
] = []
# Menu Function
def menu():
    # Question to ask for menu option
    menu_question = prompt(
    [
        {
            "name":"question1",
            "message":"Menu: \nSelect Your Choice",
            "type":"list",
            "choices":[
                "Add a book📗",
                "Remove a book📕",
                "Search for a book🔎",
                "Display all books📚",
                "Display statistics",
                "Exit"
            ],
        }
    ]
    )
    # Conditional Statements for Menu Options
    if menu_question["question1"] == "Add a book📗":
        add_book()
    elif menu_question["question1"] == "Remove a book📕":
        remove_book()
    elif menu_question["question1"] == "Search for a book🔎":
        search_book()
    elif menu_question["question1"] == "Display all books📚":
        display_all_books()
    elif menu_question["question1"] == "Display statistics":
        display_statistics()
    elif menu_question["question1"] == "Exit":
        print("Goodbye!")
# First message of APP
print("Welcome to your Personal Library📚 Manager")
menu()