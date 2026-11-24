import time
import board, digitalio

PINS = {
    "UP": board.D17, "DOWN": board.D22, "LEFT": board.D27, "RIGHT": board.D23,
    "CENTER": board.D4, "A(#5)": board.D5, "B(#6)": board.D6,
}

buttons = {}
for name, pin in PINS.items():
    b = digitalio.DigitalInOut(pin)
    b.direction = digitalio.Direction.INPUT
    b.pull = digitalio.Pull.UP
    buttons[name] = b

print("조이스틱이랑 버튼 눌러봐. 끝내려면 Ctrl+C")
prev = {n: False for n in buttons}
try:
    while True:
        for name, b in buttons.items():
            pressed = not b.value
            if pressed != prev[name]:
                print(f"{name:7s} {'눌림' if pressed else '뗌'}")
                prev[name] = pressed
        time.sleep(0.01)
except KeyboardInterrupt:
    print("\n끝")
