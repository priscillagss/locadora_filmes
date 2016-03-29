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

if __name__ == '__main__':
    o_meuFilme = c_Filme('titanic',3)