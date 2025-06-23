def amounts(list):
    for item in set(list):
        return f"{item} - {list.count(item)}"