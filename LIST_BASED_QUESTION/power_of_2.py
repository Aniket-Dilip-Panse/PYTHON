def checkPower(number):
    x = 0
    temp = number
    while temp != 1:
        temp = temp // 2
        x = x + 1
    if number == 2**x:
        print("number is power of 2")
    else:
        print("number is not power of 2")
checkPower(8)