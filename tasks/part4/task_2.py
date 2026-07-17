import math


class OperationNotFoundException(Exception):
    pass


def math_calculate(function: str, *args):
    operation = getattr(math, function, None)
    if operation is None or not callable(operation):
        raise OperationNotFoundException

    return operation(*args)
