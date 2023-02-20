# OC_Projet_7 GrandPyApp

Le programme est une interface de communication où l'on demande à GrandPy s'il connait un lieu, et en fonction de ses connaissances il nous affiche une Google Map du lieu.

## Tout d'abord 

Ces consignes vont vous permettre d'obtenir une copie de mon projet et de le tester avec la console de votre machine.

### Pré-requis 

Le programme étant écrit en Python, il doit être installé sur votre ordinateur. Vous pouvez le télécharger à cette adresse : [Télecharger Python](https://www.python.org/downloads/)

Vous aurez aussi besoin d'une API Key valide pour l'utilisation de [Google Maps](https://developers.google.com/maps/get-started?hl=fr#create-project).

### Installation

Tout d'abord, recupérez mon projet avec cette commande : 

```git clone https://github.com/R4mTex/P7_POUTOT_Simon.git``` 

puis placez-vous dans ce dossier : 

```cd P7_POUTOT_Simon```

Pour ne pas interférer avec d'autres projets, il est conseillé d'exécuter celui-ci dans un environnement virtuel. 
Voici les principales commandes pour :

1. Créer un environnement virtuel 

windows/mac/linux : ```python3 -m venv env```

2. Activer l'environnement virtuel

windows : ```env\Scripts\activate.bat```
mac/linux : ```source env/bin/activate```

Pour en apprendre plus sur les environnements virtuels, vous avez toute la documentation à cette adresse : [Documentation Python](https://docs.python.org/fr/3.6/tutorial/venv.html/)

Pour le bon fonctionnement du programme, il est indispensable d'installer les bibliothèques fournies.
Celles-ci sont listées dans le document ```requirements.txt```.

Une fois la console placée dans le dossier racine du programme, leurs installations se fait via la commande suivante :

```pip install -r requirements.txt```

### Initialisation

Veillez à mettre votre clef Google Map valide à la place de "gmk" dans le fichier "geocoder_api.py" se situant ici : 

```P7_POUTOT_Simon\GrandPyApp\scripts\python\geocoder_api.py```

Maintenant, si la console est placée dans le dossier racine du programme, il suffit d'exécuter la commande :

```python run.py```

Enfin une URL vous sera donnée : ```* Running on http://127.0.0.1:5000``` suivez le lien et vous serez redirigé vers ma page.

Bon essai.

## Écrit avec
[VisualStudioCode](https://code.visualstudio.com/) - Editeur de texte

## Auteur

POUTOT Simon. 

### Remerciements

Merci à **GONNAGE Ranga** pour son soutien.
