def is_anagram(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    return sorted(str1) == sorted(str2)


if __name__ == "__main__":
    first = input("Enter first string: ")
    second = input("Enter second string: ")

    if is_anagram(first, second):
        print("The strings are anagrams.")
    else:
        print("The strings are not anagrams.")