#Calculadora em Python
#-*- coding: utf-8 -*-
#Funções
def soma(n1,n2):
    resultado = n1 + n2
    return resultado
def subtracao(n1,n2):
    resultado = n1 - n2
    return resultado
def multiplicacao(n1,n2):
    resultado = n1 * n2
    return resultado
def divisao(n1,n2):
    resultado = n1 / n2
    return resultado

#Variáveis para controle        
calcular = 1
novo = 0

#Motor do código
while(calcular==1):
    print("Seja bem-vindo!")
    n1 = float(input("Entre com o primeiro valor: "))
    n2 = float(input("Entre com o segundo valor: "))
    print("Selecione uma das operacoes")
    operador = int(input("[1]Adicionar | [2]Subtrair | [3]Multiplicar | [4]Dividir => "))
    if(operador == 1):
        print(soma(n1,n2))
        novo = int(input("Deseja efetuar outro calculo? [1]SIM | [2] NAO => "))
        if(novo==1):
            calcular=1
        else:
            calcular=0
    if(operador == 2):
        print(subtracao(n1,n2))
        novo = int(input("Deseja efetuar outro calculo? [1]SIM | [2] NAO => "))
        if(novo==1):
            calcular=1
        else:
            calcular=0
    if(operador == 3):
        print(multiplicacao(n1,n2))
        novo = int(input("Deseja efetuar outro calculo? [1]SIM | [2] NAO => "))
        if(novo==1):
            calcular=1
        else:
            calcular=0
    if(operador == 4):
        print(divisao(n1,n2))
        novo = int(input("Deseja efetuar outro calculo? [1]SIM | [2] NAO => "))
        if(novo==1):
            calcular=1
        else:
            calcular=0
