# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 21:54:35 2021
@author: Camilla Rosa Freire Sousa
Desenvolvido para processo seletivo de Summer 2022.01 na NAVI
"""
import math, numpy as np

def main():
    try:
        modo = int(input("Digite o número de qual algoritmo deseja rodar (1 - Peneira de Números; 2 - Algoritmo de vetor; 3 - Algoritmo de notas): "))
        if modo == 1:
            total = 0
            for i in range(1, 5000001):
                if (i % (2*37*49) == 0): #primos entre si
                    total = total + 1
            print("Existem",total, "números pares múltiplos de 37 e 49 simultaneamente entre 1 e 5.000.000")
        
        elif modo == 2:
            v = []
            for i in range(10):
                if i==0 or i%2==0:
                    v.append((3**i)+(7*math.factorial(i)))
                else:
                    v.append((2**i)+(4*np.log(i)))
            print("O vetor resultante nas condições dadas é:",v)
            
        elif modo == 3:
            dicionario = []
            maiornota = 0
            indicemaior = 0
            for i in range (1,6):
                linha = []
                linha.append(input("Digite o nome d@ alun@ %d:" %i))
                linha.append(float(input("Digite a nota d@ alun@ %d:" %i)))
                if linha[1] >= maiornota:
                    indicemaior = i-1
                    maiornota = linha[1]
                dicionario.append(linha)
            print("O aluno com a maior nota e sua respectiva nota são",dicionario[indicemaior])
    except:
        print("Um erro ocorreu. Verifique se você digitou os valores corretamente. O programa só aceita os valores numéricos 1, 2 e 3 para operar entre seus modos. O modo 3 só aceita valores numéricos com ponto no campo de nota.")
if __name__ == "__main__":
    main()
