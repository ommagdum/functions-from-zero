import wikipedia

def scrape(name="Carlos Sainz Jr.", length = 4):
    result = wikipedia.summary(name, sentences = length)
    return result