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
    user = {
        "name": "Alex",
        "age": 27,
        "mail": "Ffl.B-Unit@mail.ru"
    }
    if key in user:
        return user.get(key)
    else:
        print("The specified key is missing!")
        for key, value in user.items():
            print(f"{key} = {value}")


