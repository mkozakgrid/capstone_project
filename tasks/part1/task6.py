from typing import Tuple

def get_min_max(filename: str) -> Tuple[int, int]:
    max = -1
    min = 100000000000
    result: Tuple = (0, 0)
    with open(filename) as opened_file:
        for line in opened_file:
            if line >= max:
                max = line
            if line <= min:
                min = line
        result = (min, max)
    return result