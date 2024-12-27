from nlplogic.corenlp import search_wikipedia, summarize_wiki, get_text_blob, get_phrases

def test_get_phrase():
    assert 'ferrari' in get_phrases("Carlos Sainz Jr.")