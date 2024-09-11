# even_odd check
input1=int(input("enter the number "))
def even_odd(x):
    y=lambda a:a%2==0
    if y(input1):
        print("even")
    else:
        print("odd")
even_odd(input1)