from itertools import product

# taking first two input
K,M = map(int,input().split())

# making a list containing k nested lists
N = (list(map(int, input().split()))[1:] for _ in range(K))

#using lamda to make function writing more easy and comfortable
results = map(lambda x: sum(i**2 for i in x)%M, product(*N))

#taking the output
print(max(results))
