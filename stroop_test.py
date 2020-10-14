# Settings for Stroop Test
# dr.strangelove@kberi.re.kr
import random
import json

META_KEYCODE = 32

DEFAULT_BLOCK_NUMBER = 30
RED, BLUE, GREEN, YELLOW, WHITE = 1, 2, 3, 4, 5

COLOR_SET = [
    RED,
    BLUE,
    GREEN,
    YELLOW,
    WHITE,
]

DEFAULT_COLOR_CODE = "white"
DEFAULT_COLOR = WHITE
BACKGROUND_COLOR = "black"

COLOR_STR = {
    RED: "빨강",
    BLUE: "파랑",
    GREEN: "초록",
    YELLOW: "노랑",
    WHITE: "하양",
}


COLOR_CODE = {
    RED: "#FF0000",
    BLUE: "#0000FF",
    GREEN: "#00FF00",
    YELLOW: "#FFFF00",
    WHITE: "#FFFFFF",
}

DEFAULT_STR = "ㅁ"  # C 조건에서 사용할 문자. 네모문자ㅁ는 일부 브라우저(크롬)에서 색이 안입혀짐. 일반문자로 대체

NAME_OF_TEST = ["c", "w", "cw"]

instruction_messages = [
    [
        "검사 1에서는 중앙에 주어진 네모(" + DEFAULT_STR + ")의 색깔을 맞춰야 합니다. ",
        "아래 그림은 검사 1의 화면의 예입니다.",
        "이 화면에서는 '빨강'을 눌러야 합니다. 네모의 색깔이 빨간색이기 때문입니다.",
    ],[
        "검사 2에서는 중앙에 씌여진 단어와 같은 단어를 골라주시면 됩니다.",
        "아래 그림은 검사 2의 화면의 예입니다.",
        "이 화면에서는 주어진 단어인 '빨강'과 같은 '빨강'을 골라주시면 됩니다.",
    ],[
        "검사 3에서는 글자의 내용과 글자의 색이 무관하게 나타납니다.",
        "글자의 내용과 무관하게 나타나있는 색깔을 선택해야 합니다",
        "아래 그림은 검사 3의 화면의 예입니다",
        "이 화면에서는 '초록' 을 눌러야 합니다. 글자 내용은 '빨강' 이지만 글자의 색이 '초록' 색이기 때문입니다.",
    ]
]


class Stroop:
    displayed_character = None
    displayed_color = None
    displayed_color_code = None
    correct_answer = None
    num_errors = 0
    response_time = None
    keypress_history = {}

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def print_stroop(self):
        # print("displayed_character:", self.displayed_character,
        #       "displayed_color:", self.displayed_color,
        #       "correct_answer:", self.correct_answer)
        pass


class StroopC(Stroop):
    def __init__(self, random_color):
        self.displayed_character = DEFAULT_STR
        # random_color = random.choice(COLOR_SET)
        self.displayed_color_code = COLOR_CODE[random_color]
        self.displayed_color = random_color
        self.correct_answer = random_color
        self.print_stroop()


class StroopW(Stroop):
    def __init__(self, random_color):
        self.displayed_color_code = DEFAULT_COLOR_CODE
        self.displayed_color = DEFAULT_COLOR
        # random_color = random.choice(COLOR_SET)
        self.displayed_character = COLOR_STR[random_color]
        self.correct_answer = random_color
        self.print_stroop()


class StroopCW(Stroop):
    def __init__(self, random_color1, random_color2):
        # random_color1 = random.choice(COLOR_SET)
        # random_color2 = random.choice(COLOR_SET)
        self.displayed_character = COLOR_STR[random_color1]
        self.displayed_color_code = COLOR_CODE[random_color2]
        self.displayed_color = random_color2
        self.correct_answer = random_color2
        self.print_stroop()


class SessionBlocks:
    name_of_test = NAME_OF_TEST
    items = {}
    for name in NAME_OF_TEST:
        items[name] = []

    # we need 4 * size_of_list random numbers_with_no_duplicates
    def generate_no_duplicated_random_colors(size):
        random_colors = []
        for i in range(0, size):
            random_color = random.choice(COLOR_SET)
            if i > 0:
                while random_colors[i - 1] == random_color:
                    random_color = random.choice(COLOR_SET)
            random_colors.append(random_color)
        return random_colors

    rnd_for_c = generate_no_duplicated_random_colors(DEFAULT_BLOCK_NUMBER)
    rnd_for_w = generate_no_duplicated_random_colors(DEFAULT_BLOCK_NUMBER)
    rnd_for_cw1 = generate_no_duplicated_random_colors(DEFAULT_BLOCK_NUMBER)
    rnd_for_cw2 = generate_no_duplicated_random_colors(DEFAULT_BLOCK_NUMBER)

    def __init__(self):
        self.items = {}   # 이렇게 안하면 constructor 부를때마다 누적됨 5 10 15 20.. append 쓰기 때문인듯.
        for name in NAME_OF_TEST:
            self.items[name] = []
        for i in range(0, DEFAULT_BLOCK_NUMBER):
            self.items[self.name_of_test[0]].append(StroopC(self.rnd_for_c[i]))
            self.items[self.name_of_test[1]].append(StroopW(self.rnd_for_w[i]))
            self.items[self.name_of_test[2]].append(StroopCW(self.rnd_for_cw1[i], self.rnd_for_cw2[i]))


default_SessionBlocks = SessionBlocks()
