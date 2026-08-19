from typing import Any


class Canvas:
    def SetImage(
        self,
        image: Any,
        offset_x: int = 0,
        offset_y: int = 0,
        unsafe: bool = True,
    ) -> None: ...

    def SetPixelsPillow(
        self,
        xstart: int,
        ystart: int,
        width: int,
        height: int,
        image_capsule: Any,
    ) -> None: ...


class FrameCanvas(Canvas):
    width: int
    height: int
    pwmBits: int
    brightness: int

    def Fill(
        self,
        red: int,
        green: int,
        blue: int,
    ) -> None: ...

    def Clear(self) -> None: ...

    def SetPixel(
        self,
        x: int,
        y: int,
        red: int,
        green: int,
        blue: int,
    ) -> None: ...


class RGBMatrixOptions:
    hardware_mapping: str

    rows: int
    cols: int
    chain_length: int
    parallel: int
    pwm_bits: int
    pwm_lsb_nanoseconds: int
    brightness: int
    scan_mode: int
    row_address_type: int
    multiplexing: int
    pwm_dither_bits: int
    limit_refresh_rate_hz: int

    disable_hardware_pulsing: bool
    show_refresh_rate: bool
    inverse_colors: bool

    led_rgb_sequence: str
    pixel_mapper_config: str
    panel_type: str

    gpio_slowdown: int
    rp1_pio: int
    daemon: int
    drop_privileges: int
    drop_priv_user: str
    drop_priv_group: str


class RGBMatrix(Canvas):
    luminanceCorrect: bool
    pwmBits: int
    brightness: int
    height: int
    width: int

    def __init__(
        self,
        rows: int = 0,
        chains: int = 0,
        parallel: int = 0,
        options: RGBMatrixOptions | None = None,
    ) -> None: ...

    def Fill(
        self,
        red: int,
        green: int,
        blue: int,
    ) -> None: ...

    def SetPixel(
        self,
        x: int,
        y: int,
        red: int,
        green: int,
        blue: int,
    ) -> None: ...

    def Clear(self) -> None: ...

    def CreateFrameCanvas(self) -> FrameCanvas: ...

    def SwapOnVSync(
        self,
        newFrame: FrameCanvas,
        framerate_fraction: int = 1,
    ) -> FrameCanvas: ...