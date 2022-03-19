from collections import Counter
from datetime import date

# TASK 1: СЧЕТЧИК ОДНОГОДОК.
# Test: print(get_men_counted_by_year(users))
users = [
    {"name": "Bronn", "gender": "male", "birthday": "1973-03-23"},
    {"name": "Reigar", "gender": "male", "birthday": "1973-11-03"},
    {"name": "Eiegon", "gender": "male", "birthday": "1963-11-03"},
    {"name": "Sansa", "gender": "female", "birthday": "2012-11-03"},
    {"name": "Jon", "gender": "male", "birthday": "1980-11-03"},
    {"name": "Robb", "gender": "male", "birthday": "1980-05-14"},
    {"name": "Tisha", "gender": "female", "birthday": "2012-11-03"},
    {"name": "Rick", "gender": "male", "birthday": "2012-11-03"},
    {"name": "Joffrey", "gender": "male", "birthday": "1999-11-03"},
    {"name": "Edd", "gender": "male", "birthday": "1973-11-03"},
]


# Decision:
def get_men_counted_by_year(sequence: list) -> dict:
    list_of_year = []
    for user in sequence:
        if user["gender"] == "male":
            birthday_date = date.fromisoformat(user["birthday"])
            list_of_year.append(birthday_date.year)
    birthday_map = dict(Counter(list_of_year))
    return birthday_map


# TASK 2: COMPOSITION OF FUNCTION.
# Test: print(compose(str, mul3)(1))
def add5(x):
    return x + 5


def mul3(x):
    return x * 3


# Decision:
def compose(func_1, func_2):
    def inner(argument):
        result = func_1(func_2(argument))
        return result

    return inner


# TASK 3: SEARCH FOR THE NEAREST NEIGHBOR.
# Test: print(find_index_of_nearest(2, [8, 3, 5]))

# Decision:
def find_index_of_nearest(number: int, sequence: list):
    list_of_deltas = []
    if sequence:
        for item in sequence:
            list_of_deltas.append(abs(item - number))
        return list_of_deltas.index(min(list_of_deltas))


# TASK 4: COLOR CONVERTER.
# Test rgb2hex: print(rgb2hex(36, 171, 0))
# Test hex2rgb: print(hex2rgb("#24ab5b"))

# Decision:
def rgb2hex(r=0, g=0, b=0) -> str:
    return f"#{int(hex(r), 16):02x}{int(hex(g), 16):02x}{int(hex(b), 16):02x}"


def hex2rgb(hex_color: str) -> dict:
    color = hex_color.lstrip("#")
    return {
        "r": int(color[0:2], 16),
        "g": int(color[2:4], 16),
        "b": int(color[4:6], 16),
    }


# TASK 5: ANAGRAM FILTER.
# Test: print(filter_anagrams([1, 2], [[2, 1], [2, 2], [1, 2]]))

# Decision:
def filter_anagrams(task, sequence):
    anagrams_list = []
    for item in sequence:
        if Counter(task) == Counter(item):
            anagrams_list.append(item)
    return anagrams_list
