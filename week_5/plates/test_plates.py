import pytest
from plates import is_valid

def test_length():
    assert is_valid("HELLO") == True
    assert is_valid("HEY") == True 
    
def test_two_letters():
    assert is_valid("CS") == True
    assert is_valid("B") == False
    assert is_valid("B5") == False
    
def test_letters_and_nums():
    assert is_valid("AB12") == True
    assert is_valid("AB12!") == False

def test_numbers_end():
    assert is_valid("CS50P") == False
    assert is_valid("ABC012") == False
    assert is_valid("CS50") == True