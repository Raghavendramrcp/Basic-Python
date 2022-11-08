class Family:

    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def father(self):
        print(self.name)
        print(self.age)
        print(self.height)
        print(self.weight)

f = Family("Ramana", 55, 160, 60)
f.father()