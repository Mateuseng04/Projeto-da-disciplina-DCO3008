import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wv
import os

# ------------------------------
# Parâmetros da onda
# ------------------------------
tf = 1                       # Tempo de duração da nota
fc = 512                     # Frequência da nota Dó
fs = 100 * fc                # Frequência de amostragem
t = np.arange(0, tf+1/fs, 1/fs)  # Vetor tempo
A = 1                        # Amplitude do sinal
y = A * np.cos(2 * np.pi * fc * t)  # Sinal senoidal

# ------------------------------
# Plot do sinal
# ------------------------------
plt.figure(1, figsize=[10, 7])
plt.plot(t, y)
plt.axis([0, 0.02, -2, 2])   # Zoom para melhor visualização
plt.title("Sinal gerado")
plt.show()

# ------------------------------
# Conversão para int16 (necessário para WAV)
# ------------------------------
y_int16 = np.int16(y / np.max(np.abs(y)) * 32767)

# ------------------------------
# Caminho do arquivo
# ------------------------------
saida = r"C:\Users\mateu\OneDrive\Documents\Projetos_em _Python\Projeto-da-disciplina-DCO3008\tom_gerado.wav"

# ------------------------------
# Salvando o .wav
# ------------------------------
wv.write(saida, fs, y_int16)
print(f"Arquivo .wav criado em: {saida}")

# ------------------------------
# Reproduzindo o arquivo (opcional)
# ------------------------------
# Teste VLC no Windows: normalmente o comando é "vlc" e não "cvlc"
os.system(f'vlc --play-and-exit "{saida}"')
