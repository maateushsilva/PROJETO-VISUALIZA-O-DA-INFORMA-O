import numpy as np
import matplotlib.pyplot as plt

#Carrega os dados ignorando o cabeçalho,,
dados = np.genfromtxt(r"C:\Users\55199\Downloads\USD_BRL_hist.csv", delimiter=',', dtype=str, skip_header=1)
datas = dados[:, 0]
valores = dados[:, 1].astype(float)

#Gráfico de Barras (últimos 10 dias),
ultimos = dados[-10:]
datas_ult = ultimos[:, 0]
valores_ult = ultimos[:, 1].astype(float)

plt.figure(figsize=(8, 5))
plt.bar(datas_ult, valores_ult, color='orange')
plt.title('USD/BRL - Últimos 10 dias')
plt.xlabel('Data')
plt.ylabel('Cotação')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Gráfico Temporal com destaque (zoom nos últimos 30 dias),
ultimos_30 = dados[-30:]
datas_30 = ultimos_30[:, 0]
valores_30 = ultimos_30[:, 1].astype(float)

plt.figure(figsize=(10, 5))
plt.plot(datas_30, valores_30, color='green', marker='x')
plt.title('USD/BRL - Últimos 30 Dias')
plt.xlabel('Data')
plt.ylabel('Cotação')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
plt.barh(datas_ult, valores_ult, color='seagreen')
plt.title('USD/BRL - Últimos 10 Dias (Colunas Horizontais)')
plt.xlabel('Cotação')
plt.ylabel('Data')
plt.tight_layout()
plt.show()