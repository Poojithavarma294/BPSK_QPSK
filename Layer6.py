import numpy as np
import matplotlib.pyplot as plt

EbN0_dB = np.arange(0, 11, 2)
snr = 10**(EbN0_dB/10)
capacity = np.log2(1 + snr)

plt.figure(figsize=(8, 4))
plt.plot(EbN0_dB, capacity, 'o-', linewidth=2)
plt.title("Layer 6: Shannon Capacity")
plt.xlabel("Eb/N0 (dB)")
plt.ylabel("Capacity (bits/s/Hz)")
plt.grid(True)
plt.tight_layout()
plt.show()