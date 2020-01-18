#! usr/bin/python3

import numpy as np

ans = np.array([[2, 1], [6, 3]])
print(ans)

print("Sum of the column 0:")
sum = 0
for i in ans[:, 0]:
    sum += i
print(sum)

print("Sum of column 1:")
sum = 0
for i in ans[:, -1]:
    sum += i
print(sum)