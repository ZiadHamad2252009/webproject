class employee :
    def __init__(self,title,author,isbn,available):
        self .title=title
        self.author=author
        self.isbn=isbn
        self.availble=available
        def borrow_book(self):
            if self . availble:
                self . availble=False
                print(f"you have successfully borrowed'{self . title}' is currently not available.")

                def return_book (self):
                    if not self.available:
                        self.available=True
                        print(f"you have successfully  returned '{self.title}'.")
                    else:
                        print(f"'{self. title}'was not borrowed.")
