from model import PrintedBook, EBook, BookNotFoundError

class library:
    # 생성자 / 등록된 도서는 dict로 관리
    def __init__(self):
        self.books = {} 
    
    # 일반도서 등록
    def createPrintedBook(self, isbn, title, author, keep) :
        printedBook = PrintedBook(isbn, title, author, keep)
        self.books[isbn] = printedBook

    
    def createEBook(self, isbn, title, author, fileFormat, fileMB) :
        ebook = EBook(isbn, title, author, fileFormat, fileMB)
        self.books[isbn] = ebook
    
    # 전체 도서 목록 조회
    def readBook(self, isbn = None) :
        if isbn is None:
            for book in self.books.values():
                print(book)
        else:
            if isbn in self.books:
                print(self.books[isbn])
            else:
                raise BookNotFoundError(f"ISBN '{isbn}'에 해당하는 도서가 없습니다.")    
    
    # 일반 도서 수정, none값이 들어오면 기존 값 유지
    def updatePrintedBook(self, isbn, title=None, author=None, keep=None):
        if isbn not in self.books:
            raise BookNotFoundError(f"ISBN '{isbn}'에 해당하는 도서가 없습니다.")
        
        book = self.books[isbn]
        if title: book.title = title
        if author: book.author = author
        if keep: book.keep = keep 
        
    #  전자 도서 수정 
    def updateEBook(self, isbn, title=None, author=None, fileFormat=None, fileMB=None):
        if isbn not in self.books:
            raise BookNotFoundError(f"ISBN '{isbn}'에 해당하는 도서가 없습니다.")
            
        book = self.books[isbn]
        if title: book.title = title
        if author: book.author = author
        if fileFormat: book.fileFormat = fileFormat 
        if fileMB: book.fileMB = fileMB
    
    # 대출 가능한 도서 리스트
    def searchAvailableBooks(self):
        available_books = [book for book in self.books.values() if not book.Loan_status]
        if not available_books:
            print("대출 가능한 도서가 없습니다.")
        for book in available_books:
            print(book)
    
    # 저자 목록 (중복x)
    def getUniqueAuthors(self):
        authors = {book.author for book in self.books.values()}
        if not authors:
            print("등록된 저자가 없습니다.")
        else:
            print("--- 등록된 저자 목록 ---")
            for author in authors:
                print(f"- {author}")
                
    # 도서 삭제
    def deleteBook(self, isbn):
        if isbn in self.books :
            del self.books[isbn]
            print(f"isbn : {isbn} 도서가 삭제되었습니다.")
        else :
            raise BookNotFoundError(f"존재하지 않는 ISBN입니다: {isbn}")
    
    
