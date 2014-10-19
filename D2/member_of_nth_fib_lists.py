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
