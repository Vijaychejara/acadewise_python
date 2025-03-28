x = input()
print(x)
if x.isdigit():
    print("integer")
elif "." in x:
    if  x.count('.') == 1:
        # print("FLOAT")
        a,b = x.split(".")
        if a.isdigit() and b.isdigit():
            # print("float")
            if float(x).is_integer():
                print("intiger") # Output: True
            else:
                print("Float")  
        else:
            print("string")
    else:
        print("string")
else:
    print("string")
