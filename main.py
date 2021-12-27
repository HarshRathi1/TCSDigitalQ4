n,k=map(int,input().split())
arr=list(map(int,input().split()))
pairs=0
for i in arr:
    for j in arr:
       if i-j==k:
           print(i,j)
           pairs+=1
print(pairs)