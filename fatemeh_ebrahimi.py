class Person :
    def __init__(self,name,family):
        self.name = name
        self.family = family

    def save(self):
        print(f"saving person : {self.name} - {self.family}")

person1 = Person("fatemeh","ebrahimi")
person1.save()

