import board
import digitalio

# CENTER(D4)는 주변 4방향이 같이 눌려서 사용하지 않음
PINS = {
    "UP": board.D17, "DOWN": board.D22, "LEFT": board.D27, "RIGHT": board.D23,
    "A": board.D5, "B": board.D6,
}


class Buttons:
    def __init__(self):
        self._pins = {}
        for name, pin in PINS.items():
            io = digitalio.DigitalInOut(pin)
            io.direction = digitalio.Direction.INPUT
            io.pull = digitalio.Pull.UP
            self._pins[name] = io

    def pressed(self):
        """지금 눌려 있는 버튼 이름들을 set으로 돌려준다. 누르면 LOW라서 not을 붙인다."""
        return {name for name, io in self._pins.items() if not io.value}