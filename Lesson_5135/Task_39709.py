nums = list(map(int, input().split()))
ans = [str(nums[0])]
n = nums[0]
for i in nums:
    if n < i:
        n = i
        ans.append(str(i))
print(">>".join(ans))