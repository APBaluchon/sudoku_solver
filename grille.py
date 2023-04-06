import itertools
import sys

class Grille:
    """
    Classe simulant le fonctionnement d'une grille de sudoku, les cases vides sont représentées par des 0.

    Parameters
    ----------
    valeurs : list of list of str
        Les valeurs de la grille, chaque liste représente une ligne
    """

    def __init__(self, valeurs):
        self.valeurs = valeurs
        self.liste_possibilites = self.get_possibilities()

    def at(self, i, j):
        """
        Retourne la valeur à la ligne i et à la colonne j (convention python)

        Parameters
        ----------
        i : int
            La ligne
        j : int
            La colonne
        
        Return
        ------
        int
            La valeur à la ligne i et à la colonne j
        """
        return self.valeurs[i][j]
    
    def number_of_possibilites(self, i, j):
        """
        Indique le nombre de valeurs possibles pour une case donnée

        Parameters
        ----------
        i : int
            La ligne
        j : int
            La colonne

        Return
        ------
        int
            Le nombre de valeurs possible dans la case donnée
        """
        res = 0
        if self.valeurs[i][j] == 0:
            for n in range(1, 10):
                if self.is_value_possible(n, i, j):
                    res += 1
        return res

    def is_value_possible(self, n, i, j):
        """
        Indique si la valeur n peut-être mise dans la case située en ligne i et colonne j

        Parameters
        ----------
        n : int
            Valeur à tester
        i : int
            La ligne
        j : int
            La colonne

        Return
        ------
        bool
            True si la valeur peut-être mise dans la case, False sinon
        """
        if self.is_value_in_row(n, i) or self.is_value_in_column(n, j) or self.is_value_in_square(n, i, j):
            return False
        else:
            return True

    def is_value_in_row(self, n, i):
        """
        Indique si la valeur n se trouve dans la ligne i

        Parameters
        ----------
        n : int
            La valeur à tester
        i : int
            La ligne

        Return
        ------
        bool
            True si la valeur n est dans la ligne, False sinon
        """
        return n in self.valeurs[i]
    
    def is_value_in_column(self, n, j):

        """
        Indique si la valeur n se trouve dans la colonne j

        Paramters
        ---------
        n : int
            La valeur à tester
        j : int
            La colonne

        Return
        ------
        bool
            True si la valeur n est dans la colonne, False sinon
        """
        return n in [self.valeurs[i][j] for i in range(9)]
    
    def is_value_in_square(self, n, i, j):
        """
        Indique si la valeur n est dans le carré (3x3) où se trouve la case de coordonnées i, j

        Parameters
        ----------
        n : int
            La valeur à tester
        i : int
            La ligne
        j : int
            La colonne

        Return
        ------
        bool
            True si la valeur n est dans le carré, False sinon
        """
        a = i//3
        b = j//3
        for ligne in range(3):
            for colonne in range(3):
                if (3*a+ligne, 3*b+colonne) != (i, j):
                    if self.valeurs[3*a+ligne][3*b+colonne] == n:
                        return True
        return False

    def get_possibilities(self):
        """
        Retourne le nombre de valeurs possibles pour chaque case de la grille

        Return
        ------
        list
            Retourne une liste de tuple, le premier élément correpond à la case, le second au nombre de possibilités
        """   
        d = {(i, j):self.number_of_possibilites(i, j) for i,j in itertools.product(range(9), range(9)) if self.number_of_possibilites(i, j) != 0}
        return sorted(d.items(), key=lambda x : x[1])

    def is_completed(self):
        """
        Indique si une grille est complétée

        Return
        ------
        bool
            True si la grille est complétée, False sinon
        """
        return len(self.get_possibilities())==0
    
    def solve_backtracking(self):
        """
        Fonction pour résoudre la grille
        """
        
        index = 0

        while(self.is_completed() == False):
            i = self.liste_possibilites[index][0][0]
            j = self.liste_possibilites[index][0][1]
            actual_value = self.valeurs[i][j]
            self.valeurs[i][j] = 0

            for n in range(actual_value+1,10):
                if(self.is_value_possible(n, i, j)):
                    self.valeurs[i][j] = n
                    index += 1
                    break
                if n == 9:
                    index -= 1


    def __str__(self):
        res = ""

        for i in range(9):
            for j in range(9):
                res += str(self.valeurs[i][j])+" "
            res += "\n"

        return res