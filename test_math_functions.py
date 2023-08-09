import math_functions

def test_multiply_positive_numbers():
    result = math_functions.multiply(3, 4)
    assert result == 12

def test_multiply_negative_numbers():
    result = math_functions.multiply(-2, 5)
    assert result == -10

def test_multiply_zero():
    result = math_functions.multiply(7, 0)
    assert result == 0

def test_multiply_float_numbers():
    result = math_functions.multiply(2.5, 3)
    assert result == 7.5
