import random

class Cat:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
    def to_pokushal(self):
        print("Pokushal")
        self.progress += 1
        self.gladness += 1
    def to_pokakal(self):
        print("Pokakal")
        self.gladness += 3
    def to_ykral(self):
        print("Ykral kolbasy")
        self.gladness += 5
        self.progress -= 0.1
    def to_otdix(self):
        print("otdix")
        self.gladness += 100
        self.progress += 1
    def is_otdix(self):
        if self.progress <=5:
            print("zasnyl")
        elif self.gladness >=0:
            print("Ystal")
        elif self.progress > 5:
            print("lenivaya zopa")
    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")
    def live(self, day):
        day = "Day" + str(day) + "of" + self.name + "life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 4)
        if live_cube == 1:
            self.to_ykral()
        elif live_cube == 2:
            self.to_pokakal()
        elif live_cube == 3:
            self.to_otdix()
            self.end_of_day()
        elif live_cube == 4:
            self.to_pokushal()

nick = Cat(name = "Semen")
for day in range(365):
    nick.live(day)
