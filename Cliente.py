# -*- coding: utf-8 -*-
#import java.util.Enumeration;
#import java.util.Vector;
from Filme import c_Filme
from Alocacao import c_Alocacao
import itertools

CRIANCAS = 2
REGULAR = 0
NOVA_RELEASE = 1

class c_Cliente():
    _nome = None
    _alocacoes = []

    def __init__(self, p_nome):
        self._nome = p_nome
        self._alocacoes = []
    
    #arg do tipo Alocacao
    def f_adicionarAlocacao(self, p_arg):
        self._alocacoes.append(p_arg)
    
    def f_obterNomeCliente(self):
        return self._nome
    
    def f_calculaValor(self, p_alocacao):
        return p_alocacao.getCharge()

    def f_Expresao(self):
        v_totalAPagar = 0.0
        v_pontosFrequenciaAlocacao = 0
        v_alocacoes = iter(self._alocacoes)
        v_resultado = 'Registro de Locação para : '+ self.f_obterNomeCliente()+'\n'

        #while(alocacoes):
        for cada_alocacao in v_alocacoes:
            v_valorIndividual = self.f_calculaValor(cada_alocacao)
            
            #adicionar pontos de locador frequente
            v_pontosFrequenciaAlocacao += 1
            #adicionar bonus para uma locação de dois dias para lançamentos
            if cada_alocacao.f_obterFilme().f_obterPrecoCodigo() == c_Filme.NOVA_RELEASE and cada_alocacao.f_obterDiasAlocados()>1:
                v_pontosFrequenciaAlocacao += 1
            #mostrar informacoes para esta locacao
            v_resultado += " " + cada_alocacao.f_obterFilme().f_obterTitulo()+ " " + str(v_valorIndividual) + "\n"

            v_totalAPagar += v_valorIndividual

        #adicionar rodape do relatorio
        v_resultado += "Quantia devida é "+ str(v_totalAPagar)+"\n"
        v_resultado += "Voce ganhou " + str(v_pontosFrequenciaAlocacao)+ " pontos de locacao."

        return v_resultado

if __name__ == '__main__':
    o_meuCliente = c_Cliente('Ruben')
    print o_meuCliente.f_obterNomeCliente()
    v_fil01 = c_Filme('Titanic',2)
    v_alo01 = c_Alocacao(v_fil01,5) #filme, dias locados
    v_alo02 = c_Alocacao(v_fil01,2) #filme, dias locados
    v_alo03 = c_Alocacao(v_fil01,1) #filme, dias locados

    o_meuCliente.f_adicionarAlocacao(v_alo01)
    o_meuCliente.f_adicionarAlocacao(v_alo02)
    o_meuCliente.f_adicionarAlocacao(v_alo03)

    print o_meuCliente.f_Expresao()
