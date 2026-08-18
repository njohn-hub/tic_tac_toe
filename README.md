# ♟️ Chessboard — Python Turtle

A clean and customizable **chessboard generator built with Python Turtle Graphics**.

The project uses loops, functions, coordinates, colors, and Turtle graphics to dynamically generate an 8×8 chessboard.

## 📸 Features

* ♟️ Generates an 8×8 chessboard
* 🎨 Realistic chessboard colors
* 📐 Automatically centers the board
* 🔢 Chessboard coordinates
* 🖼️ Board border
* 📝 Project title
* ⚙️ Configurable board size
* 📏 Configurable square size
* 🐢 Built with Python Turtle
* 🧩 Uses reusable functions
* 🚫 No external dependencies

## 🛠️ Technologies Used

* **Python 3**
* **Turtle Graphics**

Python's built-in `turtle` module is used to create the graphical chessboard.

No external packages are required.

## 📂 Project Structure

```text
chessboard/
│
├── main.py
└── README.md
```

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/chessboard.git
```

### 2. Navigate into the project

```bash
cd chessboard
```

### 3. Run the application

```bash
python main.py
```

On Linux systems:

```bash
python3 main.py
```

## 🖥️ How It Works

The application creates a Turtle graphics screen:

```python
screen = turtle.Screen()
```

A Turtle object is then created to draw the board:

```python
pen = turtle.Turtle()
```

The board is generated using nested loops.

```python
for row in range(BOARD_SIZE):

    for column in range(BOARD_SIZE):
```

The nested loops allow the program to process every square on the board.

## 🎨 Alternating Square Colors

The application determines the color of each square using:

```python
if (row + column) % 2 == 0:
    color = LIGHT_COLOR
else:
    color = DARK_COLOR
```

This is what creates the alternating chessboard pattern.

For example:

```text
Light Dark Light Dark
Dark  Light Dark Light
Light Dark Light Dark
Dark  Light Dark Light
```

## 📐 Board Coordinates

The board is automatically centered using:

```python
board_width = BOARD_SIZE * SQUARE_SIZE

start_x = -board_width / 2
start_y = -board_width / 2
```

This means the board remains centered even when its size changes.

## 🧩 Drawing a Square

The project uses a reusable function:

```python
def draw_square(x, y, color):
```

The function receives:

* `x` — horizontal position
* `y` — vertical position
* `color` — square color

It then draws the square using four Turtle movements:

```python
for _ in range(4):
    pen.forward(SQUARE_SIZE)
    pen.left(90)
```

## ⚙️ Configuration

The main configuration values are located near the top of `main.py`.

```python
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700

BOARD_SIZE = 8
SQUARE_SIZE = 60

LIGHT_COLOR = "#F0D9B5"
DARK_COLOR = "#B58863"

BACKGROUND_COLOR = "#1E293B"
```

### Change the board size

For a 10×10 board:

```python
BOARD_SIZE = 10
```

For a 6×6 board:

```python
BOARD_SIZE = 6
```

### Change square size

```python
SQUARE_SIZE = 80
```

### Change the board colors

For example:

```python
LIGHT_COLOR = "#FFFFFF"
DARK_COLOR = "#000000"
```

Or use a modern green chessboard:

```python
LIGHT_COLOR = "#EEEED2"
DARK_COLOR = "#769656"
```

## 🧠 Python Concepts Demonstrated

This project demonstrates:

* Importing modules
* Variables
* Constants
* Functions
* Function parameters
* Nested loops
* Conditional statements
* The modulo operator `%`
* Turtle graphics
* Coordinate systems
* Pen control
* Color manipulation
* Screen configuration
* Program organization
* `if __name__ == "__main__"`

## 🔮 Future Improvements

Possible improvements include:

* [ ] Add chess pieces
* [ ] Add drag-and-drop pieces
* [ ] Add legal chess moves
* [ ] Create a playable chess game
* [ ] Add player turns
* [ ] Add check/checkmate detection
* [ ] Add undo/redo
* [ ] Add move history
* [ ] Add chess notation
* [ ] Add AI opponent
* [ ] Add difficulty levels
* [ ] Add sound effects
* [ ] Add game timer
* [ ] Add save/load functionality
* [ ] Add multiplayer support

## ♟️ Future Project: Playable Chess

This board provides a good foundation for a complete Python chess game.

A future version could contain:

```text
Chess Game
│
├── Board
├── Pieces
│   ├── King
│   ├── Queen
│   ├── Rook
│   ├── Bishop
│   ├── Knight
│   └── Pawn
│
├── Movement System
├── Capture System
├── Turn System
├── Check Detection
├── Checkmate Detection
├── Game Timer
└── User Interface
```

## 📚 Learning Goals

This project is useful for learning:

* Python loops
* Nested loops
* Functions
* Conditional logic
* Coordinate systems
* Basic graphics programming
* Turtle Graphics
* Code organization

It also demonstrates how a relatively small Python program can generate a structured graphical interface programmatically.

## 👨‍💻 Author

**John Ndungu**

Fullstack Developer passionate about building modern, functional, and user-friendly applications.

### Skills

* React
* JavaScript
* TypeScript
* Python
* Node.js
* Express.js
* Django
* Laravel
* MongoDB
* PostgreSQL
* Tailwind CSS

## 📄 License

This project is open source and available for educational and personal use.
