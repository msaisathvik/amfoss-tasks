x = int(input())
lst = []
nums = []
count = 0
for i in range(0, x):
    lst = (input()).split(" ")
    nums.append(lst)
    if int(nums[i][0]) + int(nums[i][1]) + int(nums[i][2]) == 0:
        count += 1
if count == x:
    print("YES")
else:
    print("NO")
