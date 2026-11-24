from PIL import Image, ImageDraw

from hw.display import Display, WIDTH, HEIGHT
from hw.buttons import Buttons
from game.loop import run
from game.fps import FpsCounter
from game.demo_scene import DemoScene


def main():
    display = Display()

    try:
        buttons = Buttons()
        scene = DemoScene(WIDTH, HEIGHT)
        fps = FpsCounter()

        # 프레임 이미지는 한 번만 만들어서 계속 덮어 그린다
        image = Image.new("RGB", (WIDTH, HEIGHT))
        draw = ImageDraw.Draw(image)

        def update(dt):
            scene.update(dt, buttons.pressed())

        def render():
            scene.draw(draw, fps.fps)
            display.show(image)
            fps.tick()
        run(update, render)
    except KeyboardInterrupt:
        pass
    finally:
        display.close()


if __name__ == "__main__":
    main()
