"""
Demonstrating composition with a Library Management System.
Shows complex relationships between Library, Books, Authors, and Members.
"""

from datetime import datetime, timedelta
from typing import List, Optional


class Author:
    """An author who writes books."""
    
    def __init__(self, name, birth_year, nationality):
        self.name = name
        self.birth_year = birth_year
        self.nationality = nationality
        self.biography = ""
        
    def set_biography(self, bio):
        """Set the author's biography."""
        self.biography = bio
        
    def __str__(self):
        """String representation of the author."""
        return f"{self.name} (b. {self.birth_year}, {self.nationality})"


class Book:
    """A book that contains reference to its author(s)."""
    
    def __init__(self, isbn, title, authors: List[Author], publication_year, genre):
        self.isbn = isbn
        self.title = title
        self.authors = authors  # Composition: Book HAS Authors
        self.publication_year = publication_year
        self.genre = genre
        self.total_copies = 1
        self.available_copies = 1
        self.times_borrowed = 0
        
    def add_copies(self, count):
        """Add more copies of the book."""
        self.total_copies += count
        self.available_copies += count
        
    def is_available(self):
        """Check if the book is available for borrowing."""
        return self.available_copies > 0
        
    def borrow(self):
        """Borrow a copy of the book."""
        if self.is_available():
            self.available_copies -= 1
            self.times_borrowed += 1
            return True
        return False
        
    def return_book(self):
        """Return a copy of the book."""
        if self.available_copies < self.total_copies:
            self.available_copies += 1
            return True
        return False
        
    def get_author_names(self):
        """Get a formatted string of all author names."""
        return ", ".join([author.name for author in self.authors])
        
    def __str__(self):
        """String representation of the book."""
        return f'"{self.title}" by {self.get_author_names()} ({self.publication_year})'


class Loan:
    """Represents a book loan transaction."""
    
    def __init__(self, book: Book, loan_date: datetime, due_days=14):
        self.book = book  # Composition: Loan HAS-A Book
        self.loan_date = loan_date
        self.due_date = loan_date + timedelta(days=due_days)
        self.return_date = None
        self.fine = 0.0
        
    def return_book(self, return_date: datetime):
        """Process book return."""
        self.return_date = return_date
        if return_date > self.due_date:
            days_overdue = (return_date - self.due_date).days
            self.fine = days_overdue * 0.50  # $0.50 per day fine
        self.book.return_book()
        
    def is_overdue(self, current_date: datetime):
        """Check if the loan is overdue."""
        return current_date > self.due_date and self.return_date is None
        
    def __str__(self):
        """String representation of the loan."""
        status = "Returned" if self.return_date else "Active"
        return f"{self.book.title} - Due: {self.due_date.strftime('%Y-%m-%d')} - Status: {status}"


class Member:
    """A library member who can borrow books."""
    
    def __init__(self, member_id, name, email, join_date: datetime):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.join_date = join_date
        self.active_loans = []  # Composition: Member HAS Loans
        self.loan_history = []
        self.total_fines = 0.0
        
    def borrow_book(self, book: Book, borrow_date: datetime):
        """Borrow a book from the library."""
        if len(self.active_loans) >= 5:
            return None, "Maximum loan limit (5 books) reached"
            
        if not book.is_available():
            return None, "Book is not available"
            
        # Check for overdue books
        overdue_books = [loan for loan in self.active_loans 
                        if loan.is_overdue(borrow_date)]
        if overdue_books:
            return None, f"Please return {len(overdue_books)} overdue book(s) first"
            
        # Create loan
        book.borrow()
        loan = Loan(book, borrow_date)
        self.active_loans.append(loan)
        return loan, "Book borrowed successfully"
        
    def return_book(self, isbn: str, return_date: datetime):
        """Return a borrowed book."""
        for loan in self.active_loans:
            if loan.book.isbn == isbn:
                loan.return_book(return_date)
                self.active_loans.remove(loan)
                self.loan_history.append(loan)
                if loan.fine > 0:
                    self.total_fines += loan.fine
                    return f"Book returned. Fine: ${loan.fine:.2f}"
                return "Book returned successfully"
        return "Book not found in active loans"
        
    def get_active_loans(self):
        """Get list of active loans."""
        return self.active_loans
        
    def __str__(self):
        """String representation of the member."""
        return f"{self.name} (ID: {self.member_id}) - Active loans: {len(self.active_loans)}"


class Catalog:
    """A catalog system for organizing books."""
    
    def __init__(self):
        self.books = {}  # ISBN -> Book mapping
        self.by_genre = {}  # Genre -> List[Book] mapping
        self.by_author = {}  # Author name -> List[Book] mapping
        
    def add_book(self, book: Book):
        """Add a book to the catalog."""
        self.books[book.isbn] = book
        
        # Update genre index
        if book.genre not in self.by_genre:
            self.by_genre[book.genre] = []
        self.by_genre[book.genre].append(book)
        
        # Update author index
        for author in book.authors:
            if author.name not in self.by_author:
                self.by_author[author.name] = []
            self.by_author[author.name].append(book)
            
    def find_by_isbn(self, isbn: str) -> Optional[Book]:
        """Find a book by ISBN."""
        return self.books.get(isbn)
        
    def find_by_title(self, title: str) -> List[Book]:
        """Find books by title (partial match)."""
        results = []
        for book in self.books.values():
            if title.lower() in book.title.lower():
                results.append(book)
        return results
        
    def find_by_author(self, author_name: str) -> List[Book]:
        """Find books by author name."""
        return self.by_author.get(author_name, [])
        
    def find_by_genre(self, genre: str) -> List[Book]:
        """Find books by genre."""
        return self.by_genre.get(genre, [])
        
    def get_popular_books(self, top_n=5):
        """Get most borrowed books."""
        sorted_books = sorted(self.books.values(), 
                            key=lambda b: b.times_borrowed, 
                            reverse=True)
        return sorted_books[:top_n]


class Library:
    """A library that manages books, members, and loans through composition."""
    
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.catalog = Catalog()  # Composition: Library HAS-A Catalog
        self.members = {}  # Member ID -> Member mapping
        self.next_member_id = 1000
        
    def add_book(self, book: Book):
        """Add a book to the library catalog."""
        self.catalog.add_book(book)
        return f"Added {book} to the library"
        
    def register_member(self, name: str, email: str) -> Member:
        """Register a new library member."""
        member_id = f"M{self.next_member_id}"
        self.next_member_id += 1
        member = Member(member_id, name, email, datetime.now())
        self.members[member_id] = member
        return member
        
    def find_member(self, member_id: str) -> Optional[Member]:
        """Find a member by ID."""
        return self.members.get(member_id)
        
    def checkout_book(self, member_id: str, isbn: str) -> tuple:
        """Process book checkout for a member."""
        member = self.find_member(member_id)
        if not member:
            return False, "Member not found"
            
        book = self.catalog.find_by_isbn(isbn)
        if not book:
            return False, "Book not found"
            
        loan, message = member.borrow_book(book, datetime.now())
        return (loan is not None), message
        
    def return_book(self, member_id: str, isbn: str) -> str:
        """Process book return."""
        member = self.find_member(member_id)
        if not member:
            return "Member not found"
            
        return member.return_book(isbn, datetime.now())
        
    def get_library_stats(self):
        """Get library statistics."""
        total_books = len(self.catalog.books)
        total_copies = sum(book.total_copies for book in self.catalog.books.values())
        available_copies = sum(book.available_copies for book in self.catalog.books.values())
        total_members = len(self.members)
        active_loans = sum(len(m.active_loans) for m in self.members.values())
        
        stats = f"=== {self.name} Statistics ===\n"
        stats += f"Location: {self.address}\n"
        stats += f"Unique Books: {total_books}\n"
        stats += f"Total Copies: {total_copies}\n"
        stats += f"Available Copies: {available_copies}\n"
        stats += f"Members: {total_members}\n"
        stats += f"Active Loans: {active_loans}\n"
        
        return stats


# Example usage
if __name__ == "__main__":
    # Create library
    city_library = Library("City Central Library", "123 Library Lane")
    
    # Create authors
    rowling = Author("J.K. Rowling", 1965, "British")
    tolkien = Author("J.R.R. Tolkien", 1892, "British")
    martin = Author("George R.R. Martin", 1948, "American")
    
    # Create books with authors (composition)
    hp1 = Book("978-0439708180", "Harry Potter and the Sorcerer's Stone", 
               [rowling], 1997, "Fantasy")
    hp1.add_copies(4)  # Add more copies
    
    lotr = Book("978-0544003415", "The Lord of the Rings", 
                [tolkien], 1954, "Fantasy")
    lotr.add_copies(2)
    
    got = Book("978-0553103540", "A Game of Thrones", 
               [martin], 1996, "Fantasy")
    
    # Add books to library
    city_library.add_book(hp1)
    city_library.add_book(lotr)
    city_library.add_book(got)
    
    # Register members
    alice = city_library.register_member("Alice Johnson", "alice@email.com")
    bob = city_library.register_member("Bob Smith", "bob@email.com")
    
    print("=== Library Composition Example ===")
    print(city_library.get_library_stats())
    
    # Members borrow books
    print("\n--- Book Checkouts ---")
    success, message = city_library.checkout_book(alice.member_id, hp1.isbn)
    print(f"Alice borrows Harry Potter: {message}")
    
    success, message = city_library.checkout_book(bob.member_id, lotr.isbn)
    print(f"Bob borrows LOTR: {message}")
    
    success, message = city_library.checkout_book(alice.member_id, got.isbn)
    print(f"Alice borrows Game of Thrones: {message}")
    
    # Show member status
    print(f"\n{alice}")
    print("Alice's active loans:")
    for loan in alice.get_active_loans():
        print(f"  - {loan}")
        
    # Search catalog
    print("\n--- Catalog Search ---")
    print("Fantasy books in library:")
    for book in city_library.catalog.find_by_genre("Fantasy"):
        availability = "Available" if book.is_available() else "Checked out"
        print(f"  - {book} [{availability}]")
        
    # Return a book
    print("\n--- Book Returns ---")
    # Simulate returning after due date
    alice.active_loans[0].due_date = datetime.now() - timedelta(days=2)
    result = city_library.return_book(alice.member_id, hp1.isbn)
    print(f"Alice returns Harry Potter: {result}")
    
    # Show popular books
    print("\n--- Most Popular Books ---")
    for i, book in enumerate(city_library.catalog.get_popular_books(3), 1):
        print(f"{i}. {book.title} - Borrowed {book.times_borrowed} times")
        
    # Final statistics
    print(f"\n{city_library.get_library_stats()}")