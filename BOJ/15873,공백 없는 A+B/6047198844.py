nums = input()
tmp = ''
for i in range(len(nums)):
    if 0 <= int(tmp + nums[i]) <= 10:
        tmp += nums[i]
    else:
        print(int(nums[:i]) + int(nums[i:]))
        break
