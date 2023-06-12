def iseven(number: int) -> bool:
    """Check if the given number is even"""
    return number % 2 == 0


def isodd(number: int) -> bool:
    """Check if the given number is odd"""
    return not iseven(number)
