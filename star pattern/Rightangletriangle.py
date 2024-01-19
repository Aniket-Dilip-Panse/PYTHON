num = int(input("enter number of rows: "))
for row in range(1, num+1):
    print("* "*row)

num2 = int(input("enter number of rows: "))
k=1
for row in range(1,num2+1):
    for col in range(1,k+1):
        print("* ",end=" ")
    k = k + 2
    print(" ")