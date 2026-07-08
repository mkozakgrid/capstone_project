import typing

def division(x: int, y: int) -> typing.Union[None, int]:
    if y == 0:
        print("Division by zero")
        print("Division finished")
        return None
    elif y == 1:
        print("Division finished")
        raise Exception("Deletion on 1 get the same result")
    else:
        print("Division finished")
        return x / y
 