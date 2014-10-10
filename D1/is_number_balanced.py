def is_number_balanced(n):
    index = 0
    index2 = 0
    right = n
    left = 0
    n2 = n
    left_sum = 0
    right_sum = 0
    while n2:
        n2 //= 10
        index += 1
    if index % 2 != 0 and index != 1:
        index -= 1
    if index != 1:
        index //= 2
    n2 = n
    while index2 < index:
        right = (n2 % 10) * pow(10, index2)
        n2 //= 10
        index2 += 1
    if index % 2 != 0 and index != 1:
        left = n2 // 10
    else:
        left = n2
    while right:
        right_sum += right % 10
        right //= 10
    while left:
        left_sum += left % 10
        left //= 10
    if left_sum == right_sum:
        return True
    else:
        return False


def main():
    print(is_number_balanced(121))
if __name__ == '__main__':
    main()
