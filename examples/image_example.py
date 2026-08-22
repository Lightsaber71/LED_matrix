from rgbmatrix import RGBMatrix, RGBMatrixOptions
import time

ROWS = 32
COLS = 64

options = RGBMatrixOptions()
options.rows = ROWS
options.cols = COLS
options.hardware_mapping = "adafruit-hat"

matrix = RGBMatrix(options=options)
canvas = matrix


# ==================================================
# Colors
# ==================================================

BACKGROUND = (5, 10, 20)

UMBRELLA = (220, 40, 60)
UMBRELLA_DARK = (130, 20, 40)

HAIR = (25, 15, 20)
SKIN = (255, 190, 155)

SHIRT = (40, 90, 160)
SKIRT = (45, 55, 110)

SHOES = (15, 15, 20)

EYE = (0, 0, 0)


# ==================================================
# Logical canvas
#
# We are designing as:
#
#       32 pixels wide
#       64 pixels tall
#
# Then rotating it onto the physical 64x32 matrix.
# ==================================================

def px(x, y, color):
    if 0 <= x < 32 and 0 <= y < 64:
        canvas.SetPixel(y, 31 - x, *color)


# ==================================================
# Background
# ==================================================

canvas.Fill(*BACKGROUND)


# ==================================================
# Umbrella
# ==================================================

# Umbrella centered at x=16
#
#             █████
#          ███████████
#        █████████████████
#       ███████████████████
#

for y in range(2, 11):

    half_width = 4 + y

    left = 16 - half_width
    right = 16 + half_width

    for x in range(left, right + 1):
        px(x, y, UMBRELLA)


# Umbrella scallops

for x in range(6, 27, 4):
    px(x, 11, UMBRELLA_DARK)
    px(x + 1, 11, UMBRELLA_DARK)


# Umbrella ribs

for x in (10, 16, 22):
    for y in range(5, 11):
        px(x, y, UMBRELLA_DARK)


# ==================================================
# Umbrella pole
# ==================================================

for y in range(11, 24):
    px(16, y, UMBRELLA_DARK)


# ==================================================
# Head / hair
# ==================================================

for y in range(15, 22):

    if y == 15:
        width = 3
    elif y == 16:
        width = 4
    else:
        width = 5

    for x in range(16 - width, 17 + width):
        px(x, y, HAIR)


# Face

for y in range(17, 22):
    for x in range(13, 19):
        px(x, y, SKIN)


# Hair framing face

for y in range(18, 25):
    px(12, y, HAIR)
    px(13, y, HAIR)

for y in range(18, 22):
    px(18, y, HAIR)
    px(19, y, HAIR)


# Eyes

px(14, 19, EYE)
px(17, 19, EYE)


# ==================================================
# Neck
# ==================================================

for x in range(14, 18):
    px(x, 22, SKIN)


# ==================================================
# Body / shirt
# ==================================================

for y in range(23, 34):

    width = 4

    for x in range(16 - width, 17 + width):
        px(x, y, SHIRT)


# ==================================================
# Arm holding umbrella
# ==================================================

# Arm rises toward umbrella pole

for y in range(24, 29):
    px(21, y, SKIN)
    px(22, y, SKIN)

px(22, 23, SKIN)
px(21, 22, SKIN)
px(20, 21, SKIN)

# Hand

px(18, 20, SKIN)
px(19, 20, SKIN)


# ==================================================
# Other arm
# ==================================================

for y in range(25, 33):
    px(10, y, SKIN)
    px(11, y, SKIN)


# ==================================================
# Skirt
# ==================================================

for y in range(33, 43):

    half_width = 5 + (y - 33) // 2

    for x in range(
        16 - half_width,
        17 + half_width
    ):
        px(x, y, SKIRT)


# ==================================================
# Legs
# ==================================================

# Left leg

for y in range(43, 58):
    px(14, y, SKIN)
    px(15, y, SKIN)


# Right leg

for y in range(43, 58):
    px(18, y, SKIN)
    px(19, y, SKIN)


# ==================================================
# Shoes
# ==================================================

for x in range(12, 16):
    px(x, 58, SHOES)
    px(x, 59, SHOES)

for x in range(18, 22):
    px(x, 58, SHOES)
    px(x, 59, SHOES)


# ==================================================
# Display
# ==================================================

time.sleep(600)

canvas.Clear()