# palindrome check
def palindrome():
    y=lambda a: a[::-1]==a
    input1=input("enter the string ")
    if y(input1):
        print("palindrome")
    else:
        print("not palindrome")
palindrome()
