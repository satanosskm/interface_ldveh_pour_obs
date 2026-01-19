# Interface Livre dont vous êtes le héros pour OBS

## Description

Interface Livre dont vous êtes le héros pour OBS est un outil Python conçu pour les streamers et créateurs de contenu qui souhaitent jouer aux **Livres Dont Vous Êtes le Héros** en direct. L'application propose deux interfaces graphiques distinctes (Inventaire et Combat) permettant à OBS Studio de basculer automatiquement entre les scènes selon la fenêtre active.

Les données sont stockées dans des fichiers texte individuels, ce qui permet à OBS de les afficher en temps réel via des sources texte.

Cet outil est compatible avec la série **Défis Fantastiques**. Il ne fonctionne pas avec tous les tomes de la collection, mais couvre la majorité d'entre eux. L'application a été testée et validée avec le livre **L'épreuve des champions**.

---

## Fonctionnalités

### Double interface

- **Fenêtre Inventaire** : gestion complète du personnage (caractéristiques, objets, notes)
- **Fenêtre Combat** : interface simplifiée pour les affrontements avec suivi de l'ennemi

### Synchronisation en temps réel

- Les deux fenêtres partagent les mêmes fichiers de données
- Mise à jour automatique toutes les 0.5 secondes
- Modification sur une interface instantanément visible sur l'autre

### Intégration OBS

- Deux fenêtres séparées pour exploiter l'auto-switch de scènes OBS
- Fichiers texte individuels lisibles par les sources "Texte (GDI+)" d'OBS
- Positionnement initial des fenêtres optimisé (Inventaire à gauche, Combat à droite)

### Gestion des champs

- **Validation** : touche Entrée pour sauvegarder
- **Annulation** : touche Échap pour annuler les modifications en cours
- Protection contre l'écrasement lors de l'édition active

---

## Champs disponibles

### Interface Inventaire

| Champ | Description |
|-------|-------------|
| Endurance départ | Valeur initiale d'endurance |
| Endurance | Endurance actuelle |
| Habileté départ | Valeur initiale d'habileté |
| Habileté | Habileté actuelle |
| Chance départ | Valeur initiale de chance |
| Chance | Chance actuelle |
| Provisions | Nombre de provisions |
| Objets | Zone de texte pour lister les objets |
| Notes | Zone de texte libre |

### Interface Combat

| Champ | Description |
|-------|-------------|
| Endurance | Endurance du joueur (synchronisée) |
| Habileté | Habileté du joueur (synchronisée) |
| Nom ennemi | Nom de l'adversaire |
| Endurance ennemi | Points de vie de l'ennemi |
| Habileté ennemi | Habileté de l'ennemi |

---

## Dépendances

### Python

- **Python 3.6+** (utilisation de f-strings et pathlib)

### Bibliothèques

| Bibliothèque | Type | Description |
|--------------|------|-------------|
| tkinter | Standard | Interface graphique |
| threading | Standard | Actualisation en arrière-plan |
| time | Standard | Gestion des intervalles |
| pathlib | Standard | Manipulation des fichiers |

Aucune installation supplémentaire requise. Toutes les dépendances font partie de la bibliothèque standard Python.

---

## Installation

1. Cloner le dépôt ou télécharger le script

```bash
git clone https://github.com/votre-utilisateur/interface-ldvelh-obs.git
cd interface-ldvelh-obs

Lancer l'application
Bash

python ldvelh.py
Structure des fichiers
text

interface-ldvelh-obs/
├── ldvelh.py
├── README.md
└── txt_files/
    ├── endurance_depart.txt
    ├── endurance.txt
    ├── habilete_depart.txt
    ├── habilete.txt
    ├── chance_depart.txt
    ├── chance.txt
    ├── provisions.txt
    ├── objets.txt
    ├── notes.txt
    ├── nom_ennemi.txt
    ├── endurance_ennemi.txt
    └── habilete_ennemi.txt
Le dossier txt_files est créé automatiquement au premier lancement.

Configuration OBS
Basculement automatique de scènes
OBS Studio dispose d'un commutateur de scènes intégré. Pour le configurer :

Ouvrir OBS Studio
Aller dans Outils puis Commutateur automatique de scènes
Cocher Activer
Créer deux scènes dans OBS : une pour l'inventaire, une pour le combat
Dans la section Commutateurs de fenêtres, ajouter deux règles :
Fenêtre LDVELH - Inventaire vers la scène Inventaire
Fenêtre LDVELH - Combat vers la scène Combat
Fermer la fenêtre de configuration
Désormais, OBS basculera automatiquement vers la scène appropriée selon la fenêtre active.

Affichage des valeurs
Ajouter une source Texte (GDI+) dans OBS
Cocher Lire depuis un fichier
Sélectionner le fichier .txt correspondant dans le dossier txt_files
Répéter pour chaque valeur à afficher
Utilisation
Lancer le script Python
Les deux fenêtres s'ouvrent simultanément
Remplir les caractéristiques de départ du personnage
Basculer entre les fenêtres selon le contexte de jeu
OBS change automatiquement de scène en fonction de la fenêtre active
Raccourcis clavier
Touche	Action
Entrée	Valider et sauvegarder le champ
Échap	Annuler les modifications
Compatibilité
Série supportée
Ce projet est conçu pour la série Défis Fantastiques (Fighting Fantasy en anglais). Le système de caractéristiques (Endurance, Habileté, Chance) correspond aux règles de cette collection.

Livres testés
L'épreuve des champions
La majorité des livres de la série Défis Fantastiques utilisant le système de règles standard devraient être compatibles. Certains tomes proposant des mécaniques spécifiques pourraient nécessiter des adaptations.
