# Accepting User Inputs

# raw input( ) accepts input and stores it as a string. Hence, if the user inputs a integer, the code should convert the string to an integer and then proceed.
abc = raw_input("Type something here and it will be stored in variable abc \t")
print( type(abc)) # str

#input( ), this is used only for accepting only integer inputs.
abc1 = input("Only integer can be stored in in variable abc \t")
print( type(abc1) ) # int

# Note that type( ) returns the format or the type of a variable or a number


# Space Separated integers to a List
lis = list(map(int, input().split()))
print(lis)
# > 1 2 3 4 5 6 7 8    # [1, 2, 3, 4, 5, 6, 7, 8]


## Taking Two Integers as input
a,b = map(int,input().split())
print("a:",a)
print("b:",b)

## Taking a List as input
arr = list(map(int,input().split()))
print("Input List:",arr)