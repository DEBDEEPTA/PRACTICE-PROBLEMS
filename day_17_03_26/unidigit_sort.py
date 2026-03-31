def sort_by_unit_digit(nums):
    return sorted(nums, key=lambda x: x % 10)


if __name__ == "__main__":
    nums = list(map(int, input("Enter numbers: ").split()))

    result = sort_by_unit_digit(nums)

    print("Sorted by unit digit:", result)