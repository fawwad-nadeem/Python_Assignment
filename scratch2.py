import numpy as np
from numpy import random
f=np.array([[[1,2,3], [4,5, 6], [7, 8, 9]],
  [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
  [[0, 0, 0], [0, 0, 0], [0, 0, 0]]])
print(f[:,0])
a=np.array_split(f,3,axis=0)
print(a)
c=a[:][0][0]
print(c[0][1])
g=np.array([1,3,4,5,76,78,8,0,3,4,7,9])
print(np.sort(g))
y=np.where(g==4)
print(y)
#i=random.randiant(100,size=(3,3))
j=random.choice([1,2,3,4,5],p=[0.6,0.1,0.1,0.1,0.1],size=(50,50))
print(j)
random.normal(size=(3,3))