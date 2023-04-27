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
        # Création d'un nouveau Pokémon
pikachu = Pokemon("Pikachu", niveau=5, puissance_attaque=20, defense=10)

# Affichage des informations générales du Pokémon
pikachu.afficher_informations_generales()  # Pikachu (niveau 5) - PV: 100, DEF: 10, ATK: 20

#Créer les classes pour les types de Pokémon (Normal, Feu, Eau et Terre)
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

    # Créer le fichier "pokédex.json"
import json

class Pokedex:
    def __init__(self):
        self.pokedex = []

    def ajouter_pokemon(self, pokemon):
        if not self.pokemon_est_deja_dans_le_pokedex(pokemon):
            self.pokedex.append(pokemon)
            with open("pokedex.json", "w") as f:
                json.dump(self.pokedex, f)

    def pokemon_est_deja_dans_le_pokedex(self, pokemon):
        for p in self.pokedex:
            if p["nom"] == pokemon["nom"]:
                return True
        return False

    def afficher_pokedex(self):
        nb_pokemon = len(self.pokedex)
        print(f"Vous avez rencontré {nb_pokemon} Pokémon :")
        for p in self.pokedex:
            print(p["nom"])

# Exemple d'utilisation
pokedex = Pokedex()
pokemon = {"nom": "Pikachu", "type": "Electrique", "niveau": 5}
pokedex.ajouter_pokemon(pokemon)
pokedex.afficher_pokedex()

#Utiliser une vérification pour éviter les doublons

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


# Ajouter une fonctionnalité pour ajouter un Pokémon à ce fichier
import json

class PokemonDB:
    def __init__(self, filename):
        self.filename = filename

    def ajouter_pokemon(self, pokemon):
        with open(self.filename, "r") as f:
            data = json.load(f)
        data.append(pokemon)
        with open(self.filename, "w") as f:
            json.dump(data, f)

pokemon = {"nom": "Pikachu", "type": "Electrique", "niveau": 5}
pokemon_db = PokemonDB("pokemon.json")
pokemon_db.ajouter_pokemon(pokemon) 

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

import json

# Définition des classes Pokemon

class Pokemon:
    def __init__(self, nom, points_de_vie):
        self._nom = nom
        self._points_de_vie = points_de_vie
        self._niveau = 1
        self._puissance_attaque = 10
        self._defense = 5

    def afficher_informations(self):
        print("Nom : ", self._nom)
        print("Points de vie : ", self._points_de_vie)
        print("Niveau : ", self._niveau)
        print("Puissance d'attaque : ", self._puissance_attaque)
        print("Défense : ", self._defense)


class PokemonNormal(Pokemon):
    def __init__(self, nom, points_de_vie):
        super().__init__(nom, points_de_vie)
        self._points_de_vie *= 1
        self._puissance_attaque *= 1.2
        self._defense *= 0.8


class PokemonFeu(Pokemon):
    def __init__(self, nom, points_de_vie):
        super().__init__(nom, points_de_vie)
        self._points_de_vie *= 0.9
        self._puissance_attaque *= 1.5
        self._defense *= 0.6


class PokemonEau(Pokemon):
    def __init__(self, nom, points_de_vie):
        super().__init__(nom, points_de_vie)
        self._points_de_vie *= 1.1
        self._puissance_attaque *= 1.1
        self._defense *= 1.2


class PokemonTerre(Pokemon):
    def __init__(self, nom, points_de_vie):
        super().__init__(nom, points_de_vie)
        self._points_de_vie *= 1.3
        self._puissance_attaque *= 0.9
        self._defense *= 1.5


# Définition de la classe Combat

class Combat:
    def __init__(self, pokemon1, pokemon2):
        self._pokemon1 = pokemon1
        self._pokemon2 = pokemon2

    def est_a_zero(self):
        if self._pokemon1._points_de_vie <= 0 or self._pokemon2._points_de_vie <= 0:
            return True
        else:
            return False

    def nom_vainqueur(self):
        if self._pokemon1._points_de_vie > 0:
            return self._pokemon1._nom
        else:
            return self._pokemon2._nom

    def attaque_aleatoire(self):
        return random.choice([self._pokemon1, self._pokemon2])

    def calculer_degats(self, attaquant, defenseur):
        degats = int((attaquant._puissance_attaque * random.uniform(0.8, 1.2)) - (defenseur._defense * random.uniform(0.5, 0.9)))
        return degats if degats > 0 else 0

    def enlever_points_de_vie(self, pokemon, degats):
        pokemon._points_de_vie -= degats

    def nom_perdant(self):
        if self._pokemon1._points_de_vie <= 0:
            return self._pokemon1._nom
        else:
            return self._pokemon2._nom


# menu en début de partie pour permettre les actions suivantes Lancer une partie
#Ajouter un Pokémon dans "pokemon.json"
#ccéder au Pokédex

import json
from random import randint

# Créer la classe Pokemon avec ses attributs et méthodes

class Pokemon:
    def __init__(self, nom, points_de_vie):
        self._nom = nom
        self._points_de_vie = points_de_vie
        self.niveau = 1
        self.puissance_attaque = 10
        self.defense = 5

    def afficher_infos(self):
        print("Nom :", self._nom)
        print("Points de vie :", self._points_de_vie)
        print("Niveau :", self.niveau)
        print("Puissance d'attaque :", self.puissance_attaque)
        print("Défense :", self.defense)

    def attaquer(self, adversaire):
        print(self._nom, "attaque", adversaire._nom)
        if randint(0, 1) == 0:
            print("Attaque réussie !")
            degats = self.calculer_degats(adversaire)
            adversaire.enlever_points_de_vie(degats)
        else:
            print("Attaque ratée !")

    def calculer_degats(self, adversaire):
        if isinstance(adversaire, PokemonFeu):
            return int(self.puissance_attaque * 0.5)
        elif isinstance(adversaire, PokemonEau):
            return int(self.puissance_attaque * 2)
        elif isinstance(adversaire, PokemonTerre):
            return int(self.puissance_attaque * 1.5)
        else:
            return self.puissance_attaque

    def enlever_points_de_vie(self, degats):
        points_de_vie_restants = self._points_de_vie - max(0, degats - self.defense)
        print(self._nom, "a perdu", max(0, degats - self.defense), "points de vie")
        self._points_de_vie = points_de_vie_restants
        if self._points_de_vie <= 0:
            print(self._nom, "est KO !")

class PokemonNormal(Pokemon):
    def __init__(self, nom, points_de_vie):
        super().__init__(nom, points_de_vie)
        self.defense += 1

class PokemonFeu(Pokemon):
    def __init__(self, nom, points_de_vie):
        super().__init__(nom, points_de_vie)
        self.puissance_attaque += 2

class PokemonEau(Pokemon):
    def __init__(self, nom, points_de_vie):
        super().__init__(nom, points_de_vie)
        self.defense += 2

class PokemonTerre(Pokemon):
    def __init__(self, nom, points_de_vie):
        super().__init__(nom, points_de_vie)
        self.puissance_attaque += 1

# Créer la classe Combat avec ses méthodes

class Combat:
    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2

    def est_fini(self):
        return self.pokemon1._points_de_vie <= 0 or self.pokemon2._points_de_vie <= 0

    def obtenir_vainqueur(self):
        if self.pokemon1._points_de_vie > 0:
            return self.pokemon
        
       
       
        # Lors du lancement de la partie, le joueur doit choisir son Pokémon

import random
import json

# Définir une fonction pour créer une instance de pokemon en fonction de son type
def creer_pokemon(nom, type_pokemon, points_de_vie):
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
        return None
    return nouveau_pokemon

# Définir une fonction pour ajouter un pokemon au fichier "pokemon.json"
def ajouter_pokemon(pokemon):
    with open("pokemon.json", "r+") as f:
        data = json.load(f)
        if pokemon.nom not in data.keys():
            data[pokemon.nom] = {
                "type": pokemon.__class__.__name__,
                "pv": pokemon.points_de_vie
            }
            f.seek(0)
            json.dump(data, f, indent=4)
            print(f"{pokemon.nom} a été ajouté au Pokédex !")
        else:
            print(f"{pokemon.nom} est déjà dans le Pokédex.")

# Définir une fonction pour lancer une partie
def lancer_partie():
    # Charger la liste des pokémons depuis le fichier "pokemon.json"
    with open("pokemon.json", "r") as f:
        pokemons = json.load(f)

    # Demander au joueur de choisir son pokemon
    print("Voici la liste des pokémons disponibles :")
    for nom, stats in pokemons.items():
        print(f"- {nom} ({stats['type']})")
    choix_pokemon = input("Choisissez votre pokémon : ")

    # Vérifier que le pokémon choisi existe
    if choix_pokemon not in pokemons.keys():
        print("Pokémon non trouvé dans le Pokédex.")
        return

    # Créer une instance du pokémon choisi par le joueur
    type_pokemon = pokemons[choix_pokemon]["type"]
    points_de_vie = pokemons[choix_pokemon]["pv"]
    joueur_pokemon = creer_pokemon(choix_pokemon, type_pokemon, points_de_vie)

    # Choisir un pokémon aléatoirement pour l'adversaire
    adversaire_nom = random.choice(list(pokemons.keys()))
    adversaire_type = pokemons[adversaire_nom]["type"]
    adversaire_pv = pokemons[adversaire_nom]["pv"]
    adversaire_pokemon = creer_pokemon(adversaire_nom, adversaire_type, adversaire_pv)

    # Lancer le combat
    combat = Combat(joueur_pokemon, adversaire_pokemon)
    gagnant = combat.lancer()

    # Afficher le résultat du combat
    if gagnant == joueur_pokemon:
        print("Vous avez gagné !")
    elif gagnant == adversaire_pokemon:
        print("Vous avez perdu...")
    else:
        print("Match nul.")

# Définir une fonction pour ajouter un pokémon au fichier "pokemon.json"

import json

def ajouter_pokemon():
    nom = input("Nom du Pokémon : ")
    type_pokemon = input("Type du Pokémon : ")
    points_de_vie = int(input("Points de vie : "))

    with open("pokemon.json", "r") as f:
        pokemons = json.load(f)
    
    # Vérifier si le nom du pokemon existe déjà dans le fichier
    for pokemon in pokemons:
        if pokemon['nom'] == nom:
            print("Ce Pokémon existe déjà.")
            return
    
    # Ajouter le nouveau Pokémon à la liste
    nouveau_pokemon = {
        'nom': nom,
        'type': type_pokemon,
        'points_de_vie': points_de_vie
    }
    pokemons.append(nouveau_pokemon)

    # Écrire la liste mise à jour dans le fichier
    with open("pokemon.json", "w") as f:
        json.dump(pokemons, f)

    print(f"Le Pokémon {nom} a été ajouté avec succès !")


