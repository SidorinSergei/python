#6
x = int(input())
n=0
b=0
c=0
while x!=0:
    n=n+1
    b=b+x
    c+=x**2
    x=int(input())
print(math.sqrt((c-b/n)/(n-1)))
