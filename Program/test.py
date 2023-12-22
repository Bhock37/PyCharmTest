import math
from matplotlib import pyplot as plt
print(math.sqrt(4))
plt.figure()
data = [0,1,1,1,2,2,5]
plt.hist(data)
plt.show()
plt.savefig('testing.png')
