N = input()
nums = [0] * 10
cnt = 0
for i in range(len(N)):
    num = (int(N[i]))
    if num == 6 or num == 9:
        if nums[6] <= nums[9]:
            nums[6] += 1
        else:
            nums[9] += 1
    else:
        nums[num] += 1
print(max(nums))