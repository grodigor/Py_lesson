list_of_number = []
multiplex = 1


def max_quantity(list_of_number):
    count = 0
    max_value = max(list_of_number)
    for i in list_of_number:
        if i == max_value:
            count += 1
    return count


def odd_even(list_of_number):
    even = 0
    odd = 0
    for i in list_of_number:
        if i % 2 == 0:
            even += 1
        if i % 2 != 0:
            odd += 1
    return odd, even


while True:
    input_number = int(input('Enter the number. Number 0 will finish the program: '))
    if input_number != 0:
        list_of_number.append(input_number)
        max_num = max(list_of_number)
        odd, even = odd_even(list_of_number)
        unique_list = list(set(list_of_number))
        unique_list.sort()
        unique_list.reverse()
        multiplex *= input_number
    elif input_number == 0:
        print(f'Quantity of elements: {len(list_of_number)}')
        print(f'Sum of entered numbers: {sum(list_of_number)}')
        print(f'Product of numbers: {multiplex}')
        print(f'Average value: {sum(list_of_number) / (len(list_of_number))}')
        print(f'Max value in the list: {max_num}')
        print(f'Index number of max value: {list_of_number.index(max_num)}')
        print(f'Odd numbers {odd}, even numbers {even}')
        print(f'Premax value: {unique_list[1]}')
        print(f'Quantity of max elements: {max_quantity(list_of_number)}')
        break
