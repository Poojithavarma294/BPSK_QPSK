import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erfc

# Eb/N0 values
EbN0_dB = np.arange(0, 13, 2)
EbN0 = 10**(EbN0_dB/10)

# Theoretical BER
BER_BPSK = 0.5 * erfc(np.sqrt(EbN0))
BER_QPSK = 0.5 * erfc(np.sqrt(EbN0))

# Generate symbols
N = 1000

# BPSK symbols
bits_bpsk = np.random.randint(0, 2, N)
bpsk = 2*bits_bpsk - 1

# QPSK symbols
bits_qpsk = np.random.randint(0, 2, 2*N)
bits_pair = bits_qpsk.reshape(2, -1)
I = 2*bits_pair[0] - 1
Q = 2*bits_pair[1] - 1
qpsk = (I + 1j*Q)/np.sqrt(2)

# ---------------- Figure 1 : BER Comparison ----------------
plt.figure(figsize=(7,5))
plt.semilogy(EbN0_dB, BER_BPSK, 'o-b', linewidth=2, label='BPSK')
plt.semilogy(EbN0_dB, BER_QPSK, 's-r', linewidth=2, label='QPSK')
plt.grid(True)
plt.xlabel('Eb/N0 (dB)')
plt.ylabel('Bit Error Rate (BER)')
plt.title('BER Comparison of BPSK and QPSK')
plt.legend()

# ---------------- Figure 2 : BPSK Constellation ----------------
plt.figure(figsize=(5,5))
plt.scatter(np.real(bpsk), np.zeros(N), color='blue')
plt.xlim([-1.5, 1.5])
plt.ylim([-1, 1])
plt.xlabel('In-phase')
plt.ylabel('Quadrature')
plt.title('BPSK Constellation Diagram')
plt.grid(True)

# ---------------- Figure 3 : QPSK Constellation ----------------
plt.figure(figsize=(5,5))
plt.scatter(np.real(qpsk), np.imag(qpsk), color='red')
plt.xlim([-1.5, 1.5])
plt.ylim([-1.5, 1.5])
plt.xlabel('In-phase')
plt.ylabel('Quadrature')
plt.title('QPSK Constellation Diagram')
plt.grid(True)

plt.show()