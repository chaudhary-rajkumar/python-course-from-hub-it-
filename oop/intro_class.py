class Person:
    
    def __init__(self,name,sex,profession):
        # data members
        self.name=name
        self.sex=sex
        self.profession=profession

    # Behavior (instance methods)
    def show(self):
        print('name:',self.name, 'sex:', self.sex, 'profession:', self.profession)
    
    def work(self):
        print(self.name, 'working as a ', self.profession)
    
# Creating object of a class 
jessa=Person('Jon','male','engineer')

# call methods
jessa.show()
jessa.work()
print(jessa.name)