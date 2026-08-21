
from rgbmatrix import RGBMatrix
from rgbmatrix import graphics
from utils.matrix_string_parser import MatrixStringParser

class MatrixStringPrinter:

    def __init__(self, 
        canvas: RGBMatrix, 
        font: graphics.Font, 
        col_pad: int, 
        color: graphics.Color
    ):
        self._canvas = canvas
        self._cols = canvas.width
        self._rows = canvas.height
        self._color = color
        self._font = font
        self._cur_row = font.height
        self._col_pad = col_pad
        self._cur_col = col_pad

    def print_string(self, msg: str):
        parser = MatrixStringParser(msg,self._font)
        print("1")
        for i in range(parser.num_words):
            print("2")
            remaining_valid_cols = self._cols - self._cur_col - self._col_pad
            word_width = parser.get_current_word_width()
            print(f"word: {parser.get_current_word()}")
            print(f"word_width: {word_width}")
            print(f"remaining_valid_cols: {remaining_valid_cols}")
            print(f"word_width > remaining_valid_cols: {word_width > remaining_valid_cols}")
            if word_width > remaining_valid_cols:
                self._new_line()
            
            word = parser.get_next_word()
            if word is None:
                return
            word = word + " "
            graphics.DrawText(
                self._canvas, 
                self._font, 
                self._cur_col, 
                self._cur_row, 
                self._color, 
                word,
            )
            space_width = self._font.CharacterWidth(ord(" "))
            self._cur_col = self._cur_col + (word_width + space_width)

    def _new_line(self):
        print("new line")
        # next row
        self._cur_row = self._cur_row + self._font.height
        # reset col
        self._cur_col = self._col_pad