from week_7.numb3rs.numb3rs import validate

def test_valid_addresses():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True
    assert validate("1.1.1.1") == True
    assert validate("192.168.1.1") == True
    assert validate("10.0.0.5") == True

def test_invalid_range():
    assert validate("256.0.0.0") == False
    assert validate("255.256.255.255") == False
    assert validate("127.0.0.256") == False
    assert validate("0.0.-1.0") == False
    assert validate("300.0.0.0") == False
    assert validate("10.1.2.275") == False

def test_invalid_format():
    assert validate("1.2.3.4.5") == False  
    assert validate("1.2.3") == False      
    assert validate("cat") == False        
    assert validate("1..2.3.4") == False    
    assert validate("1.2.3.4 ") == False    
    assert validate(" 1.2.3.4") == False    
    assert validate("1.2.3.4a") == False   
    assert validate("1.2.3") == False
    assert validate("1.2.3.4.5") == False
    assert validate("1.2.3..4") == False
    assert validate("1.2.3.a") == False