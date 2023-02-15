from ..scripts.python.grand_py_ansers import Grand_py_ansers


def test_should_return_a_positive_anser():
    sut = Grand_py_ansers
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

    assert sut.random_positive_anser() in positive_ansers


def test_should_return_a_negative_anser():
    sut = Grand_py_ansers
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

    assert sut.random_negative_anser() in negative_ansers
