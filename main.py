import turtle as trtl
import random as rand

def Click():
    def __init__ (self):
        self.spot_color = "pink"
        self.score = 0
        self.timer_up = False
        self.countdown_time = 30

        self.wn = trtl.Screen()

        self.spot = trtl.Turtle()
        self.spot.shape("circle")
        self.spot.shapesize(2)
        self.spot.fillcolor(self.spot_color)

        self.counter = trtl.Turtle()
        self.counter.penup()
        self.counter.goto(0, -260)  
        self.counter.hideturtle()
        self.counter.write(self.countdown_time, font=("Arial", 20, "normal"))


        self.spot.onclick(self.spot_clicked)


        self.wn.ontimer(self.countdown, 1000)  

        self.wn.mainloop()

    def changepos(self):
        self.t.goto(random.randit(-200,200),random.randit(-150,150) )
    def update(self):
        self.score += 1
        self.t.clear()
        self.t.write(score, font=("Arial", 20, "normal"))
        

    def spotclick(self, x, y):
        if not timer_up:
            self.changepos()
            self.update()

    def countdown(self):
        if self.countdown_time > 0:
            self.countdown_time -= 1
            self.counter.clear()
            self.counter.write(self.countdown_time, font=("Arial", 20, "normal"))
            self.wn.ontimer(self.countdown, 1000)  
        else:
            self.timer_up = True
            self.spot.hideturtle()  
            self.counter.clear()
            self.counter.write("Time's Up!", font=("Arial", 20, "normal"))

if __name__ == "__main__":
    game = Click()
