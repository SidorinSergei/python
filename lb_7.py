#7
n, k =[int(p) for p in input().split()]
b=['I']*n
for i in range(k):
    l,r=[int(p) for p in input().split()]
    for j in range(l-1, r):
        b[j]='.'
print(''.join(b))
