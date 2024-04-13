from fuel import convert, gauge
import pytest


def test_convert():
    assert convert("3/4") == 75
    assert convert("4/4") == 100


def test_convert_errors():
    with pytest.raises(ZeroDivisionError):
        convert("2/0")
    with pytest.raises(ValueError):
        convert("5/4")


def test_gauge():
    assert gauge(40) == "40%"
    assert gauge(80) == "80%"


def test_gauge_full_empty():
    assert gauge(99) == "F"
    assert gauge(1) == "E"
