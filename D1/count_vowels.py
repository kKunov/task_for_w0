def count_vowels(s):
    vowels = 0
    vowels += s.count("a")
    vowels += s.count("e")
    vowels += s.count("y")
    vowels += s.count("o")
    vowels += s.count("u")
    vowels += s.count("i")
    return vowels


def main():
    print(count_vowels("Pthsdfn"))


if __name__ == '__main__':
    main()
