def number_to_list(num):
    count = []
    count.str(num)
    n = num
    i = len(num)-1
    while i >= 0:
        count.insert(n // pow(10, i))
        n = num % pow(10, i)
    return count


def main():
    print(number_to_list(1234))


if __name__ == '__main__':
    main()
