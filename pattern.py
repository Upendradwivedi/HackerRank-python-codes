n=int(input())
a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
c=[]
d=[]
for i in range(n-1,-1,-1):
    c.insert(n-i-1,a[i])
    f=list("".join(c) + "".join(d))
    print('-'*(i*2) + '-'.join(f) + '-'*(i*2))
    d.insert(0,a[i])
del(d[0])
for i in range(1,n):
    del(c[n-i])
    del(d[0])
    f=list(''.join(c) + ''.join(d))
    print('-'*(i*2)+'-'.join(f) + '-'*(i*2))
