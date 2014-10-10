def prepare_meal(number):
    n = number
    count = 0
    meal = ""
    while n:
        if n % 3 == 0 and count == 0:
            meal += "spam"
        elif n % 3 == 0 and count != 0:
            meal += " spam"
        else:
            break
        n //= 3
        count += 1
    if number % 5 == 0 and count == 0:
        meal += "eggs"
    elif number % 5 == 0 and count != 0:
        meal += " and eggs"
    return meal

print (prepare_meal(45))
