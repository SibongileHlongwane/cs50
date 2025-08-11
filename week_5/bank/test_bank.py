import pytest
from bank import value

def test_starts_with_hello():
    assert value("hello world") == "$0"
    
def test_starts_with_h():
    assert value("hey world") == "$20"
    
def test_starts_with_other():
    assert value("what's up?") == "$100"
    assert value("what's happening?") == "$100"