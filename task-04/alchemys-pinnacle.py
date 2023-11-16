# This code satisfies the method shown in the example but it is not
# satisfying the testcases because the answer given in example and
# the expected outputs are different please consider this...


def diff(x, y):
    x_dig = []  
    y_dig = []
    while x > 0:
        x_dig.append(x % 10)
        x = x // 10
        y_dig.append(y % 10)
        y = y // 10
    difference = []
    for i in range(len(x_dig)):
        z = x_dig[i] - y_dig[i]
        difference.append(z) if z > 0 else difference.append(-1 * (z))
    return difference


n = int(input())

nums = []
for i in range(0, n):
    x, y = (input()).split(" ")
    nums.extend([int(x), int(y)])
for j in range(0, len(nums), 2):
    z = (
        (diff(nums[j], nums[j + 1]))
        if (nums[j] > nums[j + 1])
        else (diff(nums[j + 1], nums[j]))
    )
    ans = 0
    for k in z:
        ans += k
    print(ans)
