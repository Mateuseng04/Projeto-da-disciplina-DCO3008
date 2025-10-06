import numpy as np
import scipy.io.wavfile as wv 
import os
import matplotlib.pyplot as plt

soundfile2 = r"C:\Users\mateu\OneDrive\Documents\Projetos_em_Python\Projeto-da-disciplina-DCO3008/output2.wav"               # Especifica do local e nome do arquivo de áudio
dFa, vtSom = wv.read(soundfile2)                                   # Abre arquivo de áudio de um arquivo
# vtSom: amplitude das amostras de som
# dFa: frequência de amostrasgem do som (amostragem no tempo)
vtSom = vtSom/ np.max(np.abs(vtSom))
vtSomint16 = np.int16(vtSom * 32767)                              #converte de float64 para int16 para reduzir ruído
wv.write(soundfile2,dFa,vtSomint16)
#salva amomstra de som para ser reproduzida

#reproduz a amostra de som salva
# os.system(r'"C:\Program Files\VideoLAN\VLC\vlc.exe" --play-and-exit "{}"'.format(soundfile2))


dta = 1/dFa                                                      # Tempo entre amostras
dTFinal = (len(vtSom)-1)*dta                                     # Tempo da última amostra do sinal de áudio
vtTSom = np.arange(0,dTFinal,dta)                            # Eixo temporal do arquivo de áudio
plt.figure(1,[10,7])
font = {'family' : 'DejaVu Sans','weight' : 'bold','size': 12}   #Configura a fonte do título
plt.rc('font', **font)
plt.plot(vtSom,vtSom)                                           # Plota gráfico do áudio
plt.title('Sinal de Áudio')                                      # Configura título do gráfico
plt.ylabel('Amplitude')                                          # Configura eixo X do gráfico
plt.xlabel('Tempo (s)')                                          # Configura eixo Y do gráfico
plt.ylim([-120000,100000])                                       # Configura eixo Y do gráfico

plt.show()