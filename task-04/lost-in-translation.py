s = input()
s = s.lower()
ref = "hello"
count =0
for i in s:
    if (i=='h'and count==0):
        count+=1
    elif (i=='e' and count==1):
        count+=1
    elif (i=='l' and count==2):
        count+=1
    elif (i=='l' and count==3):
        count+=1
    elif (i=='o' and count==4):
        count+=1
if count==5:
    print("YES")
else:
    print("NO")