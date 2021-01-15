# Documentation

## Introduction
Cette application web intéragit avec l'API OpeenFoodFacts afin de permettre aux utilisateurs de rechercher un substitut plus sain à l'aliment qui lui fait envie. Cette application a été développé avec le framework Python Django possédant une base de données PostgreSQL et un template Bootstrap. La base de données permet à l'utilisateur de se créer un compte et d'enregistrer ses substituts en favoris.

## Installation
Pour tester localement l'application, il est nécessaire de créer quelques variables d'environnement.
La plus importante est la variable ENV. Dans votre environnement virtuel, créé une variable ENV en lui donnant comme valeur, tout sauf 'PROD'.

Exemple : 

    export ENV='NO_PROD'

Si vous souhaitez tester l'application avec Selenium, il vous faudra télécharger le driver de Chrome. Puis, il vous faudra créer une variable d'environnement nommé DRIVER_PATH.

Lien de téléchargement du driver Chrome : https://chromedriver.chromium.org/

Exemple de création de la variable d'environnement : 

    Mac / Linux : 

        export DRIVER_PATH='/Your/path/driver/chromedriver'
    
    Windows :
        
        export DRIVER_PATH='/Your/path/driver/chromedriver.exe'

Sinon, vous pouvez vous rendre à la fin du fichier /project/project/settings.py et modifier la variable SELENIUM_DRIVER_PATH par votre chemin de votre driver.

**Installer les dépendances**

    pip install -r requirements.txt

**Pour lancer le serveur**

    python3 project/manage.py runserver

## Développement
L'application web a été conçu en orienté object (côté backend) afin de conserver la structure de base de Django. La partie Javascript utilise la librairie jQuery.

## Lien du projet
[Projet 8](https://project8-elodiemeunier.herokuapp.com/ "Pur Beurre")