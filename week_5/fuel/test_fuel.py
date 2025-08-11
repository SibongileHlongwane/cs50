import pytest
from fuel import convert, gauge

def test_convert():
    assert convert("1/100") == 1
    assert convert("99/100") == 99
    assert convert("50/100") == 50
    
    with pytest.raises(ZeroDivisionError):
        convert("10/0")
    with pytest.raises(ValueError):
        convert("8/4")
    with pytest.raises(ValueError):
        convert("-3/4")
    with pytest.raises(ValueError):
        convert("cat/dog")
        
def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    