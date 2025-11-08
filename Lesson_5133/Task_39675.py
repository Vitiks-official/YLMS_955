n = int(input())
nums = []
for i in range(n):
    nums.append((int(input()), float(input())))
for i in range(n - 1):
    for j in range(n - i - 1):
        if nums[j][0] < nums[j + 1][0]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
        elif nums[j][0] == nums[j + 1][0]:
            if nums[j][1] < nums[j + 1][1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
for i in nums:
    print(i)