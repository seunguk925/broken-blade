import board, digitalio
from PIL import Image
from adafruit_rgb_display import st7789

cs_pin  = digitalio.DigitalInOut(board.CE0)
dc_pin  = digitalio.DigitalInOut(board.D25)
rst_pin = digitalio.DigitalInOut(board.D24)
backlight = digitalio.DigitalInOut(board.D26)
backlight.switch_to_output()

spi = board.SPI()
disp = st7789.ST7789(spi, width=240, height=240, rotation=180, x_offset=0, y_offset=80,
                     cs=cs_pin, dc=dc_pin, rst=rst_pin, baudrate=24000000)
disp.image(Image.new("RGB", (240, 240), (0, 0, 0)))
backlight.value = False
print("화면 지움")
