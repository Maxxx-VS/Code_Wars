import random
def lineup_students(nums):
    if len(nums) <= 1:
        return nums
    else:
        pivot = random.choice(nums)
        left_nums, right_nums, middle_nums = [], [], []
        for i in nums:
            if len(i) > len(pivot):
                left_nums.append(i)
            elif len(i) < len(pivot):
                right_nums.append(i)
            else:
                middle_nums.append(i)
    return lineup_students(left_nums) + middle_nums + lineup_students(right_nums)


string = 'Tadashi Takahiro Takao Takashi Takayuki Takehiko Takeo Takeshi Takeshi'
ssr = string.split()
ssr = lineup_students(ssr)


for i in ssr:
    for j in range(len(ssr) + 1):
        if len(i)[j] == len(i)[j+1]:
            i[::-1]
            print(i)


print(ssr)


