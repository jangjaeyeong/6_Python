from library import library
from model import BookNotFoundError, AlreadyBorrowedError

def main():
    lib = library()

    while True:
        print("\n=== 도서관 관리 시스템 ===")
        print("1. 일반 도서 등록")
        print("2. 전자책 등록")
        print("3. 전체 도서 조회")
        print("4. 대출 가능한 도서 검색")
        print("5. 등록된 저자 목록 조회")
        print("6. 도서 삭제")
        print("7. 종료")
        
        choice = input("선택하실 메뉴 번호를 입력하세요: ")

        try:
            if choice == "1":
                isbn = input("ISBN: ")
                title = input("제목: ")
                author = input("저자: ")
                keep = input("보관 위치: ")
                lib.createPrintedBook(isbn, title, author, keep)
                print("일반 도서가 등록되었습니다.")

            elif choice == "2":
                isbn = input("ISBN: ")
                title = input("제목: ")
                author = input("저자: ")
                file_format = input("파일 포맷(예: PDF): ")
                file_mb = float(input("파일 용량(MB): "))
                lib.createEBook(isbn, title, author, file_format, file_mb)
                print("전자책이 등록되었습니다.")

            elif choice == "3":
                print("\n--- 전체 도서 목록 ---")
                lib.readBook()

            elif choice == "4":
                print("\n--- 대출 가능 도서 목록 ---")
                lib.searchAvailableBooks()

            elif choice == "5":
                lib.getUniqueAuthors()

            elif choice == "6":
                isbn = input("삭제할 도서의 ISBN: ")
                lib.deleteBook(isbn)

            elif choice == "7":
                print("프로그램을 종료합니다.")
                break
            else:
                print("잘못된 입력입니다. 1~7 사이의 숫자를 입력해주세요.")

        except (BookNotFoundError, AlreadyBorrowedError) as e:
            print(f"[오류 발생]: {e}")
        except ValueError:
            print("[오류 발생]: 잘못된 형식의 입력입니다. (숫자 입력란을 확인하세요)")

if __name__ == "__main__":
    main()