import turtle as trtl
import random as rand


class Click:
    def __init__(self, colorlist, sizelist):
        self.spotcolor = "pink"
        self.countdown_time = 30
        self.colors = colorlist
        self.sizes = sizelist

        self.wn = trtl.Screen()
        self.wn.bgcolor("light blue")

        self.t = trtl.Turtle()
        self.t.shape("circle")
        self.t.shapesize(2)
        self.t.fillcolor(self.spotcolor)

        self.counter = trtl.Turtle()
        self.counter.penup()
        self.counter.goto(0, -260)
        self.counter.hideturtle()
        self.counter.write(self.countdown_time, font=("Arial", 20, "normal"))

        self.t.onclick(self.spotclick)

        self.wn.ontimer(self.countdown, 1000)

        self.startgame()

    def startgame(self):
         self.score = 0
         self.timerup = False
         self.wn.mainloop()

    def changepos(self):
        self.t.penup()
        self.t.goto(rand.randint(-200, 200), rand.randint(-150, 150))
        self.t.pendown()
    def changecolor(self):
        self.t.fillcolor(rand.choice(self.colors))
        self.t.stamp()
        self.t.fillcolor(self.spotcolor)
    def sizechange(self):
        self.t.shapesize(rand.choice(self.sizes))
    def update(self):
        self.score += 1
        self.t.write(self.score, font=("Arial", 20, "normal"))

    def spotclick(self, x, y):
        if not self.timerup:
            self.changepos()
            self.changecolor()
            self.sizechange()
            self.update()

    def countdown(self):
        if self.countdown_time > 0:
            self.countdown_time -= 1
            self.counter.clear()
            self.counter.write(self.countdown_time, font=("Arial", 20, "normal"))
            self.wn.ontimer(self.countdown, 1000)
        else:
            self.timerup = True
            self.t.hideturtle()
            self.counter.clear()
            self.counter.write("Time's Up!", font=("Arial", 20, "normal"))


if __name__ == "__main__":
    game = Click(colorlist=["red","blue","black","purple", "green", "grey"], sizelist=[0.5,1,1.5,2,3.5,3,3.5,4])
