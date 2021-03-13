N,M=list(map(int,input().split()))
lis=[]
for i in range(N):
    k=list(map(int,input().split()))
    lis.append(k)
k1=int(input())
lis2=[]
for i in range(N):
    lis2.append(lis[i][k1])
lis2=list(map(int,lis2))
lis2.sort()
lis3=[]
for i in lis2:
    for j in range(N):
        if i == lis[j][k1]:
            k=lis[j]
            if k not in lis3:
                print(' '.join(list(map(str,k))))
                lis3.append(k)
                
        
    
    

