dict_ = {'first_color': 'Red', 'second_color': 'Green', 'third_color': None, 'sss': None}
def pop_dict(arg):
    # for key, value in arg.items():
    #     if value == None:
    #         arg.pop(key)
    #         break
    del_empty = {key: value for key, value in arg.items() if value is not None}
    return del_empty

dict_ = pop_dict(dict_)
print(dict_)