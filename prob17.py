# 5. Reverse a string (2 ways)
# Using slicing ([::-1])
# Using loop

x = input("Enter the String: ")

for i in range(len(x)-1,-1,-1):
    print(x[i],end="")
    # a = x[i]
    # print(a) 