from tkinter import *
import math

class light():
    def __init__(self,start):
        self.start=start


    def move(self):
        self.start[0] +=1
        self.start[1] -=1


class window():
    def __init__(self):
        self.root=Tk()
        self.root.geometry("800x800")
        self.root.title("Hallo") 
        self.canvas= Canvas(
            width=800,
            height=800,
        )
        self.canvas.pack()
        self.root.mainloop()

    def light(self,light):
        self.canvas.create_oval(light[0],light[1]+20,light[0]+20,light[1], width=3)
        


test = light([0,0])
wind=window()
print(test.start)
wind.light(test.start)
test.move()
wind.light(test.start)
for i in range(0,400):
    test.move()
    wind.light(test.start)

print(test.start)

wind.light(test.start)