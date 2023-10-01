class intro:

    def __init__(self,name,sex,profession):
        self.name=name
        self.sex=sex
        self.profession=profession

    def show(self):
        print(f"your name is {self.name} and sex is {self.sex}")
    def work(self):
        print(f"{self.name} is working as a {self.profession}")

Rajan=intro('Rajkumar','male','teacher')

Rajan.show()
Rajan.work()
