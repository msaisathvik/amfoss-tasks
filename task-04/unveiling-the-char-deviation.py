ref = "amfoss"
x = int(input())
for i in range(x):
    y = input()
    count = 0
    for j in range(6):
        if y[j]!=ref[j]:
            count+=1
    print(count)

