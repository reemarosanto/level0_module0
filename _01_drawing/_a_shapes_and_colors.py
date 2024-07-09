import turtle


window = turtle.Screen()
window.bgcolor('white')

# This code makes a new Turtle. Pick a new name for the turtle
my_reema = turtle.Turtle()

# Make your turtle's shape 'turtle', .shape('turtle')
my_reema.shape('turtle')
# Set your turtle's speed using .speed(2)
my_reema.speed(2)
# Set your turtle's color using .color('green') and .pencolor('blue')
my_reema.color('purple')
my_reema.pencolor('purple')
# Move your turtle forward using .forward(100)
# TEST    Did your turtle move forward?
my_reema.forward(100)
# Move your turtle left or right using .left(90) or .right(90)
my_reema.left(90)
# Now put the forward and left/right code into a for loop to repeat 4 times.
# TEST    Did your turtle draw a square?
for i in range(4):
    my_reema.forward(100)
    my_reema.left(90)
# Move your turtle to a new place on the screen using .goto(x, y)
# x=0 and y=0 is the center of the screen
my_reema.goto(30,30)
# Have your turtle draw a circle using .circle(radius, steps=30)
# TEST    Did your turtle draw a circle?
my_reema.begin_fill()
my_reema.circle(90, steps=30)
my_reema.end_fill()
# Add color to your shape by adding .begin_fill() before drawing the circle
# and .end_fill() below
my_reema.goto(90, 90)
# Draw 3 more shapes with different fill colors!
my_reema.color('green')
my_reema.begin_fill()
for i in range(4):
    my_reema.forward(100)
    my_reema.left(90)
my_reema.end_fill()
my_reema.goto(200, 200)
my_reema.color('red')
my_reema.begin_fill()
for i in range(4):
    my_reema.forward(100)
    my_reema.right(90)
    my_reema.forward(50)
my_reema.end_fill()
# ===================== DO NOT EDIT THE CODE BELOW ============================
turtle.done()
