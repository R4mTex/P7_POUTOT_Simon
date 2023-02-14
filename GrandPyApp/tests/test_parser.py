from GrandPyApp.scripts.python.parser import Parser, oc_stop_words, custom_stop_words
from nltk.tokenize import word_tokenize


# Create your tests here.
def test_should_remove_upper_case():
    sut = Parser
    text = 'ABC'
    expected_value = 'abc'
    assert sut.remove_upper_case(text) == expected_value

def test_should_remove_ponctuation():
    sut = Parser
    text = 'a.b!c?'
    expected_value = 'abc'
    assert sut.remove_ponctuation(text) == expected_value

def test_should_remove_accent():
    sut = Parser
    text = 'áôè'
    expected_value = 'aoe'
    assert sut.remove_accent(text) == expected_value

def test_should_remove_stop_word():
    sut = Parser 
    stop_words = set(oc_stop_words + custom_stop_words)
    text = 'coucou estce connais ladresse'
    word_tokens = word_tokenize(text)
    expected_value = [word for word in word_tokens if not word.lower() in stop_words]

    assert sut.remove_stop_word(text) == expected_value

def test_should_parse():
    sut = Parser
    text = "Salut GrandPy, est-ce que tu sais comment aller sur Paris ?"
    expected_value = ['paris']
    assert sut.script_for_parse(text) == expected_value