# L6. Ex.4
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Hey! My name is %s and i'm driving!!! Yeah! " \
        "my color is %s and i like it!" % (self.name, self.color))
    def stop(self):
        print("O, no! Stoping... Zzzz...")
    def turn(self, direction):
        self.direction = direction
        print("I'm turn", self.direction)
    def show_speed(self):
        print("My current speed: %s km/h, it's cool!" % self.speed)
        
class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print("Hmm... My current speed is too fast and I must go slower:(")
        else:
            print("My current speed: %s km/h" % self.speed)
class SportCar(Car):
    pass
class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print("Hmm... My current speed is too fast and I must go slower:(")
        else:
            print("My current speed: %s km/h" % self.speed)
class PoliceCar(Car):
    pass

car1 = SportCar(130, 'blue', 'McMissle', False)
car1.go()
car1.turn('left')
car1.show_speed()
car1.stop()
