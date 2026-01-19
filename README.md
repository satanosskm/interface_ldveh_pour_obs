# Interface Livre Dont Vous Êtes le Héros pour OBS

## Description

**Interface Livre dont vous êtes le héros pour OBS** est un outil Python conçu pour les streamers et créateurs de contenu souhaitant jouer aux *Livres Dont Vous Êtes le Héros* en direct.

L'application propose **deux interfaces graphiques distinctes** (Inventaire et Combat) permettant à **OBS Studio** de basculer automatiquement entre les scènes en fonction de la fenêtre active.

Les données sont stockées dans des **fichiers texte individuels**, ce qui permet à OBS de les afficher en temps réel via des sources texte.

Cet outil est compatible avec la série **Défis Fantastiques**. Il ne fonctionne pas avec tous les tomes de la collection, mais couvre la majorité d'entre eux.

L'application a été **testée et validée avec le livre _L'Épreuve des champions_**.

---

## Fonctionnalités

### Double interface

- **Fenêtre Inventaire**
  - Gestion complète du personnage
  - Caractéristiques, objets et notes
- **Fenêtre Combat**
  - Interface simplifiée pour les affrontements
  - Suivi des caractéristiques de l'ennemi

### Synchronisation en temps réel

- Les deux fenêtres partagent les **mêmes fichiers de données**
- Mise à jour automatique toutes les **0,5 secondes**
- Toute modification sur une interface est **instantanément visible sur l'autre**

### Intégration OBS

- Deux fenêtres séparées pour exploiter l’**auto-switch de scènes** d’OBS
- Fichiers texte individuels lisibles par les sources **Texte (GDI+)**
- Positionnement initial optimisé :
  - Inventaire à gauche
  - Combat à droite

### Gestion des champs

- **Validation** : touche Entrée
- **Annulation** : touche Échap
- Protection contre l’écrasement des données lors de l’édition active

---

## Champs disponibles

### Interface Inventaire

| Champ            | Description                          |
|------------------|--------------------------------------|
| Endurance départ | Valeur initiale d’endurance          |
| Endurance        | Endurance actuelle                   |
| Habileté départ  | Valeur initiale d’habileté           |
| Habileté         | Habileté actuelle                    |
| Chance départ    | Valeur initiale de chance            |
| Chance           | Chance actuelle                      |
| Provisions       | Nombre de provisions                 |
| Objets           | Zone de texte pour lister les objets |
| Notes            | Zone de texte libre                  |

### Interface Combat

| Champ            | Description                        |
|------------------|------------------------------------|
| Endurance        | Endurance du joueur (synchronisée) |
| Habileté         | Habileté du joueur (synchronisée)  |
| Nom ennemi       | Nom de l’adversaire                |
| Endurance ennemi | Points de vie de l’ennemi          |
| Habileté ennemi  | Habileté de l’ennemi               |

---

## Dépendances

### Python

- **Python 3.6+**
- Utilisation de f-strings
- Utilisation de pathlib

### Bibliothèques

| Bibliothèque | Type     | Description                   |
|-------------|----------|-------------------------------|
| tkinter     | Standard | Interface graphique           |
| threading   | Standard | Actualisation en arrière-plan |
| time        | Standard | Gestion des intervalles       |
| pathlib     | Standard | Manipulation des fichiers     |

Aucune installation supplémentaire n’est requise.  
Toutes les dépendances font partie de la **bibliothèque standard Python**.

---

## Installation

### Cloner le dépôt

    git clone https://github.com/votre-utilisateur/interface-ldvelh-obs.git
    cd interface-ldvelh-obs

### Lancer l'application

    python ldvelh.py

---

## Structure des fichiers

Le dossier `txt_files` est créé automatiquement au premier lancement et contient :

    endurance_depart.txt
    endurance.txt
    habilete_depart.txt
    habilete.txt
    chance_depart.txt
    chance.txt
    provisions.txt
    objets.txt
    notes.txt
    nom_ennemi.txt
    endurance_ennemi.txt
    habilete_ennemi.txt

---

## Configuration OBS

### Basculement automatique de scènes

1. Ouvrir OBS Studio
2. Aller dans **Outils → Commutateur automatique de scènes**
3. Cocher **Activer**
4. Créer deux scènes :
   - Inventaire
   - Combat
5. Ajouter deux règles :
   - Fenêtre LDVELH - Inventaire → scène Inventaire
   - Fenêtre LDVELH - Combat → scène Combat
6. Fermer la fenêtre de configuration

OBS basculera automatiquement vers la scène appropriée selon la fenêtre active.

### Affichage des valeurs

1. Ajouter une source **Texte (GDI+)**
2. Cocher **Lire depuis un fichier**
3. Sélectionner le fichier `.txt` correspondant dans le dossier `txt_files`
4. Répéter pour chaque valeur à afficher

---

## Utilisation

1. Lancer le script Python
2. Les deux fenêtres s’ouvrent simultanément
3. Renseigner les caractéristiques de départ du personnage
4. Basculer entre les fenêtres selon le contexte de jeu
5. OBS change automatiquement de scène selon la fenêtre active

---

## Raccourcis clavier

| Touche | Action                          |
|-------|----------------------------------|
| Entrée | Valider et sauvegarder un champ |
| Échap  | Annuler les modifications       |

---

## Compatibilité

### Série supportée

Ce projet est conçu pour la série **Défis Fantastiques** (*Fighting Fantasy*).  
Le système de caractéristiques (Endurance, Habileté, Chance) correspond aux règles standards de cette collection.

### Livres testés

- **L'Épreuve des champions**

La majorité des livres utilisant le système de règles standard devraient être compatibles.  
Certains tomes proposant des mécaniques spécifiques peuvent nécessiter des adaptations.
