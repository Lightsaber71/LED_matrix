from rgbmatrix import RGBMatrix, RGBMatrixOptions
from rgbmatrix import graphics
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

graphics.DrawLine(canvas, 5, 5, 22, 13, red)
graphics.DrawCircle(canvas, 15, 15, 10, green)

font = graphics.Font()
font.LoadFont("../../../fonts/7x13.bdf")

graphics.DrawText(canvas, font, 2, 10, blue, "Text")

time.sleep(10)