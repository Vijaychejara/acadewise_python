a = input()
k = len(a)
print(k)

print(type(a))
sum=0
while k>0:
    sum+=int(a[k-1])
    k-=1
print(sum)
