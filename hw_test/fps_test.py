import sys, time, random
import board, digitalio
from PIL import Image, ImageDraw
from adafruit_rgb_display import st7789

BAUD = int(sys.argv[1]) if len(sys.argv) > 1 else 24000000

cs_pin  = digitalio.DigitalInOut(board.CE0)
dc_pin  = digitalio.DigitalInOut(board.D25)
rst_pin = digitalio.DigitalInOut(board.D24)
backlight = digitalio.DigitalInOut(board.D26)
backlight.switch_to_output()
backlight.value = True

spi = board.SPI()
disp = st7789.ST7789(spi, width=240, height=240, rotation=180, x_offset=0, y_offset=80,
                     cs=cs_pin, dc=dc_pin, rst=rst_pin, baudrate=BAUD)

W, H, FRAMES = 240, 240, 60
print(f"SPI {BAUD/1e6:.0f}MHz")

def measure(name, make_frame):
    t0 = time.perf_counter()
    for i in range(FRAMES):
        disp.image(make_frame(i))
    dt = time.perf_counter() - t0
    print(f"[{name}] {FRAMES / dt:.1f} fps (프레임당 {dt / FRAMES * 1000:.1f} ms)")

solid = [Image.new("RGB", (W, H), c) for c in ("red", "green", "blue")]
measure("단색 전송", lambda i: solid[i % 3])

boxes = [[random.randint(0, W-16), random.randint(0, H-16),
          random.choice((-3, 3)), random.choice((-3, 3))] for _ in range(30)]

def game_like(i):
    img = Image.new("RGB", (W, H), (27, 31, 58))
    d = ImageDraw.Draw(img)
    for b in boxes:
        b[0] += b[2]; b[1] += b[3]
        if not 0 <= b[0] <= W-16: b[2] *= -1
        if not 0 <= b[1] <= H-16: b[3] *= -1
        d.rectangle([b[0], b[1], b[0]+15, b[1]+15], fill=(255, 122, 69))
    d.text((5, 5), f"frame {i}", fill="white")
    return img

measure("게임처럼 그리기", game_like)
