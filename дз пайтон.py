class Emplooye():
    def __init__(self, name):
        self.name = name
        self.salary = 50000
    def describe(self):
        print(f"name: {self.name}, salary: {self.salary}")

class Manager(Emplooye):
    def __init__(self, name,department):
        super().__init__(name)
        self.department = department
    def describe(self):
        print(f"name: {self.name}, salary: {self.salary}, department: {self.department}")

class Developer(Emplooye):
    def __init__(self, name, programming_language):
        super().__init__(name)
        self.programming_language = programming_language
    def describe(self):
        print(f"name: {self.name}, salary: {self.salary}, programming_language: {self.programming_language}")


m1 = Manager("kain","legal department")
m2 =Manager("heyden","personnel management")
m3 =Manager("robert","accounting")
d1 =Developer("eva","c++")
d2 =Developer("lia","java")
d3 =Developer("sem","python")

m1.describe()
m2.describe()
m3.describe()
d1.describe()
d2.describe()
d3.describe()
    