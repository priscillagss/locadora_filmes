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

    def getCharge(self):
        v_valorFilme = 0
        
        if self.f_obterFilme().f_obterPrecoCodigo() == c_Filme.REGULAR:
            v_valorFilme += 2
        if self.f_obterDiasAlocados()>2:
            v_valorFilme += (self.f_obterDiasAlocados()-2)*1.5
        elif self.f_obterFilme().f_obterPrecoCodigo() == c_Filme.NOVA_RELEASE:
            v_valorFilme += 3
        elif self.f_obterFilme().f_obterPrecoCodigo() == c_Filme.CRIANCAS:
            v_valorFilme += 1.5
            if self.f_obterDiasAlocados()>3:
                v_valorFilme += (self.f_obterDiasAlocados()-3)*1.5

        return v_valorFilme


if __name__ == '__main__':
    o_minhaAlocacao = c_Alocacao()