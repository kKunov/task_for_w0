def sevens_in_a_row(arr, n):
    i = 0
    k = 0
    while i < len(arr)-1:
        if arr[i] == 7:
            k += 1
        else:
            k = 0
        if k == n:
            return True
        i += 1
    return False


def main():
    print(sevens_in_a_row([10, 8, 7, 6, 7, 7, 7, 20, -7], 3))
if __name__ == '__main__':
    main()
