from string_utils import StringUtils

uti = StringUtils()

def test_capitilize():
    res = uti.capitilize("привет")
    assert res == "Привет"

def test_capitilize_1():
    res = uti.capitilize("ПРИВЕТ")
    assert res == "Привет"

def test_trim():
     res = uti.trim("  привет")
     assert res == "привет"

def test_trim_1():
     res = uti.trim("при вет")
     assert res == "при вет"
 
def test_to_list():
    res = uti.to_list("1/2/3/4/5", "/")
    assert res == ["1", "2", "3", "4", "5"]

def test_to_list_1():
    res = uti.to_list("", "/")
    assert res == []

def test_to_list_2():
    res = uti.to_list("1/2/3/4/5", ",")
    assert res == ["1/2/3/4/5"]
    
def test_contains():
    res = uti.contains("Привет", "П")
    assert res == True

def test_contains_1():
    res = uti.contains("Привет", "ф")
    assert res == False

def test_delete_symbol():
    res = uti.delete_symbol("Привет", "в")
    assert res == "Приет"

def test_delete_symbol_1():
    res = uti.delete_symbol("Привет", "о")
    assert res == "Привет"

def test_delete_symbol_2():
    res = uti.delete_symbol("12", "о")
    assert res == "12"

def test_starts_with():
    res = uti.starts_with("Привет", "П")
    assert res == True

def test_starts_with_1():
    res = uti.starts_with("Привет", "п")
    assert res == False

def test_starts_with_2():
    res = uti.starts_with("Привет", "Н")
    assert res == False

def test_end_with():
    res = uti.end_with("Привет", "т")
    assert res == True

def test_end_with_1():
    res = uti.end_with("Привет", "Т")
    assert res == False

def test_end_with_2():
    res = uti.end_with("Привет", "з")
    assert res == False

def test_is_empty():
    res = uti.is_empty(" ")
    assert res == True

def test_is_empty_1():
    res = uti.is_empty("г")
    assert res == False

def test_is_empty_2():
    res = uti.is_empty("")
    assert res == True


def test_list_to_string():
    res = uti.list_to_string([1, 2, 3, 4, 5], ",")
    assert res == "1,2,3,4,5"

def test_list_to_string_1():
    res = uti.list_to_string([], ",")
    assert res == ""
    
    
 
 





