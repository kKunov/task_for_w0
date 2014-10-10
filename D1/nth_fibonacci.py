def nth_fibonacci(n):
    a = 1
    b = 0
    i = 0
    c = 0
    if i == 1:
        return a
    else:
        n -= 1

    while i < n:
        c = a
        a = a + b
        b = c
        i += 1
    return a


def main():
    print(nth_fibonacci(1))
    print(nth_fibonacci(2))
    print(nth_fibonacci(3))
    print(nth_fibonacci(4))
    print(nth_fibonacci(5))
    print(nth_fibonacci(6))
    print(nth_fibonacci(7))
    print(nth_fibonacci(8))
    print(nth_fibonacci(9))
    print(nth_fibonacci(10))


if __name__ == '__main__':
    main()
