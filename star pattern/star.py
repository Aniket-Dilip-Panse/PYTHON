def pattern1(rows): 
    print("star pattern 1") 
    for i in range(1, rows+1): 
        print("*"*i)  
# pattern1(5)

def pattern2(rows):   
     print("star pattern 2")    
     for i in range(1,rows+1):        
        print(" "*(rows-i) + "*"*i)
# pattern2(5)

def pattern3(rows):    
    print("star pattern 3")    
    for i in range(rows,0,-1):        
        print("*"*i)
# pattern3(5)

def pattern4(rows):    
    print("star pattern 4")    
    for i in range(rows,0,-1):       
        print(" "*(rows-i)+"*"*i)
# pattern4(5)

def pattern5(rows):    
    print("star pattern 5")    
    k = 1    
    for i in range(1,rows+1):        
        print(" "*(rows-i) + "*"*k)        
        k = k + 2
# pattern5(5)

def pattern6(rows):    
    print("star pattern 6")    
    k = 1    
    for i in range(rows,0,-1):        
        k = (i * 2) -1        
        print(" "*(rows-i)+"*"*k)        
# pattern6(5)        

def pattern7(rows):    
    print("star pattern 7")    
    k = 1    
    for i in range(1,rows+1):        
        print(" "*(rows-i) + "*"*k)        
        k=k+2    
    for i in range(rows-1,0,-1):        
        k = (i*2) - 1        
        print(" "*(rows-i) + "*"*k)
# pattern7(5)

def pattern8(rows):
    for i in range(1,rows+1):
        print("*"*i)
    for j in range(rows-1,0,-1):
        print("*"*j)
# pattern8(5)

def pattern9(rows):
    for i in range(1,rows+1):
        print(" "*(rows-i) + "*"*i)
    for j in range(rows-1,0,-1):
        print(" "*(rows-j) + "*"*j)
# pattern9(5)

def pattern10(rows):
    for i in range(1,rows+1):
        print(" "*(rows-i) + "*"*rows)
# pattern10(5)

def pattern11(rows):
    for i in range(rows,0,-1):
        print(" "* (rows-i) + "*"*rows)
# pattern11(5)

def pattern12(rows):
    for i in range(rows,0,-1):
        print("*"*i)
    for j in range(1,rows+1):
        print("*"*j)
# pattern12(5)

def pattern13(rows):
    print('star pattern 13')
    for i in range(rows,0,-1):
        print(" "*(rows-i) + "*"*i)
    for j in range(2,rows+1):
        print(" "*(rows-j) + "*"*j)
# pattern13(5)

def pattern14(rows):
    print('star pattern 14')
    for i in range(rows,0,-1):
        print(" "*(rows-i) + "* "*i)
    for j in range(2,rows+1):
        print(" "*(rows-j) + "* "*j)
# pattern14(5)

def pattern15(rows):
    print("star pattern 15")
    for i in range(1,rows+1):
        for j in range(1,i+1):
            if i==j or j==1 or i==rows:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print(' ')
# pattern15(5)

def pattern16(rows):
    print("star pattern 16")
    for i in range(1,rows+1):
        for j in range(1,rows+1):
            if j==rows or i==rows or i+j==rows+1: 
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print(' ')
# pattern16(5)

def pattern33(rows):
    print("pattern 33")
    for i in range(1,rows+1):
        for j in range(1,rows+1):
            if i==(rows//2)+1 or j==(rows//2)+1:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print(" ")
# pattern33(9)

def  random_pattern():
    for row in range(1, 8):
        for col in range(1, 14):
            if row == 7 or col == 7 or row + col == 8 or col - row == 6:
                print("*", end=" ")
            else:
                print(end=" ")
        print(" ")
# random_pattern()


def hardPattern(rows):
    for i in range(1,rows+1):
        for j in range(1,rows+1):
            if j<i:
                print("")
            elif j==1:
                print(i)
# hardPattern(5)
