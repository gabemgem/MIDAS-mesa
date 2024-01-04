import numpy as np

m = { 'network': np.zeros(5)}
print(m)

t = m['network']
t[1] = 2
print(m)