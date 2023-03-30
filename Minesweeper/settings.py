from win32api import GetSystemMetrics

RES = WIDTH, HEIGHT = GetSystemMetrics(0)-300, GetSystemMetrics(1)-200

CENTER = HALF_WIDTH, HALF_HEIGHT = WIDTH / 2 , HEIGHT / 2

FPS = 60

BUTTON_HOVER = (175,175,175)