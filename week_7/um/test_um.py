import pytest
from um import count

def test_single_um():
    assert count("um") == 1

def test_whole_word_matching():
    assert count("hello, um, world") == 1
    assert count("um, what are regular expressions?") == 1
    assert count("um...") == 1
    assert count("...um") == 1

def test_um_in_words():
    assert count("album") == 0
    assert count("umbrella") == 0
    assert count("yummy") == 0

def test_case_insensitivity():
    assert count("UM") == 1
    assert count("Um") == 1
    assert count("uM") == 1
    assert count("um, UM, um") == 3

def test_punctuation_and_whitespace():
    assert count("um?") == 1
    assert count(" um ") == 1
    assert count("um.") == 1
    assert count("Um...") == 1
    assert count("um!") == 1

def test_no_um():
    assert count("hello world") == 0
    assert count("") == 0
    assert count(" ") == 0