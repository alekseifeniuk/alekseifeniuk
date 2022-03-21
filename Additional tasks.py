# __________________________FUNCTIONS__________________________

from collections import Counter
from datetime import date

# TASK 1: COUNTER.
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


# _______________________SETS AND DICTIONARY_______________________
# TASK 1: DNA to RNA.
# Test: print(to_rna('ACGTGGTCTTAA'))
# Decision:
def to_rna(dna: str):
    acids = {"G": "C", "C": "G", "T": "A", "A": "U"}
    rna = "".join(acids[acid] for acid in dna)
    return rna


# TASK 2: QUERY STRING BUILDER.
# Test: print(build_query_string({'per': 10, 'page': 1}))
# Decision:
def build_query_string(params: dict) -> str:
    sorted_params = sorted(params)
    query_string = "&".join(f"{key}={params[key]}" for key in sorted_params)
    return query_string


# TASK 3: DIFFERENCE CALCULATOR.
# Test: print(gen_diff({"one": "eon", "two": "two", "four": True},
#                 {"two": "own", "zero": 4, "four": True}))
# Decision:
def gen_diff(dict_1: dict, dict_2: dict) -> dict:
    keys = dict_1.keys() | dict_2.keys()
    result_dict = {}
    for key in keys:
        if key not in dict_1:
            result_dict[key] = "added"
        if key not in dict_2:
            result_dict[key] = "deleted"
        if key in dict_1 and key in dict_2:
            if dict_1[key] == dict_2[key]:
                result_dict[key] = "unchanged"
            else:
                result_dict[key] = "changed"
    return result_dict


# TASK 4: DICTIONARY MERGE.
# Test: print(merged({'a': 1, 'b': 2}, {'b': 10, 'c': 10}, {'d': 12, 'a': 4}))
# Decision:
def merged(*args: dict) -> dict:
    keys = set()
    for dictionary in args:
        keys = keys | dictionary.keys()
    merged_dict = {}
    for key in keys:
        merged_dict[key] = set()
        for dictionary in args:
            if key in dictionary:
                merged_dict[key].add(dictionary[key])
    return merged_dict


# TASK 5: SCRABBLE.
# Test: print(scrabble('scriptingjava', 'JavaScript'))
# Decision:
def scrabble(char_string: str, word: str) -> bool:
    word_dict = dict(Counter(word.lower()))
    char_dict = dict(Counter(char_string.lower()))
    for key in word_dict.keys():
        if char_dict.setdefault(key, 0) < word_dict[key]:
            return False
    else:
        return True


# TASK 6: DETECTION.
# Test: print(find_where(library, {'author': 'Shakespeare', 'year': 1611}))
library = [
    {"title": "Book of Fooos", "author": "Foo", "year": 1111},
    {"title": "Cymbeline", "author": "Shakespeare", "year": 1611},
    {"title": "The Tempest", "author": "Shakespeare", "year": 1611},
    {"title": "Book of Foos Barrrs", "author": "FooBar", "year": 2222},
    {"title": "Still foooing", "author": "FooBar", "year": 333},
    {"title": "Happy Foo", "author": "FooBar", "year": 4444},
]


# Decision:
def find_where(books: list, query: dict) -> dict:
    query_string = set(query.values())
    for book in books:
        book_inf = set(book.values())
        if book_inf.issuperset(query_string):
            return book


# TASK 7: ROMAN NUMERALS.
# Test: print(find_where(library, {'author': 'Shakespeare', 'year': 1611}))
# Decision:
def to_roman(number: int) -> str:
    library_numbers = {
        1: "I",
        4: "IV",
        5: "V",
        9: "IX",
        10: "X",
        40: "XL",
        50: "L",
        90: "XC",
        100: "C",
        400: "CD",
        500: "D",
        900: "CM",
        1000: "M",
    }
    arab = list(library_numbers.keys())
    roman = list(library_numbers.values())
    result = ""
    i = len(arab) - 1
    while number > 0:
        if number >= arab[i]:
            result += roman[i]
            number -= arab[i]
        else:
            i -= 1
    return result


print(to_roman(3))