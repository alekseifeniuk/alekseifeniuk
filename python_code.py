def learning_dict(key):
    collection = {
        "name": "Alexey",
        "age": 27,
        "mail": "Ffl.B-Unit@mail.ru"
    }
    if key in collection:
        return collection.get(key)
    else:
        print("Satisfied key is missing!")
        for k, v in collection.items():
            print(f"{k} = {v}")
