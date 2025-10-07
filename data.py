from scipy.io import loadmat

caminho = (r'C:/Users/mateu/OneDrive/Documents/Projetos_em_Python/Projeto-da-disciplina-DCO3008/20230023030 (1).mat')
data = loadmat(caminho)
print(data.keys())