# Apparently, you can have a function take any number of inputs with *args
# But, then, how do I refer to them individually? for loop.

from functools import reduce


# def symmetric_difference(*args):
#     flat_list = []
#     for arg in args:
#         for value in arg:
#             flat_list.append(value)
#     out_list = flat_list.copy()
#     out_list = [x for x in out_list if out_list.count(x) == 1]
#     return out_list


# Okay, this works for what I was trying to do, but this isn't symmetric difference. What they
# want is all values which do not appear in all sets. I also didn't consider repeated values in the same set.


# def sym(*args):
#     list_of_lists = [*args]
#     for arg in list_of_lists:
#         for value in arg:
#             pass
#     return


# print(sym([3, 3, 3, 2, 5], [2, 1, 5, 7]))
def symmetric_function(list1, list2):
    output_list = []
    for value in list1:
        if value not in list2 and (value not in output_list):
            output_list.append(value)
    for value in list2:
        if value not in list1 and (value not in output_list):
            output_list.append(value)
    return output_list


def symmetric_difference(*args):
    list_of_lists = [*args]
    out_list = reduce(symmetric_function, list_of_lists)
    out_list.sort()
    return out_list


print(symmetric_difference([1, 1, 2, 5], [2, 2, 3, 5], [3, 4, 5, 5]))
