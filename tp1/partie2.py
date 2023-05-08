import math
# PARTIE 2: Fonctions simples de la calculatrice

def calculerMinutes(annees, mois, jours, heures, minutes, secondes):
    # TODO: Assignez à la variable minutes_années le nombre de minutes dans toutes les secondes
    minutes_secondes = None

    # TODO: Assignez à la variable minutes_années le nombre de minutes dans toutes les heures
    minutes_heures = None

    # TODO: Assignez à la variable minutes_années le nombre de minutes dans tous les jours
    minutes_jours = None

    # TODO: Assignez à la variable minutes_années le nombre de minutes dans tous les mois
    minutes_mois = None

    # TODO: Assignez à la variable minutes_années le nombre de minutes dans toutes les années
    minutes_annees = None

    # TODO: Assignez à la variable somme le total
    somme = None

    return somme


def arrondir(nombre, facteurArrondissement):
    # TODO: Déterminer si le nombre est plus petit que le facteur
    nombrePlusPetitQueFacteur = nombre < facteurArrondissement

    # SI OUI (nombre est plus petit que facteur)
    if nombrePlusPetitQueFacteur:

        # TODO: Déterminer si on doit arrondir vers le haut ou vers le bas
        # INDICE: On doit arrondir vers le haut si le nombre est plus que la moitié du facteur
        doitArrondirVersLeHaut = None

        # SI OUI On doit arrondir vers le haut
        if doitArrondirVersLeHaut:
            # Retourner le résultat arrondi vers le haut
            resultatArrondi = None
            return resultatArrondi

        else:
            # Retourner le résultat arrondi vers le bas
            resultatArrondi = None
            return resultatArrondi

    # SI NON (nombre est plus grand que facteur)
    else:
        # TODO: Calculer reste de la nombre / facteurArrondissement
        reste = None

        # TODO: Déterminer si le nombre doit être arrondi vers le haut ou vers le bas
        # HINT: On doit arrondir vers le haut si le reste est plus grand que la moitié du facteur
        doitArrondirVersLeHaut = None

        # SI on doit arrondir vers le haut:
        if doitArrondirVersLeHaut:
            # TODO: calculer le résultat arrondi vers le haut
            resultatArrondi = None
            return resultatArrondi

        # SINON (on doit arrondir vers le bas)
        else:
            # TODO: calculer le résultat arrondi vers le bas
            resultatArrondi = None
            return resultatArrondi


def calculerNombreA(mot):
    # TODO: Calculer le nombre de 'a' dans un mot
    total = 0

    # Pour chaque lettre du mot:
    for lettre in mot:
        #TODO: Déterminer si la lettre est un A
        estUnA = None

        # SI OUI
        if estUnA:
            #TODO: augmenter total
            pass # Pass sert à spécifier qu'un bloc if est vide. Enlevez-le quand vous le remplirez :)

    return total


# PAS TOUCHER
if __name__ == "__main__":
    print("Exécutez le fichier calculatrice.py ou le fichier tests.py!")