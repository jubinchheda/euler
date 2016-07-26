import fileinput
import math

def largestPrimeFactor(N):
   residual = N
   i=2
   maxFactor=2
   root = math.sqrt(N)
   while (i<=root):
   #print residual, i
      if (residual%i==0):
         residual =residual/i
         maxFactor = i
      else:
         i+=1
   if i>=root and residual>i:
      return N
   else:
      return maxFactor

stringList=[]
paramList=[]

for line in fileinput.input():
   stringList.append(line.rstrip())

stringList.pop(0)

for item in stringList:
   print largestPrimeFactor(int(item))


