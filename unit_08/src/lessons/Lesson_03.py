def reverse_string(str_to_reverse):
    return str_to_reverse[::-1]

isEven = lambda x: x%2==0

def task_answer(xs):
    oddList = []
    for string in xs:
        if not isEven(len(string)):
            oddList.append(reverse_string(string))
    return oddList


if __name__ == "__main__":
    str_list = ["this", "IS", "a", "list", "of", "a", "few", "strings"]
    result = task_answer(str_list)
    print(result)  # should print ['a', 'a', 'wef', 'sgnirts']