# __________________________FUNCTIONS__________________________

from collections import Counter
from datetime import date
from typing import NamedTuple
from urllib.parse import urlparse, urlunparse, parse_qs, urlencode
import copy

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


# __________________________ABSTRACTION__________________________
# TASK 1: URL PARSING.
# Test:
# address = make("https://hexlet.io/community?q=low")
# print(address)
# print(get_scheme(address))
# print(set_scheme(address, "http"))
# print(get_host(address))
# print(set_host(address, "docs.python.org"))
# print(get_path(address))
# print(set_path(address, "/404"))
# print(get_query_param(address, "q"))
# print(set_query_param(address, "page", "high"))
# print(to_string(set_query_param(address, "page", 5)))
# Decision:
def make(url: str) -> NamedTuple:
    return urlparse(url)


def get_scheme(url):
    return url.scheme


def set_scheme(url: NamedTuple, new_scheme: str):
    return url._replace(scheme=new_scheme)


def get_host(url):
    return url.hostname


def set_host(url: NamedTuple, new_host: str):
    return url._replace(netloc=new_host)


def get_path(url):
    return url.path


def set_path(url: NamedTuple, new_path: str):
    return url._replace(path=new_path)


def get_query_param(url, param: str, value=None):
    return parse_qs(url.query).get(param, value)[0]


def set_query_param(url, param, value):
    request_params = parse_qs(url.query)
    if value is None:
        request_params.pop(param)
    else:
        request_params[param] = [value]
    return url._replace(
        query=urlencode(request_params, doseq=True)
    )


def to_string(url: NamedTuple) -> str:
    return urlunparse(url)
