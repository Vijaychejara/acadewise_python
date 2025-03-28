# Multiplication table (from 1 to 10) in Python



# To take input from the user
# num = int(input("Display multiplication table of? "))

# Iterate 10 times from i = 1 to 10
for number in range(100):
    
    k=len(str(number))
    
    sum=0
    while k>0:
        sum+= int(str(number)[k-1])
        k-=1
    if sum != 9:
        print(number)


    


