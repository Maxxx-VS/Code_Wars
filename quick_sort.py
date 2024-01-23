import random
def quick_sort(nums):
    if len(nums) <= 1:
        return nums
    else:
        pivot = random.choice(nums)
        left_nums, right_nums, middle_nums = [], [], []
        for i in nums:
            if i < pivot:
                left_nums.append(i)
            elif i > pivot:
                right_nums.append(i)
            else:
                middle_nums.append(i)
    return quick_sort(left_nums) + middle_nums + quick_sort(right_nums)

print(quick_sort([6, 5, 1, 3 ,8 ,4, 7, 9, 2]))






def quick_sort_2(nums):
    if len(nums) <= 1:
        return nums
    else:
        pivot = random.choice(nums)
    left_nums = [i for i in nums if i < pivot]
    middle_nums = [pivot] * nums.count(pivot)
    right_nums = [i for i in nums if i > pivot]
    return quick_sort(left_nums) + middle_nums + quick_sort(right_nums)


print(quick_sort_2([6, 5, 1, 3 ,8 ,4, 7, 9, 2]))