def count_consonants(s):
    s = s.lower()
    con = 'qwrtpsdfghjklzxcvbnm'
    count = 0
    for char in con:
        count += s.count(char)
    return count


def main():
    print(count_consonants("Theistareykjarbunga"))

if __name__ == '__main__':
    main()
