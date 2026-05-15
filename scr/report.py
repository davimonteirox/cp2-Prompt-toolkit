import matplotlib.pyplot as plt
import os
def gerar_graficos(df):
   if not os.path.exists('output/graficos'): os.makedirs('output/graficos')
   df.groupby('Tecnica')['Acuracia'].mean().plot(kind='bar')
   plt.savefig('output/graficos/acuracia.png')
   plt.close()
