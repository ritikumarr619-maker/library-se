class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book_id, title, author):
        if book_id in self.books:
            raise ValueError("Duplicate book ID")
        self.books[book_id] = {
            "title": title,
            "author": author,
            "borrowed": False
        }
    def borrow_book(self, book_id):
        if self.books[book_id]["borrowed"]:
            raise ValueError("Book already borrowed")
        self.books[book_id]["borrowed"] = True

    def return_book(self, book_id):
        self.books[book_id]["borrowed"] = False
    def generate_report(self):
        report = ["ID | Title | Author | Status"]
        for book_id, info in self.books.items():
            status = "Borrowed" if info["borrowed"] else "Available"
            report.append(f"{book_id} | {info['title']} | {info['author']} | {status}")
        return report
