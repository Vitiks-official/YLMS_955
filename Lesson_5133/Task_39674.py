nums = []
num = int(input())
while num != 0:
    nums.append(num)
    num = int(input())
for i in range(len(nums) - 1):
    for j in range(len(nums) - i - 1):
        if nums[j] < nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
for i in nums[:-1]:
    print(f"{i}->", end="")
print(nums[-1])