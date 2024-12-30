class Publisher:
    def __init__(self,name):
        self.name=name
    def display(self):
        print(self.name)
class Book(Publisher):
    def __init__(self,name,title,author):
        super().__init__(name)
        self.title=title
        self.author=author
        def display(self):
            super().display()
            print(self.title)
            print(self.author)
class Python(Book):
    def