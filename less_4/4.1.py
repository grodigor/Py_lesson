def run_vasia(first_day, current_day):
    day_number = 1
    while True:
        first_day *= 1.1
        day_number += 1
        if first_day >= current_day:
            return day_number

