'''
@author1: Jorge Coveiro, n10873
@author2: Carlos Rosario, n12794
@date 31-10-2012
@obs: PROGRAMA PARA A ANALISE DE DADOS DE UM .XLS
'''
import xls2csv
import processarcsv

''' 
CONVERSAO DE .XLS PARA .CSV
processarXLS1: conversao normal (linha de comandos)
processarXLS2: conversao alternativa (python-excel)
'''
xls2csv.processarXLS1()
#xls2csv.processarXLS2()

'''
PROCESSAMENTO DA BASE 
DE DADOS A PARTIR DO .CSV
'''
processarcsv.create_database()
processarcsv.write_database()
