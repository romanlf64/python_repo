import pytest
from string_utils import StringUtils

string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected



@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    (" Test", "Test"),
    ("  1234","1234"),
    ("     Hello World!","Hello World!")
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),
    ("  ", ""),
    ("test  ", "test  ")
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected



@pytest.mark.positive
@pytest.mark.parametrize("string, symbol", [
    ("test", "s"),
    ("house", "u")
])
def test_contains_positive(string, symbol):
    assert string_utils.contains(string, symbol) == True

@pytest.mark.negative
@pytest.mark.parametrize("string, symbol", [
    ("test", "o"),
    ("house", "t")
])
def test_contains_negative(string, symbol):
    assert string_utils.contains(string, symbol) == False



@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, new_result", [
    ("test", "t", "es"),
    ("house", "ous", "he"),
    ("banana", "na", "ba")
])
def test_delete_positive(string, symbol, new_result):
    assert string_utils.delete_symbol(string, symbol) == new_result

@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, new_result", [
    ("test", "o", "test"),
    ("house", "na", "house")
])
def test_delete_negative(string, symbol, new_result):
    assert string_utils.delete_symbol(string, symbol) == new_result