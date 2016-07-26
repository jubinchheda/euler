import fileinput
import math

def lcm(x, y):

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm


def lcmRange(N):
   ret  = 1
   for i in range(1,N,1):
#      print i, ret
      ret=lcm(ret,i)
      print i, ret
   return ret

print lcmRange(40)


