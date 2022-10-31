# PROGRAMME DE GESTION DE TOURNOI D'ECHECS


## Prérequis 

Le développement du script a nécessité l'utilisation de plusieurs packages, dans ce sens il faut: 

1. Accéder au répértoire du projet ```https://github.com/TrkSdi/P04_tarik_sadkhi_OC.git```
2. Créer un environnement ``` python -m venv env ```
3. activer l'environnement ``` source env/bin/activate  ```
4. installer le package ```pip install -r requirement.txt ```

## Execution

1. La commande pour activer le script principal: ```python __main__.py```

## Fonctionnalité

Ce programme a pour but de:

1. Créer un tournoi d'échecs selon les règles du système suisse
2. Il permet d'entrer 8 joueurs qui se disputeront des matchs en 4 tours
3. La base de données tournoi, id des joueurs, tours ainsi que les matchs est stockée dans un fichier .json : ```/data/Tournoi.json```
4. La base de données des joueurs est stockée dans un fichier .json : ```/data/Joueurs.json```
5. Le programme génère un rapport complet sur tous les joueurs classé par ordre alphabétique ou classement
6. Le programme génère un rapport sur la liste de tous les tournois
7. Le programme génère un rapport sur les joueurs ou tours ou matchs par tournoi séléctionné
8. Le programme permet de changer le classement de chaque joueur
9. En cas d'interruption après un tour, il est possible de reprendre le tournoi au tour suivant


## Générer rapport conformité PEP8 

1. Générer le rapport par la commande: ```flake8 --format=html --htmldir=flake-report```