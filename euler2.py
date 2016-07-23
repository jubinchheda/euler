
curr = 1
next1 = 2
temp = 0
sum1 = 0

while(next1<=4000000):
   if next1%2==0:
      sum1+=next1
#   print next1, sum1
   temp = curr
   curr = next1
   next1 = temp+curr

print sum1
