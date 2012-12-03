import sys
sys.path.append("../core")
import numpy as np
import matplotlib.pyplot as plt
from curso import Curso

def desenhaGraphBars(cursos, numero):
	'''
	Funcao que desenha um grafico de barras
	'''
	N = 16
	menMeans = cursos[numero].totalH
	menStd =   (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

	ind = np.arange(N)  # the x locations for the groups
	width = 0.25       # the width of the bars

	fig = plt.figure(figsize=(12.5,6), dpi=100, facecolor='yellow', edgecolor='black')
	ax = fig.add_subplot(111)
	rects1 = ax.bar(ind, menMeans, width, color='blue', yerr=menStd)

	womenMeans = cursos[numero].totalM
	womenStd = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

	rects2 = ax.bar(ind+width, womenMeans, width, color='red', yerr=womenStd)

	hm_Means = cursos[numero].totalHM
	hm_Std = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

	rects3 = ax.bar(ind+width*2, hm_Means, width, color='green', yerr=hm_Std)

	# add some
	ax.set_ylabel('Numero de Inscritos no Ensino Superior')
	ax.set_title('(por Ano Lectivo)')
	ax.set_xticks(ind+width)
	ax.set_xticklabels( ('9596', '9697', '9798', '9899', '9900',
                     '0001', '0102', '0203', '0304', '0405',
		   '0506', '0607', '0708', '0809', '0910', '1011') )

	ax.legend( (rects1[0], rects2[0], rects3[0] ), ('Homens', 'Mulheres', 'Homens e Mulheres') )

	def autolabel(rects):
		# attach some text labels
		for rect in rects:
			height = rect.get_height()
			ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height), ha='center', va='bottom')

	autolabel(rects1)
	autolabel(rects2)
	autolabel(rects3)

	plt.show()
