P=int(input())
count=0
for i in range(1,P+1):
    if P%i==0:
        count+=1
if count==2:
    print("Prime Number")
else:
    print("Not a Prime Number")


