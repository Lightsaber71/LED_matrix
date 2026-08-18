from rgbmatrix import RGBMatrix, RGBMatrixOptions
import time

ROWS = 32
COLS = 64

options = RGBMatrixOptions()
options.rows = ROWS
options.cols = COLS
options.hardware_mapping = "adafruit-hat"

matrix = RGBMatrix(options=options)

canvas = matrix.CreateFrameCanvas()

matrix.SwapOnVSync(canvas)

colors = [
    ((255, 0, 0), "red"),
    ((0, 255, 0), "green"),
    ((0, 0, 255), "blue"),
]
color = colors[0][0]
for i in range(1000):
	for x in range(COLS):
		for y in range(ROWS):
			canvas.SetPixel(x, y, *color)
			print(f"{i:>4} Setting color {color}")
			# for color,name in colors:
			# 	canvas.SetPixel(x, y, *color)
			# 	
			# 	time.sleep(.1)

print("done")
