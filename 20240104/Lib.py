class lib:
    def __init__(self,state):
        self.bookname={}
        self.id={}
        self.year={}
        self.author={}
        self.state=state
    
    def add_bookname(self,book_name,book_id,book_year,book_author):
        if book_name not in self.bookname:
            self.bookname.append(book_name)
            self.id.append(book_id)
            self.year.append(book_year)
            self.author.append(book_author)
            print(f"書籍{book_name},已成功添加入圖書館中")
        else:
            print(f"{book_name}已經存在")
          


# 使用示例
library =lib(open)

# 添加图书到图书馆
library.add_book("Python Programming", "P001", 2020, "John Doe")
library.add_book("Data Science Basics", "D001", 2021, "Jane Smith")

        
        
    