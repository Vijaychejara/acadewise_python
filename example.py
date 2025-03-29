# Multiplication table (from 1 to 10) in Python



# To take input from the user
# num = int(input("Display multiplication table of? "))

# Iterate 10 times from i = 1 to 10
'''for number in range(100):
    
    k=len(str(number))
    
    sum=0
    while k>0:
        sum+= int(str(number)[k-1])
        k-=1
    if sum != 9:
        print(number)'''
'''n = input()
n = int(n)
fact = 1

for i in range(1, n+1):
    fact = fact * i

print("The factorial of n is : ", end="")
print(fact)'''
num = input()
num = int(num)
flag = 0
for i in range(2,num):
  print(i)
  if num%i==0:
    flag = 1
    break
if flag == 1:
  print('Not Prime')
else:
  print("Prime")



    


