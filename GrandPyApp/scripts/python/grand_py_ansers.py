import random

class Grand_py_ansers:
    def random_positive_anser():
        positive_ansers = [
            "Bien sûr mon petit.",
            "Évidemment, quelle question.",
            "Je crois me souvenir...",
            "De mémoire, je dirais ça.",
            "Je ne suis pas sûr de ce que j'avance.",
            "Je ne m'en souviens plus. Va pour le hasard.",
            "Peut-être que c'est ça.",
            "D'abord un verre d'eau, puis ta question."
        ]

        random_positive_anser = positive_ansers[random.randint(0, len(positive_ansers)-1)]
        return random_positive_anser

    def random_negative_anser():
        negative_ansers = [
            "Je n'arrive pas à te lire.",
            "Soigne ton écriture.",
            "Je te réponderais demain.",
            "Aucune idée.",
            "Je ne connais pas cet endroit.",
            "Demande à ta mère.",
            "Il est trop tard pour poser des questions.",
            "Désolé, je perds la mémoire."
        ]

        random_negative_anser = negative_ansers[random.randint(0, len(negative_ansers)-1)]
        return random_negative_anser
