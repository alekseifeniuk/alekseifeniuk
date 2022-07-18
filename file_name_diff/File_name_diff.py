import copy
import os
import prompt
from math import sqrt


def get_path(number: int) -> str:
    return prompt.string(prompt=f"Input path to directory {number}: ")


def get_unique(list_one: list, list_two: list) -> list:
    unique = copy.deepcopy(list_one)
    for i in list_two:
        if i not in list_one:
            unique.append(i)
    return unique


def file_name_diff():
    path_1 = get_path(1)
    path_2 = get_path(2)
    list_files_1 = os.listdir(path_1)
    list_files_2 = os.listdir(path_2)
    unique = get_unique(list_files_1, list_files_2)
    return unique


# D:/python_code/alekseifeniuk/file_name_diff/new_directory
# D:/python_code/alekseifeniuk/file_name_diff/new_directory_1
# print(file_name_diff())
