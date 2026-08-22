from rgbmatrix import RGBMatrix, RGBMatrixOptions
from rgbmatrix import graphics
from utils.matrix_string_parser import MatrixStringParser
from utils.matrix_string_printer import MatrixStringPrinter
from utils.paths import font_4_x_6
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
hannahs_color = graphics.Color(87, 210, 255)

# graphics.DrawLine(canvas, 5, 5, 22, 13, red)
# graphics.DrawCircle(canvas, 15, 15, 10, green)


def draw_sun(x, y, width, color):
    radius = width // 2

    # Sun
    graphics.DrawCircle(
        canvas,
        y,
        canvas.height - x - 1,
        width // 2,
        color
    )

    # Rays
    ray_length = max(1, width // 4)
    ray_distance = radius + 2
    diag_ray_distance = radius

    # Vertical rays
    for i in range(1, ray_length + 1):
        px(x, y - ray_distance - i + 1, color)
        px(x, y + ray_distance + i - 1, color)

    # Horizontal rays
    for i in range(1, ray_length + 1):
        px(x - ray_distance - i + 1, y, color)
        px(x + ray_distance + i - 1, y, color)

    # Diagonal rays
    for i in range(1, ray_length + 1):
        px(x - diag_ray_distance - i + 1, y - diag_ray_distance - i + 1, color)
        px(x + diag_ray_distance + i - 1, y - diag_ray_distance - i + 1, color)
        px(x - diag_ray_distance - i + 1, y + diag_ray_distance + i - 1, color)
        px(x + diag_ray_distance + i - 1, y + diag_ray_distance + i - 1, color)

        
def px(x, y, color: graphics.Color):
    if 0 <= x < 32 and 0 <= y < 64:
        canvas.SetPixel(
            y,
            31 - x,
            color.red,
            color.green,
            color.blue,
        )

font = graphics.Font()

font.LoadFont(str(font_4_x_6))

msg = "Hannah loves the sun... and tanning"

# graphics.DrawText(
#     canvas, 
#     font, 
#     2, 
#     font.height, 
#     red, 
#     msg,
# )

# time.sleep(10)
# canvas.Clear()

printer = MatrixStringPrinter(
    canvas=canvas,
    font = font,
    col_pad = 0,
    color=hannahs_color,
)
printer.print_string(msg)

draw_sun(10,40,10,graphics.Color(240, 199, 38))




# graphics.DrawText(canvas, font, 2, 10, blue, "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG")
# print(font.CharacterWidth(ord('Q')))
time.sleep(600)
