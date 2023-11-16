x = int(input())
numbers_list = list(map(int, input().split(" ")))
minimum = numbers_list[0]
count = 1
for i in range(1, x):
    if numbers_list[i] <= minimum:
        if numbers_list[i] == minimum:
            print("Still Aetheria")
            count = 0
            break
        else:
            minimum = numbers_list[i]
            count = i + 1
if count:
    print(count)
