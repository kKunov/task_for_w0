def sum_of_digits(n):
    summ = 0
    if n < 0:
        n *= -1
    while n:
        summ += n % 10
        n = n // 10
    return summ


def main():
    print(sum_of_digits(-123))
if __name__ == '__main__':
    main()
