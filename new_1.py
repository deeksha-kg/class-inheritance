class Pet:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(f"my name is {self.name} my age is {self.age}")
class Cat(Pet):
    def __init__(self,name,age,color):
        super().__init__(name,age)
        self.color=color
    def show(self):
        print(f"my name is {self.name} my age is {self.age} my color is {self.color}")
    def speak(self):
        print("meow")
class Dog(Pet):
    def speak(self):
        print("bark")

# p=Pet("dee",19)
# p.show()
cat=Cat("amu",19,"white")
cat.show()
# dog=Dog("pundi",19)
# dog.show()
