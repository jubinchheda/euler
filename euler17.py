
def factorial(n):
   if n==0:
      return 1
   else:
      return n*factorial(n-1)


Lst = list (str (factorial(100)))
Sum=0
for item in Lst:
   Sum+=int (item)
 
print Sum
