
  
"""
heures en minutes:
ce programme convertit les heures en minutes
author@: IdirA
"""


def main():
    """
     Convertir_heures_en_minutes 
    
     """

try:
    print("Bienvenue au programe de conversion des heures en minutes") #Affiche un message de Bienvenue 
    heure=float(input("veuiller introduire le nombre d'heures a convertir:")) 
    # cette operation permet a l'utulisateur d'entrer le nombre d'heure voulu
    minutes=heure*60  # cette operation nous permet de convertir les heures en minutes
    print("{} heure(s) est egale a : {} minutes".format(heure, minutes)) #Affiche le resultat
except ValueError:
    print('Erreur !! Veuillez introduire un nombre.') # Si l'utulisateur ne rentre pas un chiffres ,un message d'erreur lui apparaitra
