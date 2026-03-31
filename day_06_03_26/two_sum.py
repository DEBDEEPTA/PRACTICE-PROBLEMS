
def two_sum(nums, target):
    num_map = {}   # value -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]

        num_map[num] = i

if __name__=="__main__":
    nums = [2, 7, 11, 15]
    target = 9
    two_sum(nums,target)