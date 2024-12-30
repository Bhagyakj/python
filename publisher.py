class Publisher:
    def __init__(self,name):
        self.name=name
    def display(self):
        print("publisher:",self.name)
class Book(Publisher):
    def __init__(self,name,title,auther):
        super().__init__(name)
        self.title=title
        self.auther=auther
    def display(self):
        super().display()
        print("title:",self.title)
        print("auther:",self.auther)
class Python(Book):
    def __init__(self,name,title,auther,price,noofpages):
        super().__init__(name,title,auther)
        self.price=price
        self.noofpages=noofpages
    def display(self):
        super().display()
        print("price:",self.price)
        print("no of pages:",self.noofpages)
p1=Python("DC Books","Agnichirakukal","APJ Abdul kalam",350,500)
p1.display()

