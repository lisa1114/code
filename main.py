import random

class student:
    def __init__(self, name, age):
        self.name = name
        self.progress = 0
        self.energy = 50
        self.age = age
        self.alive = True
        self.money = 1000

    def info(self):
        print(f"name:{self.name}, progress: {self.progress}, energy: {self.energy}, age: {self.age}, money: {self.money}")

    def sleep(self):
        print("sleeping")
        self.energy += 15

    def study(self):
        print("studing")
        self.progress += 5
        self.energy -5

    def work(self):
        print("working")
        self.money += 100
        self.energy -10
        
    def chill(self):
        print("chilling")
        self.energy += 10
        self.progress -= 5
        self.money -= 50

    def isalive(self):
        if self.energy <= 0:
            print("depresion")
            self.sleep()

        if self.progress < -30:
            print("cast out")
            self.study()

        if self.progress < 300:
            print("not work!")
            self.work()

    def life(self, day):
        print(f"day {day} of {self.name} life")

        stu_choise = random.randint(1, 4)

        if stu_choise == 1:
            self.study()

        elif stu_choise == 2:
            self.chill()

        elif stu_choise == 3:
            self.sleep()

        elif stu_choise == 4:
            self.work()

        self.isalive()
        self.info

stu = student("erica", "20")

for day in range (30):
    if stu.alive == False:
        break
    stu.life(day)

stu.info()