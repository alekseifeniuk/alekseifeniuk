import re
from collections import Counter


def remove_marks(request_string: str) -> list:
    # marks = "!.@#$%^&*(){}[]><,|/:;-_+="
    mark = re.sub(r"[^ a-zA-Z]", "", request_string)
    # out_req = "".join(char for char in request_string if char not in marks)
    # return out_req.lower().split()
    return mark.lower().split()


def count_words(request: list) -> dict:
    # dict_count = dict()
    # for item in request:
    #     if item not in dict_count.keys():
    #         dict_count[item] = 1
    #     else:
    #         dict_count[item] += 1
    # return dict_count
    return dict(Counter(request))


def list_of_words():
    text_request = str(input("Enter a string request: "))
    normalize_list_of_words = remove_marks(text_request)
    words_counter = count_words(normalize_list_of_words)
    with open("words.txt", "w") as file:
        for key in words_counter.keys():
            file.write(f"The word: {key} = {words_counter[key]} in text.\n")
    return "Well done! Check the output file."


# text = "Hello!. My na&me is John.
# I h%ave two /high education hell*o. Best regards, Jo;hn."
print(list_of_words())
