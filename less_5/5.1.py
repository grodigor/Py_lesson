def is_prime(x):
    if x == 1:
        return False
    if x % 2 != 0 and x / x == 1:
        return True
    if x == 2:
        return True
    else:
        return False

