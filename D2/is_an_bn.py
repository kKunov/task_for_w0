def is_an_bn(word):
    count_a = 0
    count_b = 0
    for index, char in enumerate(word):
        if char == 'a':
            count_a += 1
        elif char == 'b' and index != len(word) - 1 and word[index + 1] == 'a':
            return False
        elif char == 'b' and (index != len(word) - 1 and \
        word[index + 1] == 'b') or index == len(word) - 1:
            count_b += 1
    if count_a == count_b:
        print("n = ", count_a)
        return True
    else:
        print("a = {} b = {}".format(count_a, count_b))
        return False


print(is_an_bn("aaaaaaaaaabbbbbbbb"))