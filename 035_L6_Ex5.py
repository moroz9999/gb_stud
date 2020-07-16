# L6. Ex.5
class Stationery:
    def __init__(self, name):
        self.name = name
    
    def draw(self):
        print("Start drawning")
    
class Pen(Stationery):
    def draw(self):
        print("It's a %s-drawing: Bzzzziiiiuu!!" % self.name)

class Pencil(Stationery):
    def draw(self):
        print("It's a %s-drawing: Fshshsh..." % self.name)

class Handle(Stationery):
    def draw(self):
        print("It's a %s-drawing: Vhhhhhiiii" % self.name)


st1 = Pen('pen')
st2 = Pencil('pencil')
st3 = Handle('handle')
for i in (st1, st2, st2):
    i.draw()
