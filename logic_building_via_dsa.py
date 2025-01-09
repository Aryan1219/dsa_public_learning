"""
step 1 : for the outer loop count the number of rows ,
step 2 : for the inner loop foucs on the columns & connnect them somehow to the rows
step 3: then print the "x" inside the inner loop
step 4 : obsereve symmery optional
"""


def new_line():
    print("\n", end="")

def print_wo_newline(s : str):
    print(s,end='')

def pattern1(n: int):
    for i in range(n):
        for j in range(n):
            print("*", end="")
        print("\n")

def pattern2(n: int):
    for i in range(n + 1):
        for j in range(i):
            print("*", end="")
        new_line()

def pattern3(n: int):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j, end="")
        new_line()

def pattern4(n: int):
    for i in range(1,n+1):
        for j in range(i):
            print(i,end='')
        new_line()

def pattern5(n: int):
    for i in range(1,n+1):
        for j in range(n-i+1):
            print('*',end='')
        new_line()

def pattern6(n: int):
    for i in range(1,n+1):
        for j in range(n-i+1):
            print(j+1,end='')
        new_line()

def pattern7(n: int):
    for i in range(n):
        for _ in range(n-i-1):
            print_wo_newline(' ')
        for _ in range(2*i+1):
            print_wo_newline('*')
        for _ in range(n-i-1):
            print_wo_newline(' ')
        new_line()

def pattern8(n: int):
    for i in range(n):
        for _ in range(i):
            print_wo_newline(' ')
        for _ in range(2*n-(2*i+1)):
            print_wo_newline('*')
        for _ in range(i):
            print_wo_newline(' ')
        new_line()

def pattern9(n: int):

    pattern7(n)
    pattern8(n)
    # for i in range(n):
    #     for _ in range(n-i-1):
    #         print_wo_newline(' ')

    #     for _ in range(2*i+1):
    #         print_wo_newline('*')

    #     for _ in range(n-i-1):
    #         print_wo_newline(' ')
    #     new_line()
    # for i in range(n):
    #     for _ in range(i):
    #         print_wo_newline(" ")
    #     for _ in range(2*n-(2*i+1)):
    #         print_wo_newline('*')
    #     for _ in range(i):
    #         print_wo_newline(" ")
    #     new_line()

def pattern10(n: int):
    upper = (n-n//2)
    lower = n -upper
    for i in range(upper):
        for j in range(i+1):
            print_wo_newline('*')
        new_line()
    for i in range(lower):
        for j in range(lower-i):
            print_wo_newline("*")
        new_line()

def pattern11(n: int):
    for i in range(1,n+1):
        if i%2 != 0:
            for j in range(i):
                if j%2 == 0:
                    print_wo_newline(1)
                else:
                    print_wo_newline(0)
        else:
            for j in range(i):
                if j%2 == 0:
                    print_wo_newline(0)
                else:
                    print_wo_newline(1)
        new_line()

def pattern12(n: int):
    for i in range(n):
        for j in range(i+1):
            print_wo_newline(j+1)
        for _ in range(2*n-(2*(i+1))):
            print_wo_newline(" ")
        for j in range(i+1,0,-1):
            print_wo_newline(j)
        new_line()

def pattern13(n: int):
    num =1
    for i in range(1,n+1):
        for j in range(i):
            print_wo_newline(num)
            print_wo_newline(' ')
            num +=1
        new_line()

def pattern14(n: int):
    
    for i in range(1,n+1):
        alpha = 'A'
        for j in range(i):
            print_wo_newline(alpha)
            alpha = chr(ord(alpha)+1) 
        new_line()

def pattern15(n :int):
    for i in range(n,0,-1):
        alpha = 'A'
        for j in range(i):
            print_wo_newline(alpha)
            alpha = chr(ord(alpha)+1)
        new_line()

def pattern16(n: int):
    alpha = 'A'
    for i in range(1,n+1):
        for j in range(i):
            print_wo_newline(alpha)
        alpha = chr(ord(alpha)+1)   
        new_line()

def pattern17(n:int):
    for i in range(n):
        #spaces
        for _ in range(n-i-1):
            print_wo_newline(' ')

        #chars
        alpha = 'A'
        breakpoint = (2*i+1) //2
        for j in range(1,(2*i+1)+1):
            print_wo_newline(alpha)
            if j <= breakpoint:
                alpha = chr(ord(alpha)+1)
            else:
                alpha = chr(ord(alpha)-1)
        # alpha ='A'
        # max_alpha = ord(alpha)+i
        # rev = False
        # for j in range(2*i+1):
        #     if ord(alpha) <= max_alpha and rev == False:
        #         print_wo_newline(alpha)
        #         alpha = chr(ord(alpha)+1) 
        #     else:
        #         rev =True
        #         if ord(alpha) > max_alpha:
        #             alpha = chr(ord(alpha)-2) 
        #         else:
        #             alpha = chr(ord(alpha)-1) 
        #         print_wo_newline(alpha)



        #spaces
        for _ in range(n-i-1):
            print_wo_newline(' ')
        new_line()

def pattern18(n: int):
    alpha = chr(ord('A')+n-1)
    for i in range(n):
        dummy_alpha = alpha
        for j in range(i+1):
            print_wo_newline(dummy_alpha)
            dummy_alpha = chr(ord(dummy_alpha)+1)
        new_line()
        alpha = chr(ord(alpha)-1)

def pattern19(n: int):
    for i in range(2*n):
        if i < n:
            for j in range(n-i):
                print_wo_newline('*')
            for _ in range(2*i):
                print_wo_newline(' ')
            for j in range(n-i):
                print_wo_newline('*')    
        else:
            i -= n
            for j in range(i+1):
                print_wo_newline("*")
            for _ in range(2*n-(2*(i+1))):
                print_wo_newline(" ")
            for j in range(i+1,0,-1):
                print_wo_newline("*")
        new_line()

def pattern20(n: int):
    for i in range(n):
        for j in range(i+1):
            print_wo_newline('*')
        for _ in range(2*n-(2*(i+1))):
            print_wo_newline(" ")
        for j in range(i+1,0,-1):
            print_wo_newline("*")
        new_line()
    for i in range(1,n):
        for j in range(n-i):
            print_wo_newline('*')
        for _ in range(2*i):
            print_wo_newline(' ')
        for j in range(n-i):
            print_wo_newline('*')  
        new_line()   

def pattern21(n: int):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i == 1 or i == n:
                print_wo_newline('* ')
            else:
                if j == 1 or j== n:
                    print_wo_newline('* ')
                else:
                    print_wo_newline('  ')
        new_line()

def pattern22(n: int):
    matrix = [[0 for _ in range(n*2-1)]for _ in range(n*2-1)] 
    for i in range(2*n-1):
        for j in range(2*n-1):
            matrix[i][j]= min(i,j,2*n-2-j,2*n-2-i)

    for i in range(2*n-1):
        for j in range(2*n-1):
            print(abs(matrix[i][j]-4),end=' ')
        new_line()




if __name__ == "__main__":
    t = int(input())  # Number of test cases
    for _ in range(t):
        n = int(input()) 
        print("\n") # Input for each test case
        pattern22(n)  # Call the appropriate function
