def manual_index(list, element):
    index = 0
    for item in list:
        if item == element:
            return index
        index += 1
    else:
        return 'Error'