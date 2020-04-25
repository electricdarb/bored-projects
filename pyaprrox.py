import random
import numpy as np
N = 1000
c = 0
for i in range(N):
    x = random.random()
    y = random.random()
    if (x**2 + y**2)**.5 < 1:
        c+=1
print(np.__all__)