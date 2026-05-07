from typing import List

def calculate_power_with_difference(ints: List[int]) -> List[int]:
    result = []
    for i in range(len(ints)):
        if i == 0:
           result.append(pow(ints[i], 2))
        else:
            current = pow(ints[i], 2)
            previous = pow(ints[i - 1], 2) - ints[i - 1]
            result.append(current - previous)

    return result