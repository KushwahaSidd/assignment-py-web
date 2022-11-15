m=int(input("Enter a month number"))
match m:
    case m if m in (1,3,5,7,8,10,12):
        print("31 day")
    case m if m in (4,6,9,11):
        print("30 day")
    case 2:
        print("28 of 29 day")
    case _:
        print("Invalid months number")
        
