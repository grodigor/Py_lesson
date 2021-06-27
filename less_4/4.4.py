def stairs():
    n = int(input('input n:'))
    list_ = ''
    if n <= 9:
        for i in range(1, n+1):
            list_ += str(i)
            print(list_)

stairs()