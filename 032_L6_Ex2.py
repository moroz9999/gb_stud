# L6. Ex.2
"""
Class Road allow to count weight of materials to road bilding

"""
class Road():
    def setParam(self, width, length):
        self._length = length
        self._width = width
    def getWeight(self):
        self.m = self._length * self._width * 25 * 5 / 1000
    def display(self):
        print('This road weight =', "{:.1f}".format(self.m), 't')
        
        
class YourRoad(Road):
    def display(self):
        print('Your very long road weight =', "{:.1f}".format(self.m), 't')


r1 = Road()
r1.setParam(20, 5000)
r1.getWeight()
r1.display()

myLenght = input("Enter the road length im meters (or press Enter):\n")
if myLenght.isdigit():
    myWidth = input("Enter the road width in meters (or press Enter):\n")
    if myWidth.isdigit():
        r2 = YourRoad()
        r2.setParam(int(myWidth), int(myLenght))
        r2.getWeight()
        r2.display()
    else: print("if you don't want it, it's fine :)\n")
else: print("if you don't want it, it's fine :)\n")
