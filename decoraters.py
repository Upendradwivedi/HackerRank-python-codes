def sort_phone(l):
    print(*sorted(l), sep="\n")
def wrapper(f):
    def fun(l):
        lis2=[]
        for i in range(len(l)):
            p=[]
            if len(l[i])>=10:
                k=len(l[i])-10
                for j in range(k,len(l[i])):
                    p.append(l[i][j])
            p.insert(5,' ')
            lis2.append('+91'+' '+"".join(p))
        lis2.sort()
        f(lis2)
    return fun
sort_phone=wrapper(sort_phone)
l=[input() for i in range(int(input()))]
sort_phone(l)

                
        
        
