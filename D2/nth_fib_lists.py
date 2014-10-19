def nth_fib_lists(list_A, list_B, n):
    index = 2
    fin_list = []
    if n == 1:
        return list_A
    elif n == 2:
        return list_B
    while index < n:
        fin_list = list_A + list_B
        list_A = list_B
        list_B = fin_list
        index += 1
    return fin_list

#print(nth_fib_lists([1, 2], [1, 3], 3))
