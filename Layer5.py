import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erfc

def add_awgn(x, ebn0_db):
    ebn0 = 10**(ebn0_db/10)
    noise_std = np.sqrt(1/(2*ebn0))
    return x + noise_std*np.random.randn(len(x))

np.random.seed(0)
EbN0_dB = np.arange(0, 11, 2)
N = 100000
BER = []

for snr_db in EbN0_dB:
    bits = np.random.randint(0, 2, N)
    tx = 2*bits - 1
    rx = add_awgn(tx, snr_db)
    detected = (rx > 0).astype(int)
    BER.append(np.mean(bits != detected))

BER_theory = 0.5 * erfc(np.sqrt(10**(EbN0_dB/10)))

plt.figure(figsize=(8, 4))
plt.semilogy(EbN0_dB, BER, 'o-', label='Simulated')
plt.semilogy(EbN0_dB, BER_theory, '--', label='Theory')
plt.title("Layer 5: BER Performance of BPSK")
plt.xlabel("Eb/N0 (dB)")
plt.ylabel("BER")
plt.legend()
plt.grid(True, which='both')
plt.tight_layout()
plt.show()