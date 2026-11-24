BG_COLOR = (27, 31, 58)
BOX_COLORS = [(255, 122, 69), (80, 200, 255)]
BOX_SIZE = 20


class DemoScene:
    """루프 확인용 임시 장면. 네모가 벽에 튕기고, A를 누르면 색이 바뀐다."""

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.x = width / 2
        self.y = height / 2
        self.vx = 120.0  # 픽셀/초
        self.vy = 90.0
        self.color_index = 0
        self._was_a_pressed = False

    def update(self, dt, pressed):
        self.x += self.vx * dt
        self.y += self.vy * dt

        max_x = self.width - BOX_SIZE
        max_y = self.height - BOX_SIZE
        if self.x < 0:
            self.x, self.vx = 0, abs(self.vx)
        elif self.x > max_x:
            self.x, self.vx = max_x, -abs(self.vx)
        if self.y < 0:
            self.y, self.vy = 0, abs(self.vy)
        elif self.y > max_y:
            self.y, self.vy = max_y, -abs(self.vy)

        # 누르고 있는 동안 계속 바뀌지 않게, 눌린 "순간"에만 반응한다
        is_a_pressed = "A" in pressed
        if is_a_pressed and not self._was_a_pressed:
            self.color_index = (self.color_index + 1) % len(BOX_COLORS)
        self._was_a_pressed = is_a_pressed

    def draw(self, draw, fps):
        draw.rectangle((0, 0, self.width - 1, self.height - 1), fill=BG_COLOR)
        x, y = int(self.x), int(self.y)
        draw.rectangle((x, y, x + BOX_SIZE - 1, y + BOX_SIZE - 1),
                       fill=BOX_COLORS[self.color_index])
        draw.text((5, 5), f"FPS {fps:.1f}", fill="white")
