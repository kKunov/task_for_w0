def contains_digit(number, digit):
#    l = 0
 #   n = number
  #  while n:
   #     n /= 10
    #    l += 1
    while number:
        if number % 10 == digit:
            return True
        number /= 10
    return False
def main():
    print(contains_digit(5 ,5))
if __name__ == '__main__':
    main()