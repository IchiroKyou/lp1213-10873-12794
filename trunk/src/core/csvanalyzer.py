# -*- coding: utf-8 -*-
import csv

NUMERO_ANOS = 16

class CsvAnalyzer:
	'''
	Lê ficheiro csv e guarda a soma do número de todos os totais,
	os totais de homens, mulheres e, homens e mulheres nos atributos
	total,total_h,total_m e total_hm respectivamente, num objecto desta
	classe
	'''
	def __init__(self,csv_f):
		self.csv_f=csv_f
		self.total = [0 for s in range(48)]
		self.total_h = range(NUMERO_ANOS)
		self.total_m = range(16)
		self.total_hm = range(16)
		self.readCsv()

	def readCsv(self):
		'''
		Percorre o ficheiro
		'''
		csv_file=open(self.csv_f, "r")

		csv_r=csv.reader(csv_file)

		for row in csv_r:
			for i in range(len(self.total)):
				self.total[i]+= int(row[4+i]) #alterar para 3+i

		for i in range(len(self.total_h)):
			self.total_h[i]=self.total[3*i]
			self.total_m[i]=self.total[1+3*i]
			self.total_hm[i]=self.total[2+3*i]

		csv_file.close()
