# -*- coding: utf-8 -*-
from Filme import c_Filme

class c_Alocacao:
    def __init__(self,p_filme, p_diasAlocado): #filme de tipo Filme
        self._filme = p_filme #Tipo filme
        self._diasAlocados = p_diasAlocado
    
    def f_obterDiasAlocados(self):
        return self._diasAlocados
    
    def f_obterFilme(self):
        return self._filme

if __name__ == '__main__':
    o_minhaAlocacao = c_Alocacao()