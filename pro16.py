#write a program to enter time in 24 hour and display in it.

hours=int(input("Enter hour:"))

if hours<=12:
    print("Hours are:",hours)
if hours>=12:
    print("Hours are:",hours-12)

if hours>24:
    print("invalid")