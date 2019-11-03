#1 left rotation
nd = input().split()
n = int(nd[0])
d = int(nd[1])
a = list(map(int, input().rstrip().split()))

temp = []
x = 0
for i in range(d):
    temp.append(a[i])


for j in range(n):
    if(d < n):
        a[j] = a[d]
        d+=1
    else:
        a[j] = temp[x]
        x+=1


y = ' '.join(str(e) for e in a)

print(y)

https://www.hackerrank.com/challenges/array-left-rotation/submissions/code/129314095
