class Computer:
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
    def config(self):
        print(self.cpu)
        print(self.ram)
com1=Computer('i5',16)
com1.config()
com2=Computer('i7',8)
com2.config()