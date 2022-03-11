from typing import Tuple
from functools import reduce
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


##########


##########
def keep_truthful(sequence) -> filter:
    return filter(truth, sequence)


def abs_sum(sequence):
    return sum(map(abs, sequence))


def walk(dictionary: dict, sequence):
    return reduce(getitem, sequence, dictionary)


##########
