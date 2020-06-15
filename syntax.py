def is_correct(word, __formats):
    flag = True
    for __format in __formats:
        if len(__format) != len(word):
            flag = False
            continue
        for target, base in zip(word, __format):
            if target.isdigit() and not base.isdigit():
                break
            if not target.isdigit() and base.isdigit():
                break
        return True
    return flag
