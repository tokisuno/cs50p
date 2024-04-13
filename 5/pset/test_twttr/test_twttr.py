from twttr import shorten


def test_vowels():
    assert shorten("AEIOUaeiou") == ""


def test_numbers():
    assert shorten("lucas123") == "lcs123"


def test_punctuation():
    assert shorten("lucas,.,") == "lcs,.,"


def test_names():
    assert shorten("David") == "Dvd"
    assert shorten("Lucas") == "Lcs"
    assert shorten("nOoB") == "nB"
