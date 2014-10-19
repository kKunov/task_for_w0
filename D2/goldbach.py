def is_prime(n):  # Here I take the is_prime function form first set
    i = 1
    if n < 0:
        n = n * -1
    k = 0
    while i <= n:
        if n % i == 0:
            k += 1
        i += 1
    if k != 2:
        return False
    else:
        return True


def goldbach(n):
    if n % 2 != 0:
        return "Error: Odd number!"
    i = 2
    prime_list = []
    while i < n:
        if is_prime(i):
            j = i
            while j < n:
                if is_prime(j) and j + i == n:
                    prime_list += [(i, j)]
                j += 1
        i += 1
    return prime_list
