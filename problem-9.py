x=int(input("enter a number -> "))
if x%4==0 or (x%100 and x%400):
    print("leap year")
else:
    print("not a leap year ")