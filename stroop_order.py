# Settings for Stroop Test
# dr.strangelove@kberi.re.kr
import random

DEFAULT_BLOCK_NUMBER = 40
RED, BLUE, GREEN, YELLOW, WHITE = 1, 2, 3, 4, 5
COLOR_SET = [
    RED,
    BLUE,
    GREEN,
    YELLOW,
    WHITE,
]

DEFAULT_COLOR = WHITE

# STR = [
#     [RED, "빨강"],
#     [BLUE, "파랑"],
#     [GREEN, "초록"],
#     [YELLOW, "노랑"],
#     [WHITE, "하양"],
# ]

COLOR_STR = {
    RED: "빨강",
    BLUE: "파랑",
    GREEN: "초록",
    YELLOW: "노랑",
    WHITE: "하양",
}

# COLORCODE = [
#     [RED, "#FF0000"],
#     [BLUE, "#0000FF"],
#     [GREEN, "#00FF00"],
#     [YELLOW, "#FFFF00"],
#     [WHITE, "#FFFFFF"],
# ]

COLOR_CODE = {
    RED: "#FF0000",
    BLUE: "#0000FF",
    GREEN: "#00FF00",
    YELLOW: "#FFFF00",
    WHITE: "#FFFFFF",
}
# RED_STR, BLUE_STR, GREEN_STR, YELLOW_STR, WHITE_STR = "빨강", "파랑", "초록", "노랑", "하양"
# RED_COLOR, BLUE_COLOR, GREEN_COLOR, YELLOW_COLOR, WHITE_COLOR = "#FF0000", "#0000FF", "#00FF00", "#FFFF00", "#FFFFFF"
DEFAULT_STR = "🀰"  # C 조건에서 사용할 문자


class Stroop:
    displayed_character = None
    displayed_color = None
    correct_answer = None

    def print_stroop(self):
        print("displayed_character:", self.displayed_character,
              "displayed_color:", self.displayed_color,
              "correct_answer:", self.correct_answer)


class StroopC(Stroop):
    def __init__(self):
        self.displayed_character = DEFAULT_STR
        random_color = random.choice(COLOR_SET)
        self.displayed_color = COLOR_CODE[random_color]
        self.correct_answer = random_color


class StroopW(Stroop):
    def __init__(self):
        self.displayed_color = DEFAULT_COLOR
        random_color = random.choice(COLOR_SET)
        self.displayed_character = COLOR_STR[random_color]
        self.correct_answer = random_color


class StroopCW(Stroop):
    def __init__(self):
        random_color1 = random.choice(COLOR_SET)
        random_color2 = random.choice(COLOR_SET)
        self.displayed_character = COLOR_STR[random_color1]
        self.displayed_color = COLOR_CODE[random_color2]
        self.correct_answer = random_color2
