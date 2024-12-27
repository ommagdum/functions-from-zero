from textblob import TextBlob
import wikipedia


def search_wikipedia(name):
    """Search Wikipedia"""
    print(f"Searching For Name : {name}")
    return wikipedia.search(name)


def summarize_wiki(name):
    """Summarize Wikipedia"""
    print(f"Finding Wikipedia Summary For Name: {name}")
    return wikipedia.summary(name)


def get_text_blob(text):
    """Gets Text Blob Object"""
    blob = TextBlob(text)
    return blob


def get_phrases(name):
    """Find Wikipedia Name And Returns Phrases"""
    text = summarize_wiki(name)
    blob = get_text_blob(text)
    phrases = blob.noun_phrases
    return phrases
