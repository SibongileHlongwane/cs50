import pytest
from working import convert

def test_valid_conversions_short_format():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"
    assert convert("1 AM to 1 PM") == "01:00 to 13:00"

def test_valid_conversions_long_format():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("12:30 PM to 12:30 AM") == "12:30 to 00:30"
    assert convert("11:59 AM to 12:01 PM") == "11:59 to 12:01"

def test_valid_conversions_mixed_format():
    assert convert("10 AM to 8:50 PM") == "10:00 to 20:50"
    assert convert("10:30 PM to 8 AM") == "22:30 to 08:00"
    assert convert("12 PM to 1:00 PM") == "12:00 to 13:00"

def test_invalid_format():
    with pytest.raises(ValueError):
        convert("9:00 to 5:00")  
    with pytest.raises(ValueError):
        convert("9 AM-5 PM")     
    with pytest.raises(ValueError):
        convert("9:00 AM 5:00 PM") 
    with pytest.raises(ValueError):
        convert("9:AM to 5:PM")    
    with pytest.raises(ValueError):
        convert("9:0 AM to 5 PM")  
    with pytest.raises(ValueError):
        convert("9 AM TO 5 PM")    

def test_invalid_time_values():
    with pytest.raises(ValueError):
        convert("13 PM to 5 PM")   
    with pytest.raises(ValueError):
        convert("9:60 AM to 5 PM")  
    with pytest.raises(ValueError):
        convert("0 AM to 5 PM")    
    with pytest.raises(ValueError):
        convert("12:00 PM to 13:00 PM") 

def test_invalid_input_type():
    with pytest.raises(AttributeError):
        convert(None)
    with pytest.raises(AttributeError):
        convert(123)