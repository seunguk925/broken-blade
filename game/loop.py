import time


def run(update, render, step=1 / 30, max_frame=0.25):
    """고정 타임스텝 게임 루프.

    update(dt)는 항상 step초 단위로 불러서 게임 상태를 진행시키고,
    render()는 프레임마다 한 번 불러서 화면을 그린다.
    """
    prev = time.monotonic()
    acc = 0.0

    while True:
        frame_start = time.monotonic()

        # 렉이 한 번 걸려도 update가 수십 번 몰려서 돌지 않게 한 프레임 시간을 자른다
        elapsed = min(frame_start - prev, max_frame)
        prev = frame_start
        acc += elapsed

        # 흐른 시간만큼 고정 간격으로 상태를 진행시킨다
        while acc >= step:
            update(step)
            acc -= step

        render()

        # 이번 프레임에 쓰고 남은 시간만큼 쉰다 (프레임 속도 상한 = 1 / step)
        remaining = step - (time.monotonic() - frame_start)
        if remaining > 0:
            time.sleep(remaining)
