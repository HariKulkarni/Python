#python prog tocheck if a number is positive,negative or zero

def numbercheck(a):
    if a>0:
        print("Number given by you is positive")
    elif a<0:
        print("Number given by you is Negative")
    else:
        print("Number given by you is zero")
a=float(input("Enter a number as input value: "))
numbercheck(a)
        
