
# Créer la classe "Pokemon"

class Pokemon:
    def __init__(self, nom, points_de_vie=100, niveau=1, puissance_attaque=0, defense=0):
        self.__nom = nom
        self.__points_de_vie = points_de_vie
        self.niveau = niveau
        self.puissance_attaque = puissance_attaque
        self.defense = defense

    def __str__(self):
        return f"{self.__nom} (niveau {self.niveau}) - PV: {self.__points_de_vie}, DEF: {self.defense}, ATK: {self.puissance_attaque}"

    def afficher_informations_generales(self):
        print(self)

     #class Pokemon:
     
class Normal(Pokemon):
    def __init__(self, nom, niveau):
        super().__init__(nom, niveau)
        self.points_vie = 120
        self.puissance_attaque = 30
        self.defense = 20

class Feu(Pokemon):
    def __init__(self, nom, niveau):
        super().__init__(nom, niveau)
        self.points_vie = 80
        self.puissance_attaque = 50
        self.defense = 10

class Eau(Pokemon):
    def __init__(self, nom, niveau):
        super().__init__(nom, niveau)
        self.points_vie = 100
        self.puissance_attaque = 40
        self.defense = 30

class Terre(Pokemon):
    def __init__(self, nom, niveau):
        super().__init__(nom, niveau)
        self.points_vie = 150
        self.puissance_attaque = 20
        self.defense = 40

        # Créer la classe "Combat"

import random

class Combat:
    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2

    def pokemon_a_zero_vie(self, pokemon):
        return pokemon.points_de_vie <= 0

    def nom_du_vainqueur(self):
        if self.pokemon_a_zero_vie(self.pokemon1):
            return self.pokemon2.nom
        elif self.pokemon_a_zero_vie(self.pokemon2):
            return self.pokemon1.nom
        else:
            return None

    def attaque_aleatoire(self):
        return random.randint(0, 1)

    def degats_en_fonction_du_type(self, attaquant, defenseur):
        # implémentation simplifiée pour cet exemple
        if type(attaquant) == type(defenseur):
            return attaquant.puissance_d_attaque
        else:
            return attaquant.puissance_d_attaque // 2

    def enlever_points_de_vie(self, attaquant, defenseur):
        degats = self.degats_en_fonction_du_type(attaquant, defenseur)
        defense = defenseur.defense
        points_de_vie_perdus = degats - defense
        if points_de_vie_perdus < 0:
            points_de_vie_perdus = 0
        defenseur.points_de_vie -= points_de_vie_perdus

    def nom_du_perdant(self):
        if self.pokemon_a_zero_vie(self.pokemon1):
            return self.pokemon1.nom
        elif self.pokemon_a_zero_vie(self.pokemon2):
            return self.pokemon2.nom
        else:
            return None

    def enregistrer_dans_pokedex(self, pokemon):
        # lire le fichier "pokedex.json"
        # vérifier si le pokemon est déjà dans le fichier
        # si non, ajouter le pokemon dans le fichier
        # écrire le fichier "pokedex.json"
        pass
class PokemonNormal(Pokemon):
    def __init__(self, nom, points_de_vie):
        super().__init__(nom, points_de_vie)
        self.niveau = 1
        self.puissance_attaque = 10
        self.defense = 10
        self.type = "Normal"


class PokemonFeu(Pokemon):
    def __init__(self, nom, points_de_vie):
        super().__init__(nom, points_de_vie)
        self.niveau = 1
        self.puissance_attaque = 12
        self.defense = 8
        self.type = "Feu"


class PokemonEau(Pokemon):
    def __init__(self, nom, points_de_vie):
        super().__init__(nom, points_de_vie)
        self.niveau = 1
        self.puissance_attaque = 8
        self.defense = 12
        self.type = "Eau"


class PokemonTerre(Pokemon):
    def __init__(self, nom, points_de_vie):
        super().__init__(nom, points_de_vie)
        self.niveau = 1
        self.puissance_attaque = 10
        self.defense = 10
        self.type = "Terre"

    #Créer le fichier "pokédex.json"


   
import json

class Pokedex:
    def __init__(self):
        self.pokedex = []

    def ajouter_pokemon(self, pokemon):
        if not self.pokemon_deja_present(pokemon):
            self.pokedex.append(pokemon)
            with open("pokedex.json", "w") as f:
                json.dump(self.pokedex, f)

    def pokemon_deja_present(self, pokemon):
        for p in self.pokedex:
            if p["nom"] == pokemon["nom"] and p["niveau"] == pokemon["niveau"]:
                return True
        return False

    def afficher_pokedex(self):
        nb_pokemon = len(self.pokedex)
        print(f"Vous avez rencontré {nb_pokemon} Pokémon :")
        for p in self.pokedex:
            print(p["nom"])

# Exemple d'utilisation
pokedex = Pokedex()
pokemon1 = {"nom": "Pikachu", "type": "Electrique", "niveau": 5}
pokemon2 = {"nom": "Bulbizarre", "type": "Plante", "niveau": 7}
pokedex.ajouter_pokemon(pokemon1)
pokedex.ajouter_pokemon(pokemon2)
pokedex.ajouter_pokemon(pokemon1) # ne sera pas ajouté
pokedex.afficher_pokedex() # affiche Pikachu et Bulbizarre 

# Ajouter le fichier "pokemon.json" 

def ajouter_pokemon():
    # Ouverture du fichier pokemon.json
    with open("pokemon.json", "r") as f:
        pokemons = json.load(f)

    # Saisie des informations sur le nouveau Pokémon
    nom = input("Nom du Pokémon: ")
    points_de_vie = int(input("Points de vie: "))
    type_pokemon = input("Type (Normal, Feu, Eau, Terre): ")

    # Création de l'objet Pokemon correspondant au type choisi
    if type_pokemon == "Normal":
        nouveau_pokemon = PokemonNormal(nom, points_de_vie)
    elif type_pokemon == "Feu":
        nouveau_pokemon = PokemonFeu(nom, points_de_vie)
    elif type_pokemon == "Eau":
        nouveau_pokemon = PokemonEau(nom, points_de_vie)
    elif type_pokemon == "Terre":
        nouveau_pokemon = PokemonTerre(nom, points_de_vie)
    else:
        print("Type de Pokémon invalide")
        return

    # Ajout du nouveau Pokémon à la liste des Pokémons
    pokemons.append(nouveau_pokemon.__dict__)

    # Écriture de la liste mise à jour dans le fichier pokemon.json
    with open("pokemon.json", "w") as f:
        json.dump(pokemons, f)

    print(f"Le Pokémon {nom} a été ajouté avec succès !")