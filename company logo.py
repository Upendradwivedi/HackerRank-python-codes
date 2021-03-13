from collections import Counter
def comp_logo(s):
    my_dict=list(dict(Counter(s)).items())
    print(my_dict)
    lis=[(j,i) for i,j in my_dict]
    lis=sorted(lis)
    k=len(lis)-1
    lis3=[]
    for i in range(len(lis)-1,-1):
        lis2=[]
        for j in range(i,-1):
            if lis[j][0]==lis[i][0]:
                print("K")
                lis2.append(lis[j][1])
            lis3.append(lis2.sort())
    print(lis3)
    
    

comp_logo(input())
