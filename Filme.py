# -*- coding: utf-8 -*-

class c_Filme:
    CRIANCAS = 2
    REGULAR = 0
    NOVA_RELEASE = 1
    _titulo = None
    _precoCod = None

    def __init__(self,p_titulo,p_precoCodigo):
        self._titulo = p_titulo
        self._precoCodigo = p_precoCodigo
    
    def f_obterPrecoCodigo(self):
        return self._precoCodigo
    
    def f_setarPrecoCodigo(self, p_arg):
        self._precoCodigo = p_arg
    
    def f_obterTitulo(self):
        return self._titulo

    def f_getCharge(self,diasAlocados):
        v_valorFilme = 0
        
        if self.f_obterPrecoCodigo() == c_Filme.REGULAR:
            v_valorFilme += 2

            if diasAlocados > 2:
                v_valorFilme += (diasAlocados - 2) * 1.5
                    
        elif self.f_obterPrecoCodigo() == c_Filme.NOVA_RELEASE:
            v_valorFilme += 3

        elif self.f_obterPrecoCodigo() == c_Filme.CRIANCAS:
            v_valorFilme += 1.5

            if diasAlocados > 3:
                v_valorFilme += (diasAlocados - 3) * 1.5
        
        return v_valorFilme
    
    
    def f_obterPontosFrequenciaPorCadaAlocacao(self, diasAlocados):
        v_pontos = 1
        
        if self.f_obterPrecoCodigo == c_Filme.NOVA_RELEASE and diasAlocados > 1:
            v_pontos += 1
        
        else:
            v_pontos
        
        return v_pontos

if __name__ == '__main__':
    o_meuFilme = c_Filme('titanic',3)