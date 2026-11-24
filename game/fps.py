import time


class FpsCounter:
    """render할 때마다 tick()을 부르면 interval초마다 평균 FPS를 계산한다."""

    def __init__(self, interval=1.0):
        self.interval = interval
        self.fps = 0.0
        self._frames = 0
        self._start = time.monotonic()

    def tick(self):
        self._frames += 1
        now = time.monotonic()
        elapsed = now - self._start
        if elapsed >= self.interval:
            self.fps = self._frames / elapsed
            self._frames = 0
            self._start = now
