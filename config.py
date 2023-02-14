import os

# To generate a new secret key:
# >>> import random, string
# >>> "".join([random.choice(string.printable) for _ in range(24)])
SECRET_KEY = "#d#JCqTTW\nilK\\7m\x0bp#\tj~#H"

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = True

GOOGLE_MAPS_KEY = "AIzaSyAVtCfvLbfgSm8528irK1sEq5SpSA0zcKY"

GRAND_PY_ANSERS = [
    "Bien sûr mon petit.",
    "Évidemment, quelle question.",
    "Je crois me souvenir...",
    "De mémoire, je dirais ça.",
    "Je ne suis pas sûr de ce que j'avance.",
    "Je ne m'en souviens plus. Va pour le hasard.",
    "Peut-être que c'est ça.",
    "D'abord un verre d'eau, puis ta question"
]