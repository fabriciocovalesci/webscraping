import pytest
from .main import Soma, duplicados

def test_Soma_receive_integer_positive():
    assert Soma(2) == 3
    assert Soma(8) == 36     
    
    
def test_Soma_receive_integer_negative():
    with pytest.raises(ValueError) as e:
        Soma(-8)
    assert str(e.value) == 'Only positive values ​​are accepted'
    
    
def test_Soma_receive_one_must_return_one():
    assert Soma(1) == 1
    
    
def test_Soma_receive_list():
    with pytest.raises(ValueError) as e:
        Soma([1, 2, 3])
    assert str(e.value) == 'This function accepts integers only'
    
    
def test_Soma_receive_dict():
    with pytest.raises(ValueError) as e:
        Soma({"one": 1, "two": 2, "three": 3})
    assert str(e.value) == 'This function accepts integers only'
    

def test_Soma_receive_string():
    with pytest.raises(ValueError) as e:
        Soma("9")
    assert str(e.value) == 'This function accepts integers only'
    
    
def test_duplicados_receive_list_of_strings():
    assert duplicados(["kelless","keenness","Alfalggo"]) == ["keles","kenes","Alfalgo"]
    assert duplicados(["abracadabra","allottee","assessee"]) == ["abracadabra","alote","asese"]
    
    
def test_duplicados_receive_list_of_integers():
    with pytest.raises(ValueError) as e:
        duplicados([2, 4, 5, 6, 7])
    assert str(e.value) == 'List must only contain words with type string'
    
    
def test_duplicados_receive_dict_of_integers():
    with pytest.raises(ValueError) as e:
        duplicados({"one": 1, "two": 2, "three": 3})
    assert str(e.value) == 'This function only takes a string list'
    
    
def test_duplicados_receive_list_of_number_of_type_string():
    assert duplicados(['2', '4', '5', '6', '7']) == ['2', '4', '5', '6', '7']
