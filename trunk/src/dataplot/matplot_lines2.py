#set up matplotlib and the figure
import matplotlib.pyplot as plt
plt.figure




#create data
x_series = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
y_series_1 = [43,42,32,43,41,22,32,51,22,23,43,12,43,38,33,32]

#plot data
plt.plot(x_series, y_series_1, label="Spline dos Alunos Inscritos")

#add in labels and title
plt.xlabel("por Ano")
plt.ylabel("Numero de Inscritos")
plt.title("Analise de Inscritos no Ensino Superior")

#add limits to the x and y axis
plt.xlim(1, 16)
plt.ylim(0, 55)

#create legend
plt.legend(loc="upper right")

#save figure to png
plt.show()


