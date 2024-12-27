from nlplogic.corenlp import get_phrases

def test_get_phrase():
    assert 'ferrari' in get_phrases("Carlos Sainz Jr.")