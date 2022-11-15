def palindrome(str1):
    if str1==str1[::-1]:
        return 1
    else:
        return -1

s=input("Enter the string")
r=palindrome(s)
if r==1:
    print("palindrome")
else:
    print("Not palindrome")
