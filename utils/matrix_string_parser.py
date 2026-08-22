import time
from rgbmatrix import graphics

class MatrixStringParser():
    def __init__(self, msg: str, font: graphics.Font):
        self._font = font
        self._msg = msg
        self._index = 0
        self._split_index = 0
        self._split = self._msg.split()

    @property
    def num_words(self):
        return len(self._split)

    def get_next_word(self):
        if self._split_index < len(self._split):
            word = self._split[self._split_index]
            self._split_index = self._split_index + 1
            return word
        else:
            return None

    def get_current_word(self):
            if self._split_index < len(self._split):
                word = self._split[self._split_index]
                return word
            else:
                return None   

    def get_current_word_width(self):
        word = self.get_current_word()
        word_width = 0
        if word is None:
            return 0
        for char in word:
            word_width = word_width + self._font.CharacterWidth(ord(char))
        return word_width