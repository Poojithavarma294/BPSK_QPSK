import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
N = 16
bits = np.random.randint(0, 2, N)
bpsk = 2*bits - 1

plt.figure(figsize=(8, 3))
plt.step(np.arange(N), bpsk, where='mid', linewidth=2)
plt.ylim(-1.5, 1.5)
plt.yticks([-1, 1], ['-1', '+1'])
plt.title("Layer 1: BPSK Signal Representation")
plt.xlabel("Bit Index")
plt.ylabel("Amplitude")
plt.grid(True)
plt.tight_layout()
plt.show()