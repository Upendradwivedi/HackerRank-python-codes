def solved_string(s):
    count1=0
    count=[]
    c=[]
    k=[]
    for i in range(len(s)):
        if s[i]==' ':
            count1=count1+1
        elif s[i]!=' ' and count1!=0:
            count.append(count1)
            count1=0
    b=" "
    a=s.split(' ')
    print(a)
    for i in a:
        if i!='':
            k.append(i)
    print(k)
    d=len(c)
    for i in range(len(k)):
        c.append(k[i].capitalize())
    print(c)
    for i in range(len(count)):
        b=b+c[i]+(' '*count[i])
    b=b+c[d-1]
    return b
                
        
    

s=input()
result=solved_string(s)
print(result)

