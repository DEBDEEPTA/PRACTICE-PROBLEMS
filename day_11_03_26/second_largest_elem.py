
def second_largest(nums):
    unique_nums = list(set(nums))

    if len(unique_nums) < 2:
        return None

    unique_nums.sort()
    return unique_nums[-2]


if __name__ == "__main__":
    nums = list(map(int, input("Enter numbers: ").split()))

    result = second_largest(nums)

    if result is not None:
        print("Second largest:", result)
    else:
        print("No second largest element found")