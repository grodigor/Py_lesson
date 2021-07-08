def split_decor(func):
    def wraper():
        s = func().split()
        print(s)
    return wraper


@split_decor
def print_str():
    s1 = input('enter the string: ')
    return  s1


print_str()
