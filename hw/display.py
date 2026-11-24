import board
import digitalio
from PIL import Image
from adafruit_rgb_display import st7789

WIDTH = HEIGHT = 240
BAUDRATE = 62_000_000  # fps_test.py에서 쓴 값으로 맞추기


class Display:
    def __init__(self):
        self._backlight = digitalio.DigitalInOut(board.D26)
        self._backlight.switch_to_output()
        self._backlight.value = True

        self._disp = st7789.ST7789(
            board.SPI(), width=WIDTH, height=HEIGHT,
            rotation=180, x_offset=0, y_offset=80,
            cs=digitalio.DigitalInOut(board.CE0),
            dc=digitalio.DigitalInOut(board.D25),
            rst=digitalio.DigitalInOut(board.D24),
            baudrate=BAUDRATE,
        )

    def show(self, image):
        self._disp.image(image)

    def close(self):
        self._disp.image(Image.new("RGB", (WIDTH, HEIGHT), (0, 0, 0)))
        self._backlight.value = False