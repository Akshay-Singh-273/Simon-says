#simon says
from graphics import *
from win32api import GetSystemMetrics
import random
import time

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
score = 0
center = 20
n = 0
game = True
speed = 1
rec = []
ans = []

win = GraphWin("Simon says",700,500)

class box:
    def __init__(self, center):
        self.center = center
        self.length = 25
        self.breadth = 15
    
    def rectangle(self):
        self.r = Rectangle(Point(self.center - self.length, 100 - self.breadth),Point(self.center + self.length, 100 + self.breadth))
        self.r.setFill("white")
        self.r.draw(win)

def click(center):
    j = 0
    click_point = win.getMouse()
    if (click_point.getX() < center + 25 and click_point.getX() > center - 25 and click_point.getY() < 100 + 15 and click_point.getY() > 100 - 15):
        return True
    elif (click_point.getY() > 100 + 15 or click_point.getY() < 100 - 15):
        user_input = click(center)
        return user_input
    else:
        return False

while n < 10:
    center += 60
    rec.append(box(center))
    n+=1

for obj in rec:
    obj.rectangle()

while game is True:
    i = 0
    if score <= 10:
        del ans
        ans = []
        while i <= score:
            ans.append(random.randint(0,9))
            i+=1
        for val in ans:
            rec[val].r.setFill("blue")
            time.sleep(speed)
            rec[val].r.setFill("white")
        for val in ans:
            user_input = click(rec[val].center)
            if user_input == True:
                rec[val].r.setFill("green")
                time.sleep(speed)
                rec[val].r.setFill("white")
            else:
                rec[val].r.setFill("red")
                time.sleep(speed)
                rec[val].r.setFill("white")
                game = False
                break
    score += 1
win.close()
