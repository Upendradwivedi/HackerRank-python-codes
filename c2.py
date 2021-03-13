from collections import Counter
def comp_logo(s):
    my_dict=list(dict(Counter(s)).items())
    c=dict(Counter(s))
    print(my_dict)
    lis=[(j,i) for i,j in my_dict]
    lis=sorted(lis)
    print(lis)
    k=len(lis)-1
    lis3=[]
    for i in range(len(lis)-1,-1,-1):
        lis2=[]
        count=lis[i][0]
        for j in range(len(lis)-1,-1,-1):
            if count==lis[j][0]:
                lis2.append(lis[j][1])
                
        lis3.append(sorted(lis2))
        
    lis4=[]    
    for i in lis3:
        if i not in lis4:
            lis4.append(i)
    print(lis4)
    k=0
    for i in range(len(lis4)):
        for j in range(len(lis4[i])):
            print(lis4[i][j],c[lis4[i][j]])
            k=k+1
            if k==3:
                break
        if k==3:
            break
                      
        
    
    

comp_logo(input())
