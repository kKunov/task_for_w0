def prime_number_of_divisors(n):
    i = 1
    k = 0
    j = 0
    while i <= n:
        if n % i == 0:
            k += 1
        i += 1
    i = 1
    while i <= k:
        if k % i == 0:
            j += 1
        i += 1
    if j != 2:
        return False
    return True


def main():
    print(prime_number_of_divisors(7))
    print(prime_number_of_divisors(8))
    print(prime_number_of_divisors(9))
if __name__ == '__main__':
    main()
