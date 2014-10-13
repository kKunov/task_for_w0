def reduce_lines(path):
    new_path = ""
    for index, element in enumerate(path):
        if index != 0 and \
            ((element == '/' and new_path[len(new_path)-1] != '/') or element != '/') and \
            ((index == len(path) - 1 and element != '/') or index != len(path) - 1):
            new_path += element
        elif index == 0:
            new_path += element
    return new_path


def reduce_double_dot(path):
    new_path = ""
    new_path2 = ""
    i = 0
    i2 = 0
    i3 = 0
    for index, element in enumerate(path):
        if element == "." and index != len(path) - 1 and path[index + 1] == ".":
            i2 = len(new_path) - 1
            while i <= 1:
                if new_path[i2] == '/':
                    i += 1
                i2 -= 1
            i2 += 1
            while i3 <= i2:
                new_path2 += new_path[i3]
                i3 += 1
            new_path = ""
            for el in new_path2:
                new_path += el
            i = 0
            i2 = 0
            i3 = 0
        else:
            new_path += element
    return new_path


def reduce_single_dot(path):
    new_path = ""
    for index, element in enumerate(path):
        if index != 0 and element != ".":
            new_path += element
        elif index == 0:
            new_path += element
    #path = ""
    #path = new_path
    return new_path


def reduce_file_path(path):
    path = reduce_double_dot(path)
    path = reduce_single_dot(path)
    path = reduce_lines(path)
    path = reduce_lines(path)
    return path


print(reduce_file_path("/srv/..//asd/asd/./ads"))
