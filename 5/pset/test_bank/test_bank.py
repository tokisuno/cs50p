from bank import value


def test_hello():
    assert value("hello") == 0
    assert value("hello, newman") == 0


def test_starts_with_h():
    assert value("How you doing?") == 20


def test_starts_with_w():
    assert value("What's up?") == 100
