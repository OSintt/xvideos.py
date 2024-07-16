import pytest
from xvideos.xvideos import XVideos

@pytest.fixture
def scraper():
    return XVideos()
    
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

def test_search_with_empty_string_params(scraper):
    with pytest.raises(ValueError):
        scraper.search(page=1, k="", sort="", durf="", datef="", quality="", premium=False)

def test_fresh_with_large_page(scraper):
    with pytest.raises(ValueError):
        scraper.fresh(page=99999)

def test_search_with_large_page(scraper):
    result = scraper.search(page=99999, k="example", sort="relevance")
    assert 'pagination' in result

def test_get_verified_with_large_page(scraper):
    with pytest.raises(ValueError):
        scraper.get_verified(page=99999)
        
def test_search_without_page(scraper):
    result = scraper.search(k="example", sort="relevance")
    assert 'pagination' in result

def test_details_with_invalid_url(scraper):
    invalid_url = 'https://invalidsite.com/video'
    with pytest.raises(ValueError):
        scraper.details(invalid_url)

def test_details_with_valid_url(scraper):
    valid_url = 'https://www.xvideos.com/video.udefpih987f/mi_madrastra_perdio_apuesta_en_final_argentina_vs_colombia_y_me_lo_chupa'
    details = scraper.details(valid_url)
    assert 'title' in details
    assert 'url' in details
    assert 'views' in details
    assert 'image' in details
