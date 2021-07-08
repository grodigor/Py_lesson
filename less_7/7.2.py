def calculator_t():
    t = int(input('Enter the temperature: '))
    m = input('Enter the metric("C", "F", "K"): ').upper()
    if m == 'K':
        k = t
        c = k - 273.5
        f = k * 1.8 - 459.67
    if m == 'F':
        f = t
        k = (f + 459.67) / 1.8
        c = k - 273.5
    if m == 'C':
        c = t
        k = c + 273.5
        f = k * 1.8 - 459.67
    print(f'C = {c}, F = {f}, K = {k}')


calculator_t()