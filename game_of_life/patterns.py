MAX_PATTERTN_SIZE = 10


def get_glider_pattern():
    return [[0, 1, 0], [0, 0, 1], [1, 1, 1]]


def get_blinker_pattern():
    return [[0, 0, 0], [1, 1, 1], [0, 0, 0]]


def get_pulsar_pattern():
    return [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
    ]


PRESET_PATTERNS = {
    "glider": get_glider_pattern(),
    "blinker": get_blinker_pattern(),
    "pulsar": get_pulsar_pattern(),
}
