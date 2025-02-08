# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 03:20:13 2025

@author: asgun
"""


import random
import matplotlib.pyplot as plt

from math import sqrt

def gera_base_tsp(n):
    base_tsp=[]
    random.seed()
    
    for i in range(n):
        base_tsp.append([i, random.randint(10, 100), random.randint(10, 100)])
        
    return(base_tsp)

def dist_euclid(p0, p1):
    #Atencao. Devido ao formato idx lat long, pega coluna 1 e 2
    return( sqrt((p0[1]-p1[1])**2 +(p0[2]-p1[2])**2))



def plotaPontos(base,titulo):
    coordX = []
    coordY = []

    for n in range(len(base)):
        coordX.append(base[n][1])
        coordY.append(base[n][2])
    
    plt.scatter(coordX, coordY)
    plt.title(titulo)
    plt.show()


def plotaRota(base,rota, titulo):
    #Plota base
    coordX = []
    coordY = []
    for n in range(len(base)):
        coordX.append(base[n][1])
        coordY.append(base[n][2])
    
    plt.scatter(coordX, coordY)

    #Todos os pontos exceto o último
    for n in range(len(rota)-1):
        idxn = rota[n]
        idxn2 =rota[n+1]
        plt.plot([base[idxn][1], base[idxn2][1]], [base[idxn][2], base[idxn2][2]], color = 'black', linestyle=':')


    #Fecha o último
    idxn = rota[len(rota)-1]
    idxn2 =rota[0]
    plt.plot([base[idxn][1], base[idxn2][1]], [base[idxn][2], base[idxn2][2]], color = 'black', linestyle=':')

    plt.title(titulo)
    plt.show()
        


def prim(base):
    #Algoritmo de Prim para encontrar Minimum Spanning Tree
    n = len(base)
    
    #Ponto inicial
    vertices ={0}
    ramos =[]
    
    for i in range(n-1):
        distMin = 10000000
        idxOrigem = -1
        idxDestino = -1
        
        #Verifica qual o ponto mais próximo da árvore até o momento
        for origem in vertices:
            for k in range(n):
                if k not in vertices:
                    dist= dist_euclid(base[origem], base[k])
                    if dist < distMin:
                        distMin = dist
                        idxOrigem = origem
                        idxDestino = k
        #Insere no set de vértices e no de ramos
        vertices.add(idxDestino)
        ramos.append([idxOrigem,idxDestino])
        
    #Plota resultado
    for i in range(n):
        plt.scatter(base[i][1],base[i][2], color = 'black')
    
    for r in ramos:
        
 
        plt.plot([base[r[0]][1],base[r[1]][1]], [base[r[0]][2],base[r[1]][2]], color = 'black', linestyle=':')

    plt.title("Minimum Spanning Tree - Prim")
    plt.show()
        
    return(vertices, ramos)
        



base1 = gera_base_tsp(25)

#Plota só pontos
plotaPontos(base1, "Pontos aleatórios")


#Algoritmo de Prim
vert, ramos2 = prim(base1)
