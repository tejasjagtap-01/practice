# Take a string and print reverse character one by one using loop

x = input("Enter the String: ")

for i in range(len(x)-1,-1,-1):
    a = x[i]
    print(a)