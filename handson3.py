import numpy as np
import scipy.io.wavfile as wv
import os
import matplotlib.pyplot as plt

soundFile = (r'C:\Users\mateu\OneDrive\Documents\Projetos_em_Python\Projeto-da-disciplina-DCO3008\output.wav')
dFa, vtSom = wv.read(soundFile)

# Garante formato 2D
if vtSom.ndim == 1:
    vtSom = vtSom.reshape(-1, 1)

# Tempo máximo de reprodução
tf = 10
amostrasTf = int(np.ceil(tf * dFa))
vtSom = vtSom[:amostrasTf, :]

dta = 1 / dFa
dTFinal = (len(vtSom) - 1) * dta
vtTSom = np.linspace(0, dTFinal, len(vtSom))

plt.figure(1, [10, 7])
plt.subplot(3, 1, 1)
plt.plot(vtTSom, vtSom)
plt.title('Sinal de Áudio')
plt.ylabel('Amplitude')
plt.xlabel('Tempo (s)')

# Salva e reproduz original
wv.write(soundFile, dFa, vtSom.astype('int16'))
# os.system(r'"C:\Program Files\VideoLAN\VLC\vlc.exe" --play-and-exit "./MATERIAL/HD_02_PYTHON/sem_eco.wav"')

# --- Cria eco ---
n = 2000
eco = np.zeros_like(vtSom, dtype=float)
eco[n:, :] = vtSom[:-n, :]

vtSomEco = vtSom.astype(float) + eco
vtSomEco /= np.max(np.abs(vtSomEco))  # normaliza

wv.write(soundFile, dFa, (vtSomEco * 32767).astype('int16'))
# os.system(r'"C:\Program Files\VideoLAN\VLC\vlc.exe" --play-and-exit "./MATERIAL/HD_02_PYTHON/com_eco.wav"')

plt.subplot(3, 1, 2)
plt.plot(vtTSom, vtSomEco)
plt.title('Sinal de Áudio + Réplica')
plt.ylabel('Amplitude')
plt.xlabel('Tempo (s)')

plt.subplot(3, 1, 3)
plt.plot(vtTSom, vtSomEco - vtSom)
plt.title('Diferença entre sinais (Eco)')
plt.ylabel('Amplitude')
plt.xlabel('Tempo (s)')

plt.tight_layout()
plt.show()
