def is_int_palindrome(n):
    n2 = n
    i = 0
    i2 = 0
    while n2 != 0:
        n2 //= 10
        i += 1
    if i == 1:
        return True
    i //= 2
    n2 = i
    while i2 < i:
        if (n % 10 == 0):
            n2 += pow(10, i2)
        else:
            n2 += (n % 10) * pow(10, i2)
        n //= 10
        i2 += 1
    if i % 2 != 0:
        n //= 10
    n3 = 0
    while i2 > 0:
        n3 = (n2 % 10) * pow(10, i2)
        i2 -= 1
    if n2 == n:
        return True
    return False


def main():
    a = 123321
    print(a)
    print(is_int_palindrome(a))
if __name__ == '__main__':
    main()
