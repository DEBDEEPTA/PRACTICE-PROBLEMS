def three_sum(nums):
    nums.sort()
    result = []

    for i in range(len(nums)):
        # Skip duplicates for first element
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                result.append([nums[i], nums[left], nums[right]])

                # Skip duplicates for left pointer
                while left < right and nums[left] == nums[left + 1]:
                    left += 1

                # Skip duplicates for right pointer
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1

            elif total < 0:
                left += 1
            else:
                right -= 1

    return result


if __name__ == "__main__":
    # Taking input from user
    nums = list(map(int, input("Enter numbers separated by space: ").split()))

    result = three_sum(nums)

    print("Triplets that sum to 0:")
    for triplet in result:
        print(triplet)