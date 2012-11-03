# -*- coding: utf-8 -*-
'''
@author1: Jorge Coveiro, n10873
@author2: Carlos Rosario, n12794
@date 31-10-2012
@obs: PROGRAMA PARA O PROCESSAMENTO DE UMA BASE DE DADOS EM SQLITE3
'''
import sqlite3
import csv


def create_database():
    '''
    CRIACAO DA BASE DE DADOS
    '''
    conn = sqlite3.connect('Inscritos.db')
    cursor = conn.cursor()
    instrucao = '''CREATE TABLE Inscritos(estEnsino text, unidOrgan text, nivelCur text, curSup text, areaForma text, 
                                          ano_um_h number, ano_um_m number, ano_um_hm number,
                                          ano_dois_h number, ano_dois_m number, ano_dois_hm number,
                                          ano_tres_h number, ano_tres_m number, ano_tres_hm number,
                                          ano_quatro_h number, ano_quatro_m number, ano_quatro_hm number,
                                          ano_cinco_h number, ano_cinco_m number, ano_cinco_hm number,
                                          ano_seis_h number, ano_seis_m number, ano_seis_hm number,
                                          ano_sete_h number, ano_sete_m number, ano_sete_hm number,
                                          ano_oito_h number, ano_oito_m number, ano_oito_hm number,
                                          ano_nove_h number, ano_nove_m number, ano_nove_hm number,
                                          ano_dez_h number, ano_dez_m number, ano_dez_hm number,
                                          ano_onze_h number, ano_onze_m number, ano_onze_hm number,
                                          ano_doze_h number, ano_doze_m number, ano_doze_hm number,
                                          ano_treze_h number, ano_treze_m number, ano_treze_hm number,
                                          ano_catorze_h number, ano_catorze_m number, ano_catorze_hm number,
                                          ano_quinze_h number, ano_quinze_m number, ano_quinze_hm number,
                                          ano_dezasseis_h number, ano_dezasseis_m number, ano_dezasseis_hm number)'''
    cursor.execute(instrucao)
    conn.commit()
    cursor.close()
    pass

def write_database():
    '''
    IMPORTA DADOS DE UM FICHEIRO .CSV
    PARA A BASE DE DADOS
    '''
    conn = sqlite3.connect('Inscritos.db') 
    cursor = conn.cursor()
    reader = csv.reader(open("Inscritos.csv", "r"))
    linha = 0
    for list_line in reader:
        linha += 1
        if linha == 5:
            continue       
        instrucao = '''INSERT INTO Inscritos (estEnsino, unidOrgan, nivelCur, curSup, areaForma,
                                          ano_um_h, ano_um_m, ano_um_hm,
                                          ano_dois_h, ano_dois_m, ano_dois_hm,
                                          ano_tres_h, ano_tres_m, ano_tres_hm,
                                          ano_quatro_h, ano_quatro_m, ano_quatro_hm,
                                          ano_cinco_h, ano_cinco_m, ano_cinco_hm,
                                          ano_seis_h, ano_seis_m, ano_seis_hm,
                                          ano_sete_h, ano_sete_m, ano_sete_hm,
                                          ano_oito_h, ano_oito_m, ano_oito_hm,
                                          ano_nove_h, ano_nove_m, ano_nove_hm,
                                          ano_dez_h, ano_dez_m, ano_dez_hm,
                                          ano_onze_h, ano_onze_m, ano_onze_hm,
                                          ano_doze_h, ano_doze_m, ano_doze_hm,
                                          ano_treze_h, ano_treze_m, ano_treze_hm,
                                          ano_catorze_h, ano_catorze_m, ano_catorze_hm,
                                          ano_quinze_h, ano_quinze_m, ano_quinze_hm,
                                          ano_dezasseis_h, ano_dezasseis_m, ano_dezasseis_hm)
                                          VALUES ("{0}", "{1}", "{2}", "{3}", "{4}",
                                          "{5}", "{6}", "{7}",
                                          "{8}", "{9}", "{10}",
                                          "{11}", "{12}", "{13}",
                                          "{14}", "{15}", "{16}",
                                          "{17}", "{18}", "{19}",
                                          "{20}", "{21}", "{22}",
                                          "{23}", "{24}", "{25}",
                                          "{26}", "{27}", "{28}",
                                          "{29}", "{30}", "{31}",
                                          "{32}", "{33}", "{34}",
                                          "{35}", "{36}", "{37}",
                                          "{38}", "{39}", "{40}",
                                          "{41}", "{42}", "{43}",
                                          "{44}", "{45}", "{46}",
                                          "{47}", "{48}", "{49}",
                                          "{50}", "{51}", "{52}")'''.format(list_line[0],list_line[1],list_line[2],list_line[3],list_line[4],
                                                                             list_line[5],list_line[6],list_line[7],
                                                                             list_line[8],list_line[9],list_line[10],
                                                                             list_line[11],list_line[12],list_line[13],
                                                                             list_line[14],list_line[15],list_line[16],
                                                                             list_line[17],list_line[18],list_line[19],
                                                                             list_line[20],list_line[21],list_line[22],
                                                                             list_line[23],list_line[24],list_line[25],
                                                                             list_line[26],list_line[27],list_line[28],
                                                                             list_line[29],list_line[30],list_line[31],
                                                                             list_line[32],list_line[33],list_line[34],
                                                                             list_line[35],list_line[36],list_line[37],
                                                                             list_line[38],list_line[39],list_line[40],
                                                                             list_line[41],list_line[42],list_line[43],
                                                                             list_line[44],list_line[45],list_line[46],
                                                                             list_line[47],list_line[48],list_line[49],
                                                                             list_line[50],list_line[51],list_line[52])
        
        
        cursor.execute(instrucao)
        if linha == 11956:
          break
        pass
    conn.commit()
    cursor.close()
    pass


# def read_database():
#     '''
#     EXEMPLO DE LEITURA DA BASE DE DADOS
#     '''
#     conn = sqlite3.connect('Inscritos.db')
#     cursor = conn.cursor()
#     instrucao = '''SELECT * FROM Inscritos WHERE estEnsino="{0}"'''.format(9989)
#     cursor.execute(instrucao)
#     for result in cursor:
#         print result
#     cursor.close()

