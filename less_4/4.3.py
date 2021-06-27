def my_range(a, b):
    if a < b:
        list_ = list(range(a, b + 1))
    if a > b:
        list_ = list(range(a, b - 1, -1))
    return list_
