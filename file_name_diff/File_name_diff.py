import copy
import os
import prompt
from typing import Tuple


def get_path(number: int) -> str:
    return prompt.string(prompt=f"Input path to directory {number}: ")


def get_unique(list_one: list, list_two: list) -> list:
    unique = copy.deepcopy(list_one)
    for i in list_two:
        if i not in list_one:
            unique.append(i)
    return unique


def get_diff_lists(unique: list, list_1: list, list_2: list) -> Tuple:
    only_first = []
    only_two = []
    not_diff = []
    for item in unique:
        if item not in list_1:
            only_two.append(item)
        if item not in list_2:
            only_first.append(item)
        if item in list_1 and item in list_2:
            not_diff.append(item)
    return only_first, only_two, not_diff


def print_diff(data: Tuple):
    first_list, second_list, not_diff = data
    with open("difference.txt", "w") as output:
        output.write("ONLY IN FIRST FOLDER: \n")
        for item in first_list:
            output.write(f"---{item}\n")
        output.write("ONLY IN SECOND FOLDER: \n")
        for item in second_list:
            output.write(f"---{item}\n")
        output.write("IN BOTH FOLDER: \n")
        for item in not_diff:
            output.write(f"---{item}\n")


def file_name_diff():
    path_1 = get_path(1)
    path_2 = get_path(2)
    list_files_1 = os.listdir(path_1)
    list_files_2 = os.listdir(path_2)
    unique = get_unique(list_files_1, list_files_2)
    lists_of_diff = get_diff_lists(unique, list_files_1, list_files_2)
    print_diff(lists_of_diff)
    return "Well done!"


# D:/python_code/alekseifeniuk/file_name_diff/new_directory
# D:/python_code/alekseifeniuk/file_name_diff/new_directory_1
print(file_name_diff())
