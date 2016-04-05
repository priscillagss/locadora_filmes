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

    def f_getCharge(self):
        return self._filme.f_getCharge(self._diasAlocados)

    def f_obterPontosFrequenciaPorCadaAlocacao(self):
        return self._filme.f_obterPontosFrequenciaPorCadaAlocacao(self._diasAlocados)


if __name__ == '__main__':
    o_minhaAlocacao = c_Alocacao()