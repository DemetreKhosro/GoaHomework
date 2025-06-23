def manual_count(list, element):
    count = 0
    for item in list:
        if item == element:
            count += 1
    return count


print(manual_count([1, 1, 1, 2, 3, 4, 5], 1))