import turtle
import random

class draw_ball_n_digit:
    def __init__(self, my_turtle, color):
        turtle.speed(0)
        turtle.tracer(0)
        turtle.hideturtle()
        turtle.colormode(255)
        
        my_turtle.color(color)
        my_turtle.penup()
        my_turtle.setheading(0)
        my_turtle.goto(0, 0)
        my_turtle.pensize(10)
        
    def draw(color, size, x, y):
        turtle.penup()
        turtle.color(color)
        turtle.fillcolor(color)
        turtle.goto(x,y-size)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(size)
        turtle.end_fill()
        
    def move_ball(i, xpos, ypos, vx, vy, dt):
        xpos[i] += vx[i]*dt
        ypos[i] += vy[i]*dt
        
    def update_ball_velocity(i, xpos, ypos, vx, vy, canvas_width, canvas_height, ball_radius):
        if abs(xpos[i]) > (canvas_width - ball_radius):
            vx[i] = -vx[i]
        # if the ball hits the ceiling or the floor, reverse the vy velocity
        if abs(ypos[i]) > (canvas_height - ball_radius):
            vy[i] = -vy[i]
            
    def d_draw(self, digit, my_turtle):
        if digit == 0:
            my_turtle.goto(-50, 100)
            my_turtle.pendown()
            my_turtle.forward(100)
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.forward(100)
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.forward(100)
            my_turtle.right(90)
            my_turtle.penup()

        if digit == 1:
            my_turtle.goto(50, 100)
            my_turtle.pendown()
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.forward(100)
            my_turtle.left(90)
            my_turtle.penup()

        if digit == 2:
            my_turtle.goto(-50, 100)
            my_turtle.pendown()
            my_turtle.forward(100)
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.left(90)
            my_turtle.forward(100)
            my_turtle.left(90)
            my_turtle.forward(100)
            my_turtle.penup()

        if digit == 3:
            my_turtle.goto(-50, 100)
            my_turtle.pendown()
            my_turtle.forward(100)
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.forward(-100)
            my_turtle.left(90)
            my_turtle.forward(100)
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.left(90)
            my_turtle.left(90)
            my_turtle.penup()

        if digit == 4:
            my_turtle.goto(-50, 100)
            my_turtle.pendown()
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.left(90)
            my_turtle.forward(100)
            my_turtle.left(90)
            my_turtle.forward(100)
            my_turtle.forward(-100)
            my_turtle.forward(-100)
            my_turtle.right(90)
            my_turtle.penup()

        if digit == 5:
            my_turtle.goto(-50, 100)
            my_turtle.pendown()
            my_turtle.forward(100)
            my_turtle.forward(-100)
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.left(90)
            my_turtle.forward(100)
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.left(90)
            my_turtle.left(90)
            my_turtle.penup()

        if digit == 6:
            self.d_draw(my_turtle, 5)
            my_turtle.goto(-50, 0)
            my_turtle.pendown()
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.left(90)
            my_turtle.penup()
        
        if digit == 7:
            my_turtle.goto(-50, 100)
            my_turtle.pendown()
            my_turtle.forward(100)
            my_turtle.forward(-100)
            self.d_draw(my_turtle, 1)

        if digit == 8:
            self.d_draw(my_turtle, 0)
            my_turtle.goto(-50, 0)
            my_turtle.pendown()
            my_turtle.forward(100)
            my_turtle.penup()

        if digit == 9:
            self.d_draw(my_turtle, 5)
            my_turtle.goto(50, 100)
            my_turtle.pendown()
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.left(90)
            my_turtle.penup()
            
class run_ball(draw_ball_n_digit):
    def __init__(self):
        self.num_balls = 5
        turtle.speed(0)
        turtle.tracer(0)
        turtle.hideturtle()
        self.canvas_width = turtle.screensize()[0]
        self.canvas_height = turtle.screensize()[1]
        print(self.canvas_width, self.canvas_height)
        self.ball_radius = 0.05 * self.canvas_width
        turtle.colormode(255)
        self.xpos = []
        self.ypos = []
        self.vx = []
        self.vy = []
        self.ball_color = []
        for i in range(self.num_balls):
            self.xpos.append(random.uniform(-1*self.canvas_width + self.ball_radius, self.canvas_width - self.ball_radius))
            self.ypos.append(random.uniform(-1*self.canvas_height + self.ball_radius, self.canvas_height - self.ball_radius))
            self.vx.append(10*random.uniform(-1.0, 1.0))
            self.vy.append(10*random.uniform(-1.0, 1.0))
            self.ball_color.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        self.Tom = turtle.Turtle()
        self.tom_color = (255, 0, 0)
        draw_ball_n_digit(self.Tom, self.tom_color)
        self.delay_in_seconds = 0.2
        
    def draw_border(self):
        turtle.penup()
        turtle.goto(-self.canvas_width, -self.canvas_height)
        turtle.pensize(10)
        turtle.pendown()
        turtle.color((0, 0, 0))
        for i in range(2):
            turtle.forward(2*self.canvas_width)
            turtle.left(90)
            turtle.forward(2*self.canvas_height)
            turtle.left(90)
                
    def clear(self, my_turtle):
        my_turtle.clear()
        
    def my_delay(self, dt):
        import time
        start =  time.time()
        while time.time() - start < dt:
            pass
    
    def run(self):
        dt = 0.2
        while True:
            turtle.clear()
            self.draw_border()
            #for i in range(self.num_balls):
            #    draw_ball_n_digit.draw(color = self.ball_color[i], size = self.ball_radius, x = self.xpos[i], y = self.ypos[i])
            #    draw_ball_n_digit.move_ball(i, self.xpos, self.ypos, self.vx, self.vy, dt)
            #    draw_ball_n_digit.update_ball_velocity(i, self.xpos, self.ypos, self.vx, self.vy, self.canvas_width, self.canvas_height, self.ball_radius)
            for i in range(0, 10):
                self.clear(self.Tom)
                draw_ball_n_digit.d_draw(digit = self.Tom, my_turtle = i)
                self.my_delay(self.delay_in_seconds)
            turtle.update()
            turtle.done
            
amongus = run_ball()
amongus.run()