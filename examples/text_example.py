from rgbmatrix import RGBMatrix, RGBMatrixOptions
from rgbmatrix import graphics
from utils.matrix_string_parser import MatrixStringParser
from utils.matrix_string_printer import MatrixStringPrinter
from utils.paths import font_6_x_9
import time

ROWS = 32
COLS = 64

options = RGBMatrixOptions()
options.rows = ROWS
options.cols = COLS
options.hardware_mapping = "adafruit-hat"

matrix = RGBMatrix(options=options)

canvas = matrix
red = graphics.Color(255, 0, 0)
green = graphics.Color(0, 255, 0)
blue = graphics.Color(0, 0, 255)

# graphics.DrawLine(canvas, 5, 5, 22, 13, red)
# graphics.DrawCircle(canvas, 15, 15, 10, green)

font = graphics.Font()

font.LoadFont(str(font_6_x_9))

msg = "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"

graphics.DrawText(
    canvas, 
    font, 
    2, 
    font.height, 
    red, 
    msg,
)

time.sleep(10)
canvas.Clear()

printer = MatrixStringPrinter(
    canvas=canvas,
    font = font,
    col_pad = 0,
    color=red,
)
printer.print_string(msg)


# graphics.DrawText(canvas, font, 2, 10, blue, "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG")
# print(font.CharacterWidth(ord('Q')))
time.sleep(10)
