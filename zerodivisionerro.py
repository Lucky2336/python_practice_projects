try:
   a = int(input("enter 1st no:"))
   b = int(input("enter 2nd no:"))
   print(a/b)
except ZeroDivisionError as v:
   print("infinite")   
   