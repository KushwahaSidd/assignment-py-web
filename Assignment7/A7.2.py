print("1.Addition")
print("2.Substraction")
print("3.Multiplication")
print("4.Divisons")
print("\nEnter your choice")
ch=int(input())
def add():
    print("Enter two numbers")
    a=int(input())
    b=int(input())
    c=a+b
    print("sum is ",c)
def substract():
    print("Enter two Number")
    a=int(input())
    b=int(input())
    c=a-b
    print("Substract is ",c)
def multiply():
    print("Enter two number")
    a=int(input())
    b=int(input())
    c=a*b
    print("multiply is ",c)
def division():
    print("Enter two number")
    a=int(input())
    b=int(input())
    c=a//b
    print("divide is ",c)
match ch:
    case 1:
         add()
    case 2:
        substract()
    case 3:
        multiply()
    case 4:
        division()



