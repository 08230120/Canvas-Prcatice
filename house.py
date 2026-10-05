import turtle

t = turtle.Turtle()
t.speed(5)

# Function to draw a shape
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


# HOUSE WALL
draw("lightblue", [
    (-150, -100),
    (150, -100),
    (150, 100),
    (-150, 100)
])

# ROOF
draw("red", [
    (-180, 100),
    (0, 220),
    (180, 100)
])

# LEFT WINDOW
draw("yellow", [
    (-120, 30),
    (-70, 30),
    (-70, 80),
    (-120, 80)
])

# RIGHT WINDOW
draw("yellow", [
    (70, 30),
    (120, 30),
    (120, 80),
    (70, 80)
])

# DOOR
draw("pink", [
    (-40, -100),
    (40, -100),
    (40, 20),
    (-40, 20)
])

t.hideturtle()
turtle.done()