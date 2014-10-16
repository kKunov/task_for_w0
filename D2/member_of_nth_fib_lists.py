def member_of_nth_fib_lists(listA, listB, needle):
    fin_list = []
    if listA == needle:
        return True
    if listB == needle:
        return True
    while len(fin_list) < len(needle):
        fin_list = listA + listB
        listA = listB
        listB = fin_list
    if needle == fin_list:
        return True
    else:
        return False


print(member_of_nth_fib_lists([7,11], [2], [11,7,2,2,7]))
