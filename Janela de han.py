import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat
from scipy.signal import hann
caminho = (r'C:/Users/mateu/OneDrive/Documents/Projetos_em_Python/Projeto-da-disciplina-DCO3008/20230023030 (1).mat')

# === Carrega o arquivo ===
data = loadmat(caminho)
x = np.squeeze(data['x'])
fs = float(data['fs'])

# === Janela temporal ===
N = len(x)
t = np.arange(N) / fs

# === FFT sem janela (leakage visível) ===
X_fft = np.fft.fft(x)
freq = np.fft.fftfreq(N, d=1/fs)
X_mag = np.abs(X_fft) / N

# === FFT com janela de Hann (reduz leakage) ===
window = hann(N)
x_win = x * window
X_fft_win = np.fft.fft(x_win)
X_mag_win = np.abs(X_fft_win) / (N/2)  # normalização compensando a janela

# === Só parte positiva do espectro ===
half = N // 2
freq_pos = freq[:half]
X_mag = X_mag[:half]
X_mag_win = X_mag_win[:half]

# === Plot ===
plt.figure(figsize=(10,6))
plt.subplot(2,1,1)
plt.plot(freq_pos, X_mag)
plt.title("Espectro sem janela (com leakage)")
plt.xlabel("Frequência (Hz)")
plt.ylabel("|X(f)|")
plt.grid(True)

plt.subplot(2,1,2)
plt.plot(freq_pos, X_mag_win)
plt.title("Espectro com janela de Hann (leakage reduzido)")
plt.xlabel("Frequência (Hz)")
plt.ylabel("|X(f)|")
plt.grid(True)

plt.tight_layout()
plt.show()
