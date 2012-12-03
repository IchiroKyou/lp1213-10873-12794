# -*- coding: utf-8 -*-
'''
@author: 10873 Jorge Coveiro
@author: 12794 Carlos Rosário 
@last updated: 3-12-2012
'''

class Curso:
	'''
	Classe que contem o número de alunos inscritos 
	por ano	lectivo no curso 'nome', por sexo e o 
	número total de alunos em todos os anos lectivos
	'''
	def __init__(self, nome = "", totalH = [], totalM = [], totalHM = [], totalAnos = 0):
		self.nome = nome
		self.totalH = totalH
		self.totalM = totalM
		self.totalHM = totalHM
