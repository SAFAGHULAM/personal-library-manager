import json  # For file handling
import os  # For file handling

# Initializing a Library (a list of dictionaries)
library = []

# Function to display the menu
def menu():
    print("\nWelcome to your PERSONAL LIBRARY MANAGER!")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Search for a book")
    print("4. Display all books")
    print("5. Display Statistics")
    print("6. Exit")

# Function to handle the user's choice
def choice():
    while True:
        menu()
        user_choice = input("Enter your choice: ")

        if user_choice == '1':
            add_book()
        elif user_choice == '2':
            remove_book()  # Placeholder for future implementation
        elif user_choice == '3':
            search_book()  # Placeholder for future implementation
        elif user_choice == '4':
            display_books()  # Placeholder for future implementation
        elif user_choice == '5':
            display_statistics()  # Placeholder for future implementation
        elif user_choice == '6':
            save_library()  # Save before exiting
            print("Library saved to file. Goodbye!")
            break  # Exit the loop
        else:
            print("Invalid choice. Please try again.")

# Function to add a book
def add_book():
    title = input("Enter the title of the book: ").strip()
    author = input("Enter the author of the book: ").strip()
    
    while True:
        try:
            year = int(input("Enter the year of publication: "))
            break
        except ValueError:
            print("Invalid year. Please try again.")
            
    genre = input("Enter the genre of the book: ").strip()
    read_status = input("Have you read this book? (yes/no): ").strip().lower()
    
    # Convert read_status to boolean
    read_status = True if read_status == 'yes' else False
    
    # Create a dictionary for the book
    book = {
        'title': title,
        'author': author,
        'year': year,
        'genre': genre,
        'read_status': read_status
    }

    # Add the book to the library
    library.append(book)
    print(f"\n✅ '{title}' by {author} added successfully!\n")

# Function to save the library to a file
def save_library():
    with open("library.json", "w") as file:
        json.dump(library, file, indent=4)

def remove_book():
    if not library:
        print("\n📚 Library is empty. Nothing to remove.")
        return

    title = input("\nEnter the title of the book you want to remove: ").strip()

    for index, book in enumerate(library):
        if book['title'].lower() == title.lower():
            del library[index]  # Remove the book safely
            print(f"\n❌ '{title}' removed successfully!\n")
            return

    print(f"\n❌ '{title}' not found in the library.")
    
def search_book():
    if not library:
        print("\n📚 Library is empty. Nothing to search.")
        return
        
    print("\nSearch by:") 
    print("1. Title")
    print("2. Author")
    search_choice = input("Enter your choice(1/2): ")
        
    if search_choice == '1':
        search_key = 'title'
        search_term = input("Enter the book title: ").strip().lower()
    elif search_choice == '2':
        search_key = 'author'
        search_term = input("Enter the author's name: ").strip().lower()
    else:
        print("\n❌ Invalid choice. Please enter 1 or 2.")
        return
    
    # Find books that match the search
    matches = [book for book in library if book[search_key].lower() == search_term]

    # Display results
    if matches:
        print("\n📖 Matching Books:")
        for book in matches:
            read_status = "Read ✅" if book['read_status'] else "Unread ❌"
            print(f"📚 {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")
    else:
        print(f"\n❌ No books found with {search_key}: '{search_term}'.")
        
def display_books():
    if not library:
        print("\n📚 Library is empty...First add some books!")
        return
    
    print("\n Your Library collection:\n" + "-"*40)
    for index, book in enumerate(library, start=1):
        read_status = "Read ✅ " if book['read_status'] else "Unread ❌"
        print(f"{index}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")
        
    print("-"*40)
    
def display_statistics():
    total_books = len(library)
    
    if total_books == 0:
        print("\n📚 No books in the library yet. Add some books first!")
        return
    
    read_books = len([book for book in library if book['read_status']])
    unread_books = total_books - read_books
    percentage_read = (read_books / total_books) * 100
    
    print("\n📊 Library Statistics:\n" + "-"*40)
    print(f"📚 Total Books: {total_books}")
    print(f"📖 Books Read: {read_books}")
    print(f"📕 Books Unread: {unread_books}")
    print(f"📗 Percentage Read: {percentage_read:.2f}%")
    print("-"*40)
    
def load_library():
    global library    
    if os.path.exists("library.json"):
        with open("library.json", "r") as file:
            library = json.load(file)
        print("📚 Library loaded successfully!\n")
    else:
        print("⚠ No library found. Starting with an empty library.\n")

def save_library():
    with open("library.json", "w") as file:
        json.dump(library, file, indent=4)
    print("✅ Library successfully saved to file.")

load_library()

if __name__ == "__main__":
    choice()
