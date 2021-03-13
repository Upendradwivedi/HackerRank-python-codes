from itertools import combinations
s,b=input().split()
s=list(s)
b=int(b)
for i in range(1,b+1):
    f=[]
    d=list(combinations(s,i))
    for i in range(len(d)):
        f.append(''.join(sorted(d[i])))
    f=sorted(f)
    print('\n'.join(f))
        
        
