def simplify_fraction(fraction):
    index = 2
    while index <= fraction[0]:
        if fraction[0] % index == 0 and fraction[1] % index == 0:
            fraction[0] //= index
            fraction[1] //= index
        index += 1
    return fraction


print(simplify_fraction([63, 462]))
