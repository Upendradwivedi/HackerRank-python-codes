def code():
     a=int(input())
     b=set(map(int,input().split()))
     c=int(input())
     d=set(map(int,input().split()))
     e=list(b.difference(d))
     f=list(d.difference(b))
     c=e+f
     c=sorted(c)
     d=list(map(str,c))
     print('\n'.join(d))


