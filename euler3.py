
N = 600851475143 
residual = N
i=2
maxFactor=2
while (residual>1):
   #print residual, i
   if (residual%i==0):
      residual =residual/i
      maxFactor = i
   else:
      i+=1  

print maxFactor
