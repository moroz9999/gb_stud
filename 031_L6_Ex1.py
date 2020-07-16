# L6. Ex.1
from itertools import cycle
from time import sleep

class TrafLight:
    color = (('red', 7), ('yellow', 2), ('green', 9), ('yellow', 2))
    def running(self):
        j = 0
        for i in cycle(self.color):
            print("Now is %s" %i[0])
            sleep(i[1])
            if j == 10:
                print('End of demo. Donate please for more :)')
                break
            j += 1

    
ryg = TrafLight()
ryg.running()