# Provides a list of all Armstrong Number in a Given Range

M, N = list(map(int, input().split()))
print([ i for i in range(M, N+1) if sum(list(map(lambda x: int(x) ** 3, list(str(i))))) == i ])