import turtle
import math
import time

# -------------------------------------------------
# SCREEN SETUP
# -------------------------------------------------

screen = turtle.Screen()
screen.setup(width=900, height=650)
screen.title("My Beautiful Animated House")
screen.bgcolor("#87CEEB")
screen.tracer(0)

# -------------------------------------------------
# TURTLE SETUP
# -------------------------------------------------

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)

# -------------------------------------------------
# HELPER FUNCTIONS
# -------------------------------------------------

def rectangle(x, y, width, height, color, outline="black"):
    pen.penup()
    pen.goto(x, y)
    pen.setheading(0)
    pen.pendown()

    pen.fillcolor(color)
    pen.pencolor(outline)

    pen.begin_fill()
    for _ in range(2):
        pen.forward(width)
        pen.left(90)
        pen.forward(height)
        pen.left(90)
    pen.end_fill()


def polygon(points, color, outline="black"):
    pen.penup()
    pen.goto(points[0])
    pen.pendown()

    pen.fillcolor(color)
    pen.pencolor(outline)

    pen.begin_fill()
    for point in points[1:]:
        pen.goto(point)
    pen.goto(points[0])
    pen.end_fill()


def circle(x, y, radius, color, outline=None):
    pen.penup()
    pen.goto(x, y - radius)
    pen.setheading(0)
    pen.pendown()

    pen.fillcolor(color)

    if outline:
        pen.pencolor(outline)
    else:
        pen.pencolor(color)

    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()


# -------------------------------------------------
# STATIC BACKGROUND
# -------------------------------------------------

def draw_background():

    # Sky
    rectangle(-450, -325, 900, 650, "#87CEEB", "#87CEEB")

    # Grass
    rectangle(-450, -325, 900, 105, "#7CFC70", "#7CFC70")

    # Small darker grass line
    pen.penup()
    pen.goto(-450, -220)
    pen.pendown()
    pen.pencolor("#4CAF50")
    pen.pensize(3)
    pen.forward(900)

    pen.pensize(1)

    # -------------------------------------------------
    # HOUSE BODY
    # -------------------------------------------------

    # House wall
    rectangle(-210, -220, 420, 270, "#FFE5E5")

    # Roof
    polygon(
        [
            (-240, 50),
            (0, 210),
            (240, 50)
        ],
        "#E31B23"
    )

    # Chimney
    rectangle(120, 115, 45, 95, "#A52A2A")

    # Chimney top
    rectangle(115, 205, 55, 10, "#8B1A1A")

    # -------------------------------------------------
    # WINDOWS
    # -------------------------------------------------

    # Left window
    rectangle(-170, -10, 70, 70, "#FFF200")

    # Left window frame
    pen.penup()
    pen.goto(-135, -10)
    pen.pendown()
    pen.goto(-135, 60)

    pen.penup()
    pen.goto(-170, 25)
    pen.pendown()
    pen.goto(-100, 25)

    # Right window
    rectangle(100, -10, 70, 70, "#FFF200")

    # Right window frame
    pen.penup()
    pen.goto(135, -10)
    pen.pendown()
    pen.goto(135, 60)

    pen.penup()
    pen.goto(100, 25)
    pen.pendown()
    pen.goto(170, 25)

    # -------------------------------------------------
    # DOOR
    # -------------------------------------------------

    rectangle(-45, -220, 90, 150, "#7B008B")

    # Door knob
    circle(25, -145, 5, "#FFD700")

    # -------------------------------------------------
    # PATH TO HOUSE
    # -------------------------------------------------

    polygon(
        [
            (-35, -220),
            (35, -220),
            (75, -325),
            (-75, -325)
        ],
        "#D2B48C"
    )

    # -------------------------------------------------
    # GARDEN FLOWERS
    # -------------------------------------------------

    flower_positions = [
        (-330, -285, "#FF69B4"),
        (-285, -300, "#9B00A8"),
        (-240, -280, "#FF3030"),
        (-195, -300, "#FFA500"),
        (-150, -280, "#FFFFFF")
    ]

    for x, y, color in flower_positions:

        # Stem
        pen.penup()
        pen.goto(x, -325)
        pen.pendown()
        pen.pencolor("#006400")
        pen.pensize(3)
        pen.goto(x, y)

        # Flower
        circle(x, y + 8, 7, color)

    pen.pensize(1)

    # -------------------------------------------------
    # SMALL FENCE
    # -------------------------------------------------

    # Fence behind rabbit
    for x in range(260, 410, 40):

        rectangle(x, -290, 8, 55, "#8B4513")

    rectangle(250, -265, 170, 8, "#8B4513")
    rectangle(250, -290, 170, 8, "#8B4513")


# -------------------------------------------------
# DRAW RABBIT
# -------------------------------------------------

def draw_rabbit(x, y):

    # Body
    circle(x, y, 30, "#FFFFFF", "#555555")

    # Head
    circle(x, y + 38, 23, "#FFFFFF", "#555555")

    # Ears
    pen.penup()
    pen.goto(x - 15, y + 52)
    pen.pendown()

    pen.fillcolor("#FFFFFF")
    pen.pencolor("#555555")

    pen.begin_fill()
    pen.goto(x - 20, y + 105)
    pen.goto(x - 5, y + 80)
    pen.goto(x - 15, y + 52)
    pen.end_fill()

    pen.penup()
    pen.goto(x + 5, y + 52)
    pen.pendown()

    pen.begin_fill()
    pen.goto(x + 15, y + 105)
    pen.goto(x + 25, y + 75)
    pen.goto(x + 5, y + 52)
    pen.end_fill()

    # Inner ears
    pen.pencolor("#FFB6C1")
    pen.pensize(5)

    pen.penup()
    pen.goto(x - 13, y + 65)
    pen.pendown()
    pen.goto(x - 17, y + 92)

    pen.penup()
    pen.goto(x + 12, y + 65)
    pen.pendown()
    pen.goto(x + 15, y + 92)

    pen.pensize(1)

    # Eyes
    circle(x - 8, y + 43, 3, "black")
    circle(x + 8, y + 43, 3, "black")

    # Nose
    circle(x, y + 33, 3, "#FF69B4")

    # Mouth
    pen.penup()
    pen.goto(x, y + 30)
    pen.pendown()
    pen.goto(x, y + 24)

    # Whiskers
    pen.penup()
    pen.goto(x - 4, y + 32)
    pen.pendown()
    pen.goto(x - 25, y + 37)

    pen.penup()
    pen.goto(x - 4, y + 28)
    pen.pendown()
    pen.goto(x - 25, y + 25)

    pen.penup()
    pen.goto(x + 4, y + 32)
    pen.pendown()
    pen.goto(x + 25, y + 37)

    pen.penup()
    pen.goto(x + 4, y + 28)
    pen.pendown()
    pen.goto(x + 25, y + 25)

    # Feet
    circle(x - 15, y - 25, 10, "#FFFFFF", "#555555")
    circle(x + 15, y - 25, 10, "#FFFFFF", "#555555")

    # Tail
    circle(x + 28, y - 5, 12, "#FFFFFF", "#555555")


# -------------------------------------------------
# SUN
# -------------------------------------------------

def draw_sun(x, y):

    # Sun
    circle(x, y, 42, "#FFD700")

    # Sun rays
    pen.pencolor("#FFD700")
    pen.pensize(3)

    for angle in range(0, 360, 30):

        radians = math.radians(angle)

        x1 = x + math.cos(radians) * 52
        y1 = y + math.sin(radians) * 52

        x2 = x + math.cos(radians) * 65
        y2 = y + math.sin(radians) * 65

        pen.penup()
        pen.goto(x1, y1)
        pen.pendown()
        pen.goto(x2, y2)

    pen.pensize(1)


# -------------------------------------------------
# CLOUD
# -------------------------------------------------

def draw_cloud(x, y):

    # Use several overlapping circles to make
    # one smooth-looking cloud.

    circle(x, y, 25, "white", "#D6EAF8")
    circle(x + 30, y + 10, 32, "white", "#D6EAF8")
    circle(x + 65, y, 25, "white", "#D6EAF8")
    circle(x + 35, y - 8, 28, "white", "#D6EAF8")

    # Flat bottom
    rectangle(
        x - 5,
        y - 25,
        75,
        25,
        "white",
        "#D6EAF8"
    )


# -------------------------------------------------
# ANIMATION OBJECTS
# -------------------------------------------------

sun_x = -350
sun_y = 245

cloud1_x = -400
cloud1_y = 170

cloud2_x = 150
cloud2_y = 245

# -------------------------------------------------
# MAIN ANIMATION
# -------------------------------------------------

draw_background()

while True:

    # Clear only the animated sky area
    # by redrawing the background and objects.
    draw_background()

    # Moving sun
    draw_sun(sun_x, sun_y)

    # Moving clouds
    draw_cloud(cloud1_x, cloud1_y)
    draw_cloud(cloud2_x, cloud2_y)

    # Rabbit
    draw_rabbit(300, -275)

    screen.update()

    # Move sun
    sun_x += 1.2

    if sun_x > 430:
        sun_x = -430

    # Move clouds
    cloud1_x += 1.0
    cloud2_x += 0.7

    if cloud1_x > 430:
        cloud1_x = -450

    if cloud2_x > 430:
        cloud2_x = -450

    time.sleep(0.03)