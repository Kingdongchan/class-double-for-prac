class book:
    def __init__ (self, title, author):
        self.book_title = title
        self.book_author = author

    def __str__(self):
        
        return f"이 책의 제목은 {self.book_title}이고, 저자는 {self.book_author}입니다."
    
first_book = book("아프니까 청춘이다.", "김난도")
second_book = book("나는 내일, 어제의 너와 만난드", "나나츠키 타카후미")
third_book = book("성경", "하느님")