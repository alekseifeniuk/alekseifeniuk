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


# For this function was one more function:
def rgb(red=0, green=0, blue=0):
    return "rgb({}, {}, {})".format(red, green, blue)


def get_colors():
    colors_dictionary = {
        "red": rgb(red=255),
        "green": rgb(green=255),
        "blue": rgb(blue=255),
    }
    return colors_dictionary
