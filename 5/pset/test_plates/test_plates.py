from plates import is_valid


def test_valid():
    assert is_valid("CS50")
    assert is_valid("Lucas")


def test_invalid():
    assert not is_valid("CS05")
    assert not is_valid("CS50P")
    assert not is_valid("PI3.14")
    assert not is_valid("H")
    assert not is_valid("OUTATIME")
