Soundfile = (r"C:\Users\mateu\OneDrive\Documents\Projetos_em_Python\Projeto-da-disciplina-DCO3008\nota_re_adsr.wav")
# Soundfile = (r"C:\Users\mateu\OneDrive\Documents\Projetos_em_Python\Projeto-da-disciplina-DCO3008\output.wav")
#Especifica do local e nome do arquivo de áudio

import numpy as np
import scipy.io.wavfile as wv 
import os
import matplotlib.pyplot as plt


dFa,vtSom = wv.read(Soundfile)                                   # Abre arquivo de áudio de um arquivo
# vtSom: amplitude das amostras de som
# dFa: frequência de amostrasgem do som (amostragem no tempo)

# Converte estéreo → mono (ou escolha um canal)
if vtSom.ndim > 1:
    vtSom = vtSom.mean(axis=1)  # média dos canais

dta = 1/dFa                                                      # Tempo entre amostras
dTFinal = (len(vtSom)-1)*dta                                     # Tempo da última amostra do sinal de áudio
vtTSom = np.arange(0,dTFinal+dta,dta)                            # Eixo temporal do arquivo de áudio
##plt.figure(1,[10,7])
## plt.plot(vtTSom,vtSom)                                           # Plota gráfico do áudio

font = {'family' : 'DejaVu Sans','weight' : 'bold','size': 12}   #Configura a fonte do título
plt.rc('font', **font)
"""plt.title('Sinal de Áudio')                                      # Configura título do gráfico
plt.ylabel('Amplitude')                                          # Configura eixo X do gráfico
plt.xlabel('Tempo (s)')                                          # Configura eixo Y do gráfico
plt.ylim([-32000,25000])
plt.show() """

# Reproduz arquivo de áudio
# os.system(f'vlc --play-and-exit {Soundfile}')           
# Mostra informações gerais sobre o arquivo
print('Amostragem:')
print(' Taxa de amostragem = ',dFa,' Hz')
print(' Tempo entre amostras = ',dta,' Segundos')
print(' ')
print('Quantização e Codificação:')
print(' ')
print('Informações gerais do arquivo de áudio:')
print(' Número de canais = ',vtSom.shape)  
print(' Número de amostras = ',len(vtSom),' amostras')
print(' Duração = ',len(vtSom)*dta,' segundos')

print("Shape do vtSom:", vtSom.shape)
print("Tipo de dado:", vtSom.dtype)
print("Primeiras 10 amostras:", vtSom[:20])

# Vamos mostrar apenas os primeiros 0.02 segundos (20 ms)
tempo_visualizar = 0.1  # segundos
n_amostras = int(tempo_visualizar * dFa)

plt.figure(figsize=(10, 6))
plt.plot(vtTSom[:n_amostras], vtSom[:n_amostras], color='blue')
plt.title('Trecho do sinal de áudio (100 ms)')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.show()

plt.figure(figsize=(10, 6))
plt.specgram(vtSom, Fs=dFa, cmap='viridis')
plt.title('Espectrograma do Áudio')
plt.xlabel('Tempo (s)')
plt.ylabel('Frequência (Hz)')
plt.colorbar(label='Intensidade [dB]')
plt.show()

