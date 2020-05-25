import subprocess
from numpy.linalg import solve
import numpy as np
FLAG_start="ctf4b"

def dot(A, B):
    assert len(A) == len(B)
    return sum([a * b for a, b in zip(A, B)])




ans=np.array([0]*44)
loop=100
count=0
for i in range(loop):
  t=subprocess.check_output(['nc','noisy-equations.quals.beginners.seccon.jp','3000'])
  t=t.decode().replace('\n',',')

  x=eval(t)
  l=np.array(x[0],dtype = 'float')
  r=np.array(x[1],dtype = 'float')
  print(ord('c'))
  a=solve(l,r)
  if abs(a[0]-99)<10:
    ans=np.append(ans,a,axis=0)
    print(a)
    count+=1


print(ans.reshape(44,-1).shape)
print('median')
print(np.median(ans.reshape(-1,44),axis=0))
for ch in np.median(ans.reshape(-1,44),axis=0):
  print(chr(int(ch+0.5)),end='')
print()
