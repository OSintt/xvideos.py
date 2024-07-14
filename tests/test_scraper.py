import pytest
from scraper.xvideos import XVideosScraper

@pytest.fixture
def scraper():
    return XVideosScraper()

def test_fresh(scraper):
    result = scraper.fresh(page=2)
    assert 'pagination' in result

def test_search(scraper):
    result = scraper.search(page=2, k="example", sort="relevance")
    assert 'pagination' in result

def test_get_verified(scraper):
    result = scraper.get_verified(page=2)
    assert 'videos' in result
    assert len(result['videos']) > 0

def test_fresh_with_negative_page(scraper):
    with pytest.raises(ValueError, match="Page must be an integer greater than 0"):
        scraper.fresh(page=-1)

def test_search_with_negative_page(scraper):
    with pytest.raises(ValueError, match="Page must be an integer greater than 0"):
        scraper.search(page=-1, k="example", sort="relevance")

def test_get_verified_with_negative_page(scraper):
    with pytest.raises(ValueError, match="Page must be an integer greater than 0"):
        scraper.get_verified(page=-1)

def test_fresh_with_empty_string(scraper):
    result = scraper.fresh(page=1)
    assert isinstance(result, dict)  # Assuming it should return a dictionary

#def test_search_with_empty_string_params(scraper):
    #result = scraper.search(page=1, k="", sort="", durf="", datef="", quality="", premium=False)
    #assert 'pagination' in result

def test_get_verified_with_empty_string(scraper):
    result = scraper.get_verified(page=1)
    assert isinstance(result, dict)  # Assuming it should return a dictionary

#def test_fresh_with_large_page(scraper):
    #result = scraper.fresh(page=99999)
    #assert 'pagination' in result

def test_search_with_large_page(scraper):
    result = scraper.search(page=99999, k="example", sort="relevance")
    assert 'pagination' in result

#def test_get_verified_with_large_page(scraper):
    #result = scraper.get_verified(page=99999)
    #assert 'videos' in result


