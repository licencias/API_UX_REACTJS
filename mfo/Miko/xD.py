# -*- coding: utf-8 -*-
# -*- coding: cp1252 -*-
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys
import unicodedata
import unidecode


directorio = '../Datos.csv'
directorio = '../Causas de analisis de TD.csv'
# directorio = '../Datos_Georreferenciados_Depurados.txt'
# directorio = '../Datos_Georreferenciados.xlsx'

dateparse = lambda x:pd.datetime.strptime(x, '%Y-%m')

leer_archivo_trafos = pd.read_csv(directorio, sep= ";",dtype= 'object',parse_dates= ['Periodo'], encoding='latin1', index_col= None ,low_memory= False)
# print leer_archivo_trafos['Periodo']
saidi = leer_archivo_trafos['SAIDI Trafo']
saidi = pd.DataFrame(saidi)
# saidi = np.array(saidi)







# leer_archivo_trafos = pd.DataFrame(leer_archivo_trafos)
# saidi = leer_archivo_trafos['SAIDI Trafo']
# saidi = saidi.values.tolist()
# print saidi










# leer_archivo_trafos = pd.read_csv(directorio, sep= "\t", engine= 'python')
# leer_archivo_trafos = pd.read_csv(directorio, sep= "\t", encoding= 'utf-8')
# leer_archivo_trafos = pd.DataFrame(leer_archivo_trafos)
# print leer_archivo_trafos.describe()

# # leer_archivo_trafos.to_csv('Datos_depurados.csv', encoding= 'utf-8', sep= ';', index= False, decimal= ',', index_label= False)
# 'SAIDI Trafo'
# saidi = leer_archivo_trafos[leer_archivo_trafos['SAIDI Trafo']]
# saidi = np.array(saidi)
# print saidi
# # print leer_archivo_trafos
#
# print leer_archivo_trafos
#
#
# saidi = leer_archivo_trafos['SAIDI Trafo']
# saidi = pd.DataFrame(saidi)
# saidi = np.array(saidi)
# saidi = pd.DataFrame(saidi)
# print saidi.describe()
# # saidi = saidi.values.tolist()
#
# month = leer_archivo_trafos['Mes']
# year = leer_archivo_trafos['Year']
# # tension = leer_archivo_trafos['TENSION']

# print saidi.describe()

# for i in saidi:
# #     print 'aaaa',',',i
# #     i = i.encode('latin-1')
# #     i = float(i)
#     print i,',',type(i)

# plt.title('Histograma_SAIDI')
# plt.hist(saidi, bins= 30, alpha= 1, edgecolor = 'black', linewidth= 1)
# plt.xticks(np.arange(0.2, 1, step= 2))
# plt.show()

# plt.scatter(year, saidi, marker= 'o')
# plt.show()

# plt.plot(saidi, saidi, 'o', color= 'black')

# def histograma():

#
#     plt.grid(True)
#     plt.show()
#     plt.clf()
# histograma()

