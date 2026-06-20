import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
N = 128
bits = np.random.randint(0, 2, N)
bpsk = 2*bits - 1

X = np.fft.fftshift(np.fft.fft(bpsk, 2048))
f = np.linspace(-0.5, 0.5, len(X))

plt.figure(figsize=(8, 3))
plt.plot(f, np.abs(X), linewidth=2)
plt.title("Layer 2: Spectrum of BPSK Signal")
plt.xlabel("Normalized Frequency")
plt.ylabel("Magnitude")
plt.grid(True)
plt.tight_layout()
plt.show()