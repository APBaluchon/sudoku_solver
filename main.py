from grille import Grille

import itertools


valeurs = [
    #0,1,2,3,4,5,6,7,8
    [9,0,0,1,0,0,0,0,5],#0
    [0,0,5,0,9,0,2,0,1],#1
    [8,0,0,0,4,0,0,0,7],#2
    [0,0,0,0,8,0,0,0,0],#3
    [0,0,0,7,0,0,0,0,0],#4
    [0,0,0,0,2,6,0,0,9],#5
    [2,0,0,3,0,0,0,0,6],#6
    [0,0,0,2,0,0,9,0,0],#7
    [0,0,1,9,0,4,5,7,0] #8
]


g1 = Grille(valeurs)

print(g1.get_possibilites())

