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
