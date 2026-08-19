from .core import Canvas


class Color:
    red: int
    green: int
    blue: int

    def __init__(
        self,
        red: int = 0,
        green: int = 0,
        blue: int = 0,
    ) -> None: ...


class Font:
    height: int
    baseline: int

    def CharacterWidth(self, char: int) -> int: ...

    def LoadFont(self, file: str) -> None: ...

    def DrawGlyph(
        self,
        c: Canvas,
        x: int,
        y: int,
        color: Color,
        char: int,
    ) -> int: ...


def DrawText(
    c: Canvas,
    f: Font,
    x: int,
    y: int,
    color: Color,
    text: str,
) -> int: ...


def DrawCircle(
    c: Canvas,
    x: int,
    y: int,
    r: int,
    color: Color,
) -> None: ...


def DrawLine(
    c: Canvas,
    x1: int,
    y1: int,
    x2: int,
    y2: int,
    color: Color,
) -> None: ...