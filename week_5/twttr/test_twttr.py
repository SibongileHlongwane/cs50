import pytest
from week_5.twttr.twttr import shorten

def test_omit_vowels():
    assert shorten("CS50") == "CS50"
    assert shorten("Twitter") == "Twttr"
    assert shorten("Python") == "Pythn"
    assert shorten("aeiouAEIOU") == ""
    
def test_empty_string():
    assert shorten("") == ""
    
def test_nums_and_symbols():
    assert shorten("123@$%") == "123@$%"