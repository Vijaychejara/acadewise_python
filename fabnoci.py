n1, n2 = 0, 1
count = 0
while count < 20:
    print(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count+= 1
if n1==101:
    print("exist")
else:
    print("not exist")
  
    