import copy
import itertools
import operator
import os
from hexlet.fs import (
    mkdir,
    mkfile,
    is_file,
    get_meta,
    get_children,
    get_name,
    flatten,
)


# 1)
def remove_first_level(sequence: list) -> list:
    second_list = filter(lambda item: isinstance(item, list), sequence)
    return list(itertools.chain(*second_list))
# print(remove_first_level([[5], 1, [[3, 2], 4]]))


# 2)
def generate() -> dict:
    return (
        mkdir("python-package", meta={"hidden": True}, children=[
            mkfile("Makefile"),
            mkfile("README.md"),
            mkdir("dist"),
            mkdir("tests", children=[mkfile("test_solution.py")]),
            mkfile("pyproject.toml"),
            mkdir(".venv", meta={"owner": "root", "hidden": False}, children=[
                mkdir("lib", children=[
                    mkdir("python3.6", children=[
                        mkdir("site-packages", children=[
                            mkfile("hexlet-python-package.egg-link")
                        ])
                    ])
                ])
            ])
        ])
    )


# 3) Are given:
tree = mkdir(
    'my documents',
    [
        mkdir('1C_files'),
        mkfile('avatar.jpg', {'size': 100}),
        mkfile('photo.jpg', {'size': 150}),
    ],
    {'hide': False}
)


# Decision:
def compress_images(file_system: dict) -> dict:
    new_meta = copy.deepcopy(get_meta(file_system))
    children = list(get_children(file_system))
    new_children = []
    for child in children:
        if ".jpg" in get_name(child) and is_file(child):
            meta = copy.deepcopy(get_meta(child))
            meta["size"] //= 2
            new_children.append(mkfile(get_name(child), meta))
        else:
            new_children.append(child)
    return mkdir(get_name(file_system), new_children, new_meta)


# 4) Are given:
tree_1 = mkdir('/', [
    mkdir('eTc', [
        mkdir('NgiNx', [], {'size': 4000}),
        mkdir(
            'CONSUL',
            [mkfile('config.JSON', {'uid': 0})],
        ),
    ]),
    mkfile('HOSTS'),
])


# Decision:
def downcase_file_names(file_system: dict) -> dict:
    new_name = get_name(file_system)
    new_meta = copy.deepcopy(get_meta(file_system))
    if is_file(file_system):
        return mkfile(new_name.lower(), new_meta)
    children = get_children(file_system)
    new_children = list(map(downcase_file_names, children))
    return mkdir(new_name, new_children, new_meta)


# 5) Are given:
tree_2 = mkdir('/', [
    mkdir('etc', [
        mkdir('apache'),
        mkdir('nginx', [
            mkfile('.nginx.conf', {'size': 800}),
        ]),
        mkdir('.consul', [
            mkfile('.config.json', {'size': 1200}),
            mkfile('data', {'size': 8200}),
            mkfile('raft', {'size': 80}),
        ]),
    ]),
    mkfile('.hosts', {'size': 3500}),
    mkfile('resolve', {'size': 1000}),
])


# Decision:
def get_hidden_files_count(node: dict) -> int:
    if is_file(node) and get_name(node).startswith("."):
        return 1
    children = get_children(node)
    hidden_files_counter = list(map(get_hidden_files_count, children))
    return sum(hidden_files_counter)


# 6) Are given:
# See at 5.
# Decision:
def du(node: dict):
    children = get_children(node)

    def count_size(child):
        if is_file(child):
            return get_meta(child)["size"]
        children_list = get_children(child)
        return sum(list(map(count_size, children_list)))

    result = list(
        map(lambda child: (get_name(child), count_size(child)), children)
    )
    result.sort(key=operator.itemgetter(1), reverse=True)
    return result


# 5) Are given:
tree_3 = mkdir('/', [
    mkdir('etc', [
        mkdir('apache'),
        mkdir('nginx', [
            mkfile('nginx.conf', {'size': 800}),
        ]),
        mkdir('consul', [
            mkfile('config.json'),
            mkfile('data'),
            mkfile('raft'),
        ]),
    ]),
    mkfile('hosts', {'size': 3500}),
    mkfile('resolve', {'size': 1000}),
])


# Decision:
def find_files_by_name(tree: dict, part: str) -> list:
    def inner(node, ancestry):
        name = get_name(node)
        new_ancestry = os.path.join(ancestry, name)
        if is_file(node):
            return [] if name.find(part) < 0 else new_ancestry
        children = get_children(node)
        paths = map(lambda child: inner(child, new_ancestry), children)
        return flatten(paths)

    return inner(tree, "")
