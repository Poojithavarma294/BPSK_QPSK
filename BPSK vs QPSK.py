import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erfc

# ============================================================
# CommLink - BPSK vs QPSK Comparative Study
# Batch 5 MFCS Project
# ============================================================

np.random.seed(0)

NUM_BITS = 200000
EbN0_dB = np.arange(0,13,1)

ber_bpsk = []
ber_qpsk = []

# ============================================================
# LAYER 1 : SIGNAL REPRESENTATION (CO1)
# ============================================================

def generate_bits(n):
    return np.random.randint(0,2,n)

def bpsk_mod(bits):
    return 2*bits - 1

def qpsk_mod(bits):

    if len(bits)%2 != 0:
        bits = np.append(bits,0)

    bits_i = bits[0::2]
    bits_q = bits[1::2]

    I = 2*bits_i - 1
    Q = 2*bits_q - 1

    symbols = (I + 1j*Q)/np.sqrt(2)

    return symbols

# ============================================================
# LAYER 2 : FOURIER TRANSFORM & PSD ANALYSIS (CO2)
# ============================================================

def compute_psd(signal):

    N = len(signal)

    spectrum = np.fft.fftshift(np.fft.fft(signal))

    psd = np.abs(spectrum)**2 / N

    freq = np.fft.fftshift(np.fft.fftfreq(N))

    return freq, psd

# ============================================================
# LAYER 3 : AWGN CHANNEL MODEL (CO3)
# ============================================================

def awgn_real(signal,EbN0_dB):

    EbN0 = 10**(EbN0_dB/10)

    Eb = 1

    N0 = Eb/EbN0

    sigma = np.sqrt(N0/2)

    noise = sigma*np.random.randn(len(signal))

    return signal + noise

def awgn_complex(signal,EbN0_dB):

    EbN0 = 10**(EbN0_dB/10)

    Es = 1

    Eb = Es/2

    N0 = Eb/EbN0

    sigma = np.sqrt(N0/2)

    noise = sigma*(np.random.randn(len(signal))
                  +1j*np.random.randn(len(signal)))

    return signal + noise

# ============================================================
# LAYER 4 : RECEIVER & DEMODULATION (CO4)
# ============================================================

def bpsk_demod(received):

    return (received >= 0).astype(int)

def qpsk_demod(received):

    I_hat = (received.real >= 0).astype(int)
    Q_hat = (received.imag >= 0).astype(int)

    bits = np.zeros(2*len(I_hat),dtype=int)

    bits[0::2] = I_hat
    bits[1::2] = Q_hat

    return bits

# ============================================================
# LAYER 5 : BER ANALYSIS & MONTE CARLO (CO5)
# ============================================================

def BER(tx,rx):

    return np.mean(tx != rx)

print("CommLink - BPSK vs QPSK Comparative Study")
print("-"*60)

for snr in EbN0_dB:

    # ---------------- BPSK ----------------

    bits = generate_bits(NUM_BITS)

    tx_bpsk = bpsk_mod(bits)

    rx_bpsk = awgn_real(tx_bpsk,snr)

    detected_bpsk = bpsk_demod(rx_bpsk)

    ber1 = BER(bits,detected_bpsk)

    ber_bpsk.append(ber1)

    # ---------------- QPSK ----------------

    bits_q = generate_bits(NUM_BITS)

    tx_qpsk = qpsk_mod(bits_q)

    rx_qpsk = awgn_complex(tx_qpsk,snr)

    detected_qpsk = qpsk_demod(rx_qpsk)

    ber2 = BER(bits_q,detected_qpsk)

    ber_qpsk.append(ber2)

    print(f"Eb/N0={snr:2d} dB | "
          f"BPSK={ber1:.4e} | "
          f"QPSK={ber2:.4e}")

# Theoretical BER

EbN0_linear = 10**(EbN0_dB/10)

ber_theory = 0.5*erfc(np.sqrt(EbN0_linear))

# ============================================================
# LAYER 6 : SHANNON CAPACITY & GAP ANALYSIS (CO6)
# ============================================================

capacity = np.log2(1 + EbN0_linear)

bpsk_efficiency = 0.5
qpsk_efficiency = 1.0

bpsk_gap = 9.6 - 0.41
qpsk_gap = 9.6 - 0.0

print("\nSpectral Efficiency")
print("-------------------")
print("BPSK =",bpsk_efficiency,"bits/s/Hz")
print("QPSK =",qpsk_efficiency,"bits/s/Hz")

print("\nShannon Gap")
print("-------------------")
print("BPSK Gap =",round(bpsk_gap,2),"dB")
print("QPSK Gap =",round(qpsk_gap,2),"dB")

# ============================================================
# RESULTS & PLOTS
# ============================================================

plt.figure(figsize=(8,6))

plt.semilogy(EbN0_dB,
             ber_bpsk,
             'o-',
             label='BPSK Simulated')

plt.semilogy(EbN0_dB,
             ber_qpsk,
             's-',
             label='QPSK Simulated')

plt.semilogy(EbN0_dB,
             ber_theory,
             'k--',
             label='Theory')

plt.xlabel('Eb/N0 (dB)')
plt.ylabel('BER')
plt.title('BER Comparison')
plt.grid(True,which='both')
plt.legend()
plt.show()

# PSD Comparison

sample_bits = generate_bits(1000)

bpsk_signal = bpsk_mod(sample_bits)

qpsk_signal = qpsk_mod(sample_bits)

freq1,psd1 = compute_psd(bpsk_signal)
freq2,psd2 = compute_psd(qpsk_signal)

plt.figure(figsize=(8,6))

plt.plot(freq1,psd1,label='BPSK PSD')
plt.plot(freq2,psd2,label='QPSK PSD')

plt.xlabel('Frequency')
plt.ylabel('PSD')
plt.title('Spectral Comparison')
plt.grid()
plt.legend()
plt.show()

# Shannon Capacity Plot

plt.figure(figsize=(8,6))

plt.plot(EbN0_dB,
         capacity,
         'o-')

plt.xlabel('Eb/N0 (dB)')
plt.ylabel('Capacity (bits/s/Hz)')
plt.title('Shannon Capacity')
plt.grid(True)

plt.show()