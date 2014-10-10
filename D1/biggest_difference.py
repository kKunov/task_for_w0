def biggest_difference(arr):
    biggest = arr[0]-arr[1]
    i = 0
    j = 0
    while i < len(arr):
        while j < len(arr):
            if biggest > arr[i] - arr[j]:
                biggest = arr[i] - arr[j]
            j += 1
        i += 1
    return biggest


def main():
    print(biggest_difference(range(100)))


if __name__ == '__main__':
    main()
