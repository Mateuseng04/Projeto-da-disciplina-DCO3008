import numpy as np
import scipy.io as sio
import scipy.signal as sig
import matplotlib.pyplot as plt

caminho = (r'C:/Users/mateu/OneDrive/Documents/Projetos_em_Python/Projeto-da-disciplina-DCO3008/20230023030.mat')
def estimar_senoides_mat(caminho_mat, limiar_relativo=0.1, plot=True):
    """
    Este código estima automaticamente as frequências e fases das senóides
    que compõem um sinal contido no arquivo .mat.

    Este arquivo contém as variáveis:
      - fs: taxa de amostragem
      - x: sinal de áudio ou amostrado

    Parâmetros:
    - caminho_mat: caminho do arquivo .mat
    - limiar_relativo: fração da magnitude máxima usada para detectar picos
    - plot: se True, exibe o espectro com os picos detectados

    Retorna:
    - Lista de duplas (frequência_Hz, fase_rad)
    """

    #Leitura do arquivo .mat
    dados = sio.loadmat(caminho_mat)
    fs = float(np.squeeze(dados["fs"]))
    x = np.squeeze(dados["x"])

    #FFT normalizada unilateral
    N = len(x)
    Xf = np.fft.fft(x)
    Xf = Xf / N
    Xf_uni = Xf[:N // 2]
    freqs = np.fft.fftfreq(N, d=1 / fs)[:N // 2]
    mag = np.abs(Xf_uni)

    #Detecção automática de picos
    picos, propriedades = sig.find_peaks(mag, height=np.max(mag) * limiar_relativo, distance=5)
    picos_ordenados = sorted(picos, key=lambda i: mag[i], reverse=True)

    #Estimativa de frequência e fase
    componentes = []
    for i in picos_ordenados:
        f0 = freqs[i]
        fase = np.angle(Xf_uni[i])
        componentes.append((f0, fase))

    #Exibição gráfica
    if plot:
        plt.figure(figsize=(10, 6))
        plt.plot(freqs, mag, label="Espectro |X(f)|")
        plt.plot(freqs[picos_ordenados], mag[picos_ordenados], "ro", label="Picos detectados")
        plt.title("Espectro do sinal e picos detectados")
        plt.xlabel("Frequência (Hz)")
        plt.ylabel("Magnitude")
        plt.grid(True)
        plt.legend()
        plt.show()

    #Exibição textual
    print("Componentes senoidais detectadas:")
    for k, (f, phi) in enumerate(componentes):
        print(f"  Senoide {k+1}: f = {f:.1f} Hz, fase = {phi:.3f} rad")

    return componentes


# Exemplo de uso:

resultado = estimar_senoides_mat(caminho)
