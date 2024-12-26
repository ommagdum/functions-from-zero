from wikibot import scrape

def test_scrape():
    assert "Carlos Sainz" in scrape("Carlos Sainz Jr.")