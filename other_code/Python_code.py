from typing import Tuple
from functools import reduce, wraps
from operator import truth, getitem


# LEARN COLLECTIONS
def toggle(collection, flag: set):
    if collection in flag:
        flag.discard(collection)
    else:
        flag.add(collection)


def toggled(collection, flag: set):
    new_flag = flag.copy()
    toggle(collection, new_flag)
    return new_flag


def key_in_dict(key: str):
    user = {"name": "Alex", "age": 27, "mail": "Ffl.B-Unit@mail.ru"}
    if key in user:
        return user.get(key)
    else:
        print("The specified key is missing!")
        for key, value in user.items():
            print(f"{key} = {value}")


def diff_keys(old_collection: dict, new_collection: dict) -> dict:
    list_old = set(old_collection.keys())
    list_new = set(new_collection.keys())
    result = {
        "kept": list_old & list_new,
        "added": list_new - list_old,
        "removed": list_old - list_new,
    }
    return result


def apply_diff(target, diff: dict):
    target.update(diff.get("add", {}))
    target.difference_update(diff.get("remove", {}))
    print(target)


# LEARN FUNCTION
def greet(name, *args):
    greet_string = "Hello, " + " and ".join((name,) + args) + "!"
    return greet_string


##########


def rgb(red=0, green=0, blue=0):
    return f"rgb({red}, {green}, {blue})"


def get_colors():
    colors_dictionary = {
        "red": rgb(red=255),
        "green": rgb(green=255),
        "blue": rgb(blue=255),
    }
    return colors_dictionary


##########


def updated(collection: dict, **kwargs) -> dict:
    new_collection = collection.copy()
    new_collection.update(kwargs)
    return new_collection


def call_twice(function, *args, **kwargs) -> Tuple:
    result_1 = function(*args, **kwargs)
    result_2 = function(*args, **kwargs)
    return result_1, result_2


##########


def add_function(item) -> Tuple:
    if item > 0:
        return True, "*" * item
    else:
        return False, ""


def filter_map(function, collection) -> list:
    new_collection = []
    for item in collection:
        state, value = function(item)
        if state is True:
            new_collection.append(value)
    return new_collection


# Learn map, filter, reduce
def keep_truthful(sequence) -> filter:
    return filter(truth, sequence)


def abs_sum(sequence):
    return sum(map(abs, sequence))


def walk(dictionary: dict, sequence):
    return reduce(getitem, sequence, dictionary)


# Learn closure
def greeting(name, surname):
    return f"Hello, {name} {surname}!"


def partial_apply(function, name):
    def inner(surname):
        return function(name, surname)

    return inner


def flip(function):
    def inner(name, surname):
        return function(surname, name)

    return inner


# Learn private function
def make_module(step=1):
    return {"inc": lambda x: x + step, "dec": lambda x: x - step}


# Learn decorators
def memoized(function):
    calculated_values = {}

    def inner(x):
        if x in calculated_values:
            return calculated_values[x]
        else:
            result = function(x)
            calculated_values[x] = result
            return result

    return inner


def memoizing(limit):
    def wrapper(function):
        calculated_values = {}
        keys = []

        @wraps(function)
        def inner(argument):
            memoized_result = calculated_values.get(argument)
            if memoized_result is None:
                memoized_result = function(argument)
                calculated_values[argument] = memoized_result
                keys.append(argument)
                if len(keys) > limit:
                    oldest_argument = keys.pop(0)
                    calculated_values.pop(oldest_argument)
            return memoized_result

        return inner

    return wrapper


@memoizing(3)
@memoized
def func(x: int) -> int:
    print("Calculating...")
    return x * 10


# Learn recursion
def is_even(argument):
    if argument == 0:
        return True
    else:
        return is_odd(argument - 1)


def is_odd(argument):
    if argument == 0:
        return False
    else:
        return is_even(argument - 1)


# __________________________________________________________
# def odds_from_odds(seq: list):
#     new_seq = []
#     for i in range(len(seq)):
#         if i % 2 == 0:
#             new_seq.append(
#                 list(filter(lambda x: seq[i].index(x) % 2 == 0, seq[i]))
#             )
#     return new_seq


def keep_odds_from_odds(sequence: list):
    index = len(sequence) - 1
    while index >= 0:
        if index % 2 != 0:
            sequence.pop(index)
        else:
            item_length = len(sequence[index]) - 1
            while item_length >= 0:
                if item_length % 2 != 0:
                    sequence[index].pop(item_length)
                item_length -= 1
        index -= 1
    return sequence


# __________________________________________________________
def write_result(function):
    list_of_result = list()

    def inner(x) -> Tuple:
        for i in range(x):
            list_of_result.append(function(x) * i)
        list_sum = sum(list_of_result)
        return list_of_result, list_sum

    return inner


@write_result
def summary(number: int) -> int:
    return number * 5


# __________________________________________________________


# Generators
def non_empty_truths(sequence: list) -> list:
    result_list = [
        x for x in [[y for y in one_list if y] for one_list in sequence] if x
    ]
    return result_list


def non_empty_truths_1(sequence: list) -> list:
    result = []
    for subseq in sequence:
        sub_result = []
        for val in subseq:
            if val:
                sub_result.append(val)
        if sub_result:
            result.append(sub_result)
    return result


def number_of_unique_letters(string: str) -> int:
    result = len({char for char in string.lower() if char.isalpha()})
    return result


# __________________________________________________________
def is_int(x):
    return isinstance(x, int)


def each2d(function, sequence: list) -> bool:
    return all(all(function(val) for val in item) for item in sequence)


def some2d(function, sequence: list) -> bool:
    return any(any(function(val) for val in item) for item in sequence)


def sum2d(function, sequence: list) -> int:
    return sum(sum(val for val in item if function(val)) for item in sequence)


# __________________________________________________________
def my_map(function, sequence: list):
    for item in sequence:
        yield function(item)


# How to use my_map function:
def my_map_result(function):
    result_list = []
    for item in function:
        result_list.append(item)
    return result_list


def my_filter(function, sequence: list):
    for item in sequence:
        if function(item):
            yield item


def replicate_each(mul: int, sequence: list):
    for item in sequence:
        yield from (item for _ in range(mul))
