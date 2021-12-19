import numpy as np
# generate random maze Of N * N
n = int(input("Enter the value for N ") or "4")
A = np.random.randint(2, size=(n, n))
print(A)

np.savetxt("input.txt", np.array(A), fmt="%s")