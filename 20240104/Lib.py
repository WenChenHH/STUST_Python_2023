import datetime


class Lib:
    def __init__(self):
        self.bookname=[]
        self.id=[]
        self.year=[]
        self.author=[]
        self.state=True
        self.time=None
    
    def add_book(self,book_name,book_id,book_year,book_author):
        if book_name not in self.bookname:
            self.bookname.append(book_name)
            self.id.append(book_id)
            self.year.append(book_year)
            self.author.append(book_author)
            print(f"書籍{book_name},已成功添加入圖書館中")
        else:
            print(f"{book_name}已經存在")
    
    def print_library_info(self):
        print("書本信息:")
        for i in range(len(self.bookname)):
            print(f"書名: {self.bookname[i]}, 書本編號: {self.id[i]}, 出版年份: {self.year[i]}, 作者: {self.author[i]}")
        print(f"圖書館狀態: {self.state}")

    def borrow_book(self,book_name):
        if  self.state:
            self.state=False
            self.time=datetime.datetime.now()
            print(f"書籍{book_name}已借出")
        else:
            print("已被借出")

    def return_book(self,book_name):
        if not self.state:
            self.state=True
            return_time=datetime.datetime.now()
            print(f"{book_name}已歸還,歸還時間{return_time}")
    
    def query_book_status(self, book_name):
        if book_name in self.bookname:
            status = "已借出" if not self.state else "在圖書館中"
            print(f"書籍 {book_name} 的狀態: {status}")
        else:
            print(f"找不到書籍 {book_name}")



lib=Lib()

book1=("abc", "P001", 2020, "John Doe")
book2=("Data Science Basics", "D001", 2021, "Jane Smith")
# 添加图书到图书馆
lib.add_book(*book1)
lib.add_book(*book2)
lib.print_library_info()

lib.borrow_book("abc")
lib.query_book_status("abc")
lib.return_book("abc")

lib.query_book_status("Python Programming")
lib.query_book_status("abc")

    