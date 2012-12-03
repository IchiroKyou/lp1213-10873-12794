# -*- coding: utf-8 -*-

class NivelFormacao:
	'''
	Classe que contem o número de alunos inscritos 
	por ano	lectivo no nivel de formação 'nome', por 
	sexo e o número total de alunos em todos os anos lectivos
	'''
	def __init__(self, nome = "", totalH = [], totalM = [], totalHM = [], totalAnos = 0):
		self.nome = nome
		self.totalH = totalH
		self.totalM = totalM
		self.totalHM = totalHM
		self.totalAnos = totalAnos
