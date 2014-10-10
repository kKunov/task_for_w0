def contains_digits(number, digits):
    l = 0
    p = []
    n = number

    while l < len(digits) - 1:
        p[l] == False
        n = number
        while n != 0 or p[l] != True:
            if n % 10 == digits[l]:
                p[l] = True
            n /= 10
        l += 1
    check = len(digits) - 1
    l = 0
    while l < len(digits) - 1:
        if p[l] == True:
            check -= 1
    if check == 0:
        return True
    else:
        return False       
def main():
    print(contains_digits(666, [6,4]))
if __name__ == '__main__':
    main()