
lis=[]
from collections import deque
for i in range(int(input())):
    int(input())
    a=deque(map( int ,input().split()))
    
    
    for i in range(len(a)):
        if len(a)!=0:
            
            d=max(a)
            if a[0]==d:
                a.popleft()
                
            elif a[len(a)-1]==d:
                a.pop()
            else:
                k="No"
            
    if len(a)==0:
        lis.append("Yes")
    else:
        lis.append(k)
print('\n'.join(lis))
