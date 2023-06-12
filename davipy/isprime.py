def isprime(number: int) -> bool:
    """Check if the given number is prime"""
    # TODO qua puoi controllare se il numero è pari, così il for lo puoi fare andare di due in due (i.e. lo step, il terzo parametro)
    for x in range(2, int(number ** 0.5) + 1):  # math.ceil() ?
        if number % x == 0:
            return False
    return True
