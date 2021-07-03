import time


def countdown(func):
    def timer():
        for i in range(3,0,-1):
            print(i)
            time.sleep(1)
        func()
    return timer


@countdown
def time_now():
    print(time.strftime('%H:%M'))

time_now()