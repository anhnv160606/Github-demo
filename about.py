def C_F(n, x):
    if x==1:
        degree = float(n*9/5) + 32
    else:
        degree = float(n*5/9) - 32

    return degree

print("Enter 1 if you want to convert C degree to F degree/n "
      "Enter 2 if you want to convert F degree to C degree ")
x = int(input("Enter the number to choose mode(1/2): "))

while x!=1 and x!=2:
    print("Error! Please enter 1 or 2")
    x = int(input("Enter the number to choose mode(1/2): "))
n = float(input("enter the number of degree: "))

print(C_F(n, x))


