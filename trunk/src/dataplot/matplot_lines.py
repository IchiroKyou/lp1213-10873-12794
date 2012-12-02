# -*- coding: utf-8 -*-
'''
@author: 10873 Jorge Coveiro
@author: 12794 Carlos Rosário
@last updated: 15-11-2012
@obs: set up matplotlib and the figure
'''
import sys
sys.path.append("../core")
import matplotlib.pyplot as plt
plt.figure

class MatPlotLines:
	'''
	Desenha um gráfico de linhas
	'''
	def __init__(self, dados):
		self.dados = dados

	def draw(self, target):
		#create data
		'''
		Funcception
		'''
		if target == 'total':
			y_series_1 = self.csv_a.total
		elif target == 'total_h':
			y_series_1 = self.csv_a.total_h
		elif target == 'total_m':
			y_series_1 = self.csv_a.total_m
		elif target == 'total_hm':
			y_series_1 = self.csv_a.total_hm

		
		max_n_target = 0
		for val in y_series_1:
			if val > max_n_target:
				max_n_target += val
	
		x_series = range(len(y_series_1))  #???

		#plot data
		plt.plot(x_series, y_series_1, label="Curva dos " + target + " Inscritos por ano lectivo")
		#add in labels and title
		plt.xlabel("Ano Lectivo")
		plt.ylabel("Numero de " + target + " Inscritos")
		plt.title("Analise de Inscritos no Ensino Superior")
		#add limits to the x and y axis
		plt.xlim(0,15)                     #???
		plt.ylim(0,max_n_target)

		#create legend
		plt.legend(loc="upper right")

		#save figure to png
		plt.show()
