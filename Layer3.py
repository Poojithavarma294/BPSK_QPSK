import numpy as np
import matplotlib.pyplot as plt

def add_awgn(x, ebn0_db):
    ebn0 = 10**(ebn0_db/10)
    noise_std = np.sqrt(1/(2*ebn0))
    return x + noise_std*np.random.randn(len(x))

np.random.seed(0)
N = 20
bits = np.random.randint(0, 2, N)
tx = 2*bits - 1
rx = add_awgn(tx, 5)

plt.figure(figsize=(8, 3))
plt.plot(tx, 'o-', label='Transmitted')
plt.plot(rx, 's-', label='Received')
plt.title("Layer 3: BPSK Through AWGN Channel")
plt.xlabel("Sample")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()