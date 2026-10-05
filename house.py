import turtle

t = turtle.Turtle()
t.speed(0)

# Function to draw a filled shape
def draw(color, points):
    t.penup()
    t.goto(points[0])
    t.pendown()

    t.fillcolor(color)
    t.begin_fill()

    for point in points[1:]:
        t.goto(point)

    t.goto(points[0])
    t.end_fill()


# ================= MAIN HOUSE =================

# House wall
draw("lightblue", [
    (-200, -150),
    (200, -150),
    (200, 100),
    (-200, 100)
])

# Roof
draw("red", [
    (-230, 100),
    (0, 250),
    (230, 100)
])


# ================= WINDOWS =================

# Left window
draw("yellow", [
    (-160, 20),
    (-90, 20),
    (-90, 80),
    (-160, 80)
])

# Right window
draw("yellow", [
    (90, 20),
    (160, 20),
    (160, 80),
    (90, 80)
])


# ================= DOOR =================

draw("pink", [
    (-45, -150),
    (45, -150),
    (45, 20),
    (-45, 20)
])


# ================= SUN =================

t.penup()
t.goto(280, 180)
t.setheading(0)
t.pendown()

t.fillcolor("yellow")
t.begin_fill()
t.circle(45)
t.end_fill()

# Sun rays
for i in range(8):
    t.penup()
    t.goto(280, 225)
    t.setheading(i * 45)
    t.forward(60)
    t.pendown()
    t.forward(25)


# ================= DOG HOUSE =================

# Dog house body
draw("orange", [
    (220, -150),
    (360, -150),
    (360, -50),
    (220, -50)
])

# Dog house roof
draw("brown", [
    (200, -50),
    (290, 30),
    (380, -50)
])

# Dog house door
draw("black", [
    (255, -150),
    (325, -150),
    (325, -100),
    (315, -80),
    (300, -70),
    (280, -70),
    (265, -80),
    (255, -100)
])


# ================= GRASS =================

t.penup()
t.goto(-400, -155)
t.setheading(0)
t.pendown()

t.pensize(2)

for i in range(20):
    t.forward(15)
    t.left(90)
    t.forward(8)
    t.backward(8)
    t.right(90)


# ================= FINISH =================

t.hideturtle()
turtle.done()