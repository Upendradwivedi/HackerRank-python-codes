from collections import Counter
N=int(input())
a=map(int,input().split())
a=list(a)
n1=int(input())
lis1=[]
lis2=[]

for i in range(n1):
    c,b=input().split()
    lis1.append(int(c))
    lis2.append(int(b))
lis3=[lis1]+[lis2]
k=list(zip(*lis3))
lis4=[(k[i][0],k[i][1]) for i in range(len(k)) if k[i][0] in a]
l=dict(Counter(a))
sum1=0
for i in range(len(lis4)):
    count=l[lis4[i][0]]
    if count!=0:
        sum1=sum1+lis4[i][1]
        l[lis4[i][0]]=count-1
print(sum1)


