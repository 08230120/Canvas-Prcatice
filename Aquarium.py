
import tkinter as tk
import random
import math

# ==========================================
# 1. CREATE THE MAIN WINDOW
# ==========================================
root = tk.Tk()
root.title("Beautiful Underwater Aquarium")
root.resizable(False, False)

WIDTH = 1000
HEIGHT = 650

canvas = tk.Canvas(
    root,
    width=WIDTH,
    height=HEIGHT,
    bg="#006994",
    highlightthickness=0
)
canvas.pack()

# ==========================================
# 2. DRAW THE OCEAN BACKGROUND
# ==========================================

# Blue gradient effect
top_color = (0, 95, 155)
bottom_color = (0, 30, 65)

for y in range(HEIGHT):
    ratio = y / HEIGHT

    r = int(top_color[0] * (1-ratio)
            + bottom_color[0] * ratio)
    g = int(top_color[1] * (1-ratio)
            + bottom_color[1] * ratio)
    b = int(top_color[2] * (1-ratio)
            + bottom_color[2] * ratio)

    color = f"#{r:02x}{g:02x}{b:02x}"

    canvas.create_line(
        0, y, WIDTH, y,
        fill=color
    )

# Sunlight rays
for x in [100, 280, 470, 650, 850]:
    canvas.create_polygon(
        x, 0,
        x + 35, 0,
        x + 150, 390,
        x + 75, 390,
        fill="#167DA0",
        outline="",
        stipple="gray50"
    )

# Small distant fish silhouettes
for i in range(18):
    x = random.randint(50, WIDTH - 50)
    y = random.randint(100, 400)

    canvas.create_oval(
        x, y, x + 12, y + 5,
        fill="#17678B",
        outline=""
    )

    canvas.create_polygon(
        x, y + 2,
        x - 7, y - 3,
        x - 7, y + 7,
        fill="#17678B",
        outline=""
    )

# ==========================================
# 3. DRAW THE SEA FLOOR AND ROCKS
# ==========================================

canvas.create_polygon(
    0, 565,
    130, 535,
    240, 570,
    360, 550,
    490, 585,
    650, 550,
    800, 570,
    900, 535,
    1000, 560,
    1000, 650,
    0, 650,
    fill="#C5AE82",
    outline=""
)

# Sand texture
for i in range(180):
    x = random.randint(0, WIDTH)
    y = random.randint(570, HEIGHT)
    size = random.randint(1, 3)

    canvas.create_oval(
        x, y, x + size, y + size,
        fill=random.choice(
            ["#E8D6AD", "#A9926E", "#F1E2C3"]
        ),
        outline=""
    )

# Rocks along the bottom
rocks = [
    (20, 490, 150, 600),
    (130, 525, 245, 600),
    (350, 555, 455, 625),
    (570, 545, 690, 615),
    (780, 490, 920, 600),
    (890, 530, 1020, 620)
]

for x1, y1, x2, y2 in rocks:
    canvas.create_oval(
        x1, y1, x2, y2,
        fill=random.choice(
            ["#233F4C", "#344B55", "#40535A"]
        ),
        outline="#52727A",
        width=2
    )

    # Rock highlights
    for i in range(5):
        x = random.randint(x1 + 5, max(x1 + 5, x2 - 5))
        y = random.randint(y1 + 5, max(y1 + 5, y2 - 5))

        canvas.create_oval(
            x, y, x + 4, y + 3,
            fill="#718A89",
            outline=""
        )

# ==========================================
# 4. DRAW SEAWEED
# ==========================================

def draw_seaweed(x, base_y, height, color):
    points = []

    # Create a wavy plant using many points
    for i in range(13):
        y = base_y - i * height / 12
        wave = math.sin(i * 0.65) * 15
        points.extend([x + wave, y])

    canvas.create_line(
        *points,
        fill=color,
        width=7,
        smooth=True,
        capstyle=tk.ROUND
    )

    # Draw small leaves
    for i in range(2, 11, 2):
        px = x + math.sin(i * 0.65) * 15
        py = base_y - i * height / 12

        canvas.create_oval(
            px - 20, py - 8,
            px + 5, py + 8,
            fill=color,
            outline=""
        )

for x, height, color in [
    (45, 190, "#087F69"),
    (120, 250, "#139477"),
    (190, 160, "#086C5D"),
    (760, 220, "#087F69"),
    (850, 280, "#149477"),
    (960, 200, "#086C5D")
]:
    draw_seaweed(x, 600, height, color)

# ==========================================
# 5. DRAW COLOURFUL CORAL
# ==========================================

def draw_coral(x, y, color, size):
    # Coral branches
    canvas.create_line(
        x, y,
        x - size * 0.4, y - size,
        fill=color, width=7
    )

    canvas.create_line(
        x, y,
        x + size * 0.3, y - size * 1.2,
        fill=color, width=7
    )

    canvas.create_line(
        x - size * 0.2, y - size * 0.5,
        x - size * 0.8, y - size * 0.9,
        fill=color, width=6
    )

    canvas.create_line(
        x + size * 0.1, y - size * 0.7,
        x + size * 0.8, y - size,
        fill=color, width=6
    )

    # Rounded tips
    for dx, dy in [
        (-size * 0.4, -size),
        (size * 0.3, -size * 1.2),
        (-size * 0.8, -size * 0.9),
        (size * 0.8, -size)
    ]:
        canvas.create_oval(
            x + dx - 5, y + dy - 5,
            x + dx + 5, y + dy + 5,
            fill=color,
            outline=""
        )

draw_coral(100, 600, "#F08A65", 35)
draw_coral(220, 610, "#E99ACB", 30)
draw_coral(690, 610, "#E58B6D", 35)
draw_coral(930, 610, "#D78DCB", 30)

# ==========================================
# 6. DRAW A TREASURE CHEST
# ==========================================

# Chest body
canvas.create_rectangle(
    810, 545, 930, 610,
    fill="#70452D",
    outline="#C69A46",
    width=4
)

# Chest lid
canvas.create_arc(
    810, 510, 930, 575,
    start=0, extent=180,
    fill="#986338",
    outline="#D6AD53",
    width=4
)

# Gold bands
canvas.create_rectangle(
    835, 545, 847, 610,
    fill="#D7AF43",
    outline=""
)

canvas.create_rectangle(
    895, 545, 907, 610,
    fill="#D7AF43",
    outline=""
)

# Lock
canvas.create_rectangle(
    862, 568, 880, 590,
    fill="#F4CF54",
    outline="#A87525",
    width=2
)

canvas.create_oval(
    869, 574, 874, 580,
    fill="#62452B",
    outline=""
)

# Gold coins
for i in range(10):
    x = random.randint(825, 920)
    y = random.randint(535, 550)

    canvas.create_oval(
        x, y, x + 10, y + 5,
        fill="#FFD94D",
        outline="#C99A26"
    )

# ==========================================
# 7. FISH DRAWING FUNCTION
# ==========================================

def draw_fish(x, y, size, color, stripe_color, tag):
    # Tail fin
    canvas.create_polygon(
        x, y,
        x - size * 0.38, y - size * 0.30,
        x - size * 0.38, y + size * 0.30,
        fill=color,
        outline="#D5F4FF",
        width=2,
        tags=tag
    )

    # Main body
    canvas.create_oval(
        x, y - size * 0.34,
        x + size, y + size * 0.34,
        fill=color,
        outline="#D5F4FF",
        width=2,
        tags=tag
    )

    # Decorative stripes
    for position in [0.30, 0.52]:
        sx = x + size * position

        canvas.create_polygon(
            sx, y - size * 0.27,
            sx + size * 0.12, y - size * 0.22,
            sx + size * 0.12, y + size * 0.22,
            sx, y + size * 0.27,
            fill=stripe_color,
            outline="",
            tags=tag
        )

    # Top fin
    canvas.create_polygon(
        x + size * 0.30, y - size * 0.30,
        x + size * 0.48, y - size * 0.58,
        x + size * 0.70, y - size * 0.28,
        fill=color,
        outline="#D5F4FF",
        tags=tag
    )

    # Bottom fin
    canvas.create_polygon(
        x + size * 0.35, y + size * 0.25,
        x + size * 0.52, y + size * 0.48,
        x + size * 0.65, y + size * 0.27,
        fill=color,
        outline="#D5F4FF",
        tags=tag
    )

    # Eye white
    canvas.create_oval(
        x + size * 0.77, y - size * 0.16,
        x + size * 0.91, y - size * 0.02,
        fill="white",
        outline="#173D52",
        width=1,
        tags=tag
    )

    # Eye pupil
    canvas.create_oval(
        x + size * 0.83, y - size * 0.13,
        x + size * 0.89, y - size * 0.05,
        fill="#101820",
        outline="",
        tags=tag
    )

    # Small mouth
    canvas.create_line(
        x + size * 0.94, y + size * 0.05,
        x + size * 0.99, y + size * 0.07,
        fill="#173D52",
        width=2,
        tags=tag
    )

# ==========================================
# 8. CREATE MULTIPLE FISH
# ==========================================

fish_data = [
    {
        "x": 100, "y": 190, "size": 105,
        "color": "#F47721", "stripe": "white",
        "speed": 2.5, "tag": "fish1"
    },
    {
        "x": 400, "y": 330, "size": 75,
        "color": "#FFD52A", "stripe": "#F7F0B1",
        "speed": 2.0, "tag": "fish2"
    },
    {
        "x": 200, "y": 420, "size": 95,
        "color": "#1678F2", "stripe": "#40B9FF",
        "speed": 6.5, "tag": "fish3"
    },
    {
        "x": 650, "y": 230, "size": 65,
        "color": "#FF6C70", "stripe": "#FFE3E3",
        "speed": 3.0, "tag": "fish4"
    },
    {
        "x": 720, "y": 390, "size": 85,
        "color": "#9B64D9", "stripe": "#E5B8FF",
        "speed": 1.5, "tag": "fish5"
    }
]

for fish in fish_data:
    draw_fish(
        fish["x"],
        fish["y"],
        fish["size"],
        fish["color"],
        fish["stripe"],
        fish["tag"]
    )

# ==========================================
# 9. CREATE RISING BUBBLES
# ==========================================

bubbles = []

for i in range(35):
    x = random.randint(10, WIDTH - 10)
    y = random.randint(0, HEIGHT)
    radius = random.randint(3, 10)
    speed = random.uniform(1.0, 3.0)

    bubble_id = canvas.create_oval(
        x - radius, y - radius,
        x + radius, y + radius,
        fill="#72DDF5",
        outline="#D5FAFF",
        width=2
    )

    # Bubble highlight
    highlight = canvas.create_oval(
        x - radius * 0.5,
        y - radius * 0.6,
        x - radius * 0.1,
        y - radius * 0.2,
        fill="white",
        outline=""
    )

    bubbles.append({
        "id": bubble_id,
        "highlight": highlight,
        "radius": radius,
        "speed": speed,
        "drift": random.uniform(-0.4, 0.4)
    })

# ==========================================
# 10. ANIMATE THE AQUARIUM
# ==========================================

frame = 0

def animate():
    global frame
    frame += 1

    # Animate fish
    for fish in fish_data:
        tag = fish["tag"]

        # Move horizontally at the fish's own speed
        canvas.move(tag, fish["speed"], 0)

        bounds = canvas.bbox(tag)

        # Restart the fish on the left after it exits
        if bounds and bounds[0] > WIDTH:
            canvas.move(
                tag,
                -WIDTH - bounds[2] - 10,
                0
            )

    # Animate rising bubbles
    for bubble in bubbles:
        bubble_id = bubble["id"]
        highlight = bubble["highlight"]

        # Move bubble upward
        canvas.move(
            bubble_id,
            bubble["drift"],
            -bubble["speed"]
        )

        # Move its highlight with it
        canvas.move(
            highlight,
            bubble["drift"],
            -bubble["speed"]
        )

        bounds = canvas.bbox(bubble_id)

        # Restart bubble at the bottom
        if bounds and bounds[3] < 0:
            x = random.randint(10, WIDTH - 10)
            y = HEIGHT + random.randint(5, 100)
            r = bubble["radius"]

            canvas.coords(
                bubble_id,
                x - r, y - r,
                x + r, y + r
            )

            canvas.coords(
                highlight,
                x - r * 0.5,
                y - r * 0.6,
                x - r * 0.1,
                y - r * 0.2
            )

    # Repeat after 30 milliseconds
    root.after(30, animate)

# ==========================================
# 11. START THE ANIMATION
# ==========================================

animate()
root.mainloop()
