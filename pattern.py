'''n = 3
for i in range(n):
    print( " "*(n-i-1) + "*"*(2*i+1) )'''
'''n=3
for i in range(n):
    for j in range(1):
        if j>i:
            print( " "*(n-i-1),end='')
        else:
            print("*"*(2*i+1))
num = int(input("Enter a number of rows: "))
for i in range(0,num):
    for j in range(0,num-i-1):
        print(end=" ")
    for j in range(0,1+i):
        print("*", end=" ")
    print()'''
# ch = ord("A")
# h = ord("A")
# k, j, m = 0, 0, 0
# while k < 7:
#     while j < 7:
#         if k < j:
#             print(" ", end="")
#         else:
#             if ch > ord("Z"):
#                 print(" ", end="")
#             else:
#                 print(chr(ch), end="") 
                    
#             ch += 1
#         j += 1
#     j = 0  # Reset j for the next row
    
#     # Adjust spacing to create a proper mirror image
#     while m < 7:
#         if m < (6 - k):  # Adjust the spacing logic here
#             print(" ", end="")
#         else:
#             if h > ord("Z"):
#                 print(" ", end="")
#             else:
#                 print(chr(h), end="")
            
#             h += 1
#         m += 1
#     m = 0  # Reset m for the next row
    
#     print()
#     k += 1
    
    
    
    

rows = 3  # Number of rows
ch = ord('A')  # Start with ASCII of 'A'

for i in range(rows):
    # Print leading spaces for right alignment
    for space in range(rows - i - 1):
        print(" ", end="")

    # Print characters in reverse order
    temp_ch = ch + i  # Track starting character for each row
    for j in range(i + 1):
        print(chr(temp_ch), end="")
        temp_ch -= 1  # Move backward in characters

    print()  # Move to the next line