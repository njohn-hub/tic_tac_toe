import turtle


# ============================================================
# CONFIGURATION
# ============================================================

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700

BOARD_SIZE = 8
SQUARE_SIZE = 60

LIGHT_COLOR = "#F0D9B5"
DARK_COLOR = "#B58863"

BACKGROUND_COLOR = "#1E293B"

DRAW_SPEED = 0


# ============================================================
# SCREEN SETUP
# ============================================================

screen = turtle.Screen()

screen.setup(
    width=SCREEN_WIDTH,
    height=SCREEN_HEIGHT
)

screen.title("Chessboard - Python Turtle")
screen.bgcolor(BACKGROUND_COLOR)

# Disable automatic animation
screen.tracer(False)


# ============================================================
# TURTLE SETUP
# ============================================================

pen = turtle.Turtle()

pen.hideturtle()
pen.speed(DRAW_SPEED)
pen.penup()


# ============================================================
# DRAW SINGLE SQUARE
# ============================================================

def draw_square(x, y, color):
    """
    Draw and fill one chessboard square.

    Parameters:
        x: X coordinate
        y: Y coordinate
        color: Square color
    """

    pen.goto(x, y)

    pen.setheading(0)

    pen.color(color)
    pen.fillcolor(color)

    pen.pendown()

    pen.begin_fill()

    for _ in range(4):
        pen.forward(SQUARE_SIZE)
        pen.left(90)

    pen.end_fill()

    pen.penup()


# ============================================================
# DRAW CHESSBOARD
# ============================================================

def draw_board():
    """Draw the complete chessboard."""

    board_width = BOARD_SIZE * SQUARE_SIZE

    start_x = -board_width / 2
    start_y = -board_width / 2

    for row in range(BOARD_SIZE):

        for column in range(BOARD_SIZE):

            x = start_x + (
                column * SQUARE_SIZE
            )

            y = start_y + (
                row * SQUARE_SIZE
            )

            # Alternate colors
            if (row + column) % 2 == 0:
                color = LIGHT_COLOR
            else:
                color = DARK_COLOR

            draw_square(
                x,
                y,
                color
            )


# ============================================================
# DRAW BOARD BORDER
# ============================================================

def draw_border():
    """Draw a border around the chessboard."""

    board_width = BOARD_SIZE * SQUARE_SIZE

    start_x = -board_width / 2
    start_y = -board_width / 2

    pen.goto(start_x, start_y)

    pen.setheading(0)

    pen.color("#111827")
    pen.pensize(5)

    pen.pendown()

    for _ in range(4):
        pen.forward(board_width)
        pen.left(90)

    pen.penup()


# ============================================================
# DRAW TITLE
# ============================================================

def draw_title():
    """Display the title above the board."""

    title = turtle.Turtle()

    title.hideturtle()
    title.penup()
    title.color("#F8FAFC")

    board_width = BOARD_SIZE * SQUARE_SIZE

    title.goto(
        0,
        (board_width / 2) + 30
    )

    title.write(
        "CHESS BOARD",
        align="center",
        font=("Arial", 24, "bold")
    )


# ============================================================
# DRAW BOARD COORDINATES
# ============================================================

def draw_coordinates():
    """Draw simple chessboard coordinates."""

    labels = turtle.Turtle()

    labels.hideturtle()
    labels.penup()
    labels.color("#CBD5E1")

    board_width = BOARD_SIZE * SQUARE_SIZE

    start_x = -board_width / 2
    start_y = -board_width / 2

    files = "ABCDEFGH"

    for column in range(BOARD_SIZE):

        x = (
            start_x
            + column * SQUARE_SIZE
            + SQUARE_SIZE / 2
        )

        labels.goto(
            x,
            start_y - 25
        )

        labels.write(
            files[column],
            align="center",
            font=("Arial", 10, "bold")
        )

    for row in range(BOARD_SIZE):

        y = (
            start_y
            + row * SQUARE_SIZE
            + SQUARE_SIZE / 2
            - 5
        )

        labels.goto(
            start_x - 20,
            y
        )

        labels.write(
            str(row + 1),
            align="center",
            font=("Arial", 10, "bold")
        )


# ============================================================
# MAIN PROGRAM
# ============================================================

def main():

    draw_board()

    draw_border()

    draw_coordinates()

    draw_title()

    screen.update()

    screen.mainloop()


# ============================================================
# RUN PROGRAM
# ============================================================

if __name__ == "__main__":
    main()