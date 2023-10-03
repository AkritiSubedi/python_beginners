class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self):
        print("move")

    def draw(self):
        print("draw")

point1 = Point(10, 20)

print(point1.x)
print(point1.y)


class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")

Akriti = Person("Akriti Subedi")
Akriti.talk()

bob = Person("Bob")
bob.talk()
