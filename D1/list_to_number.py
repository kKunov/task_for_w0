def list_to_number(list):
    number = 0
    big_index = len(list) - 1
    small_index = 0
    while small_index < len(list):
        number += list[small_index] * pow(10, big_index)
        small_index += 1
        big_index -= 1
    return number


def main():
    print(list_to_number([1, 2, 3, 4, 5, 6]))


if __name__ == '__main__':
    main()
    