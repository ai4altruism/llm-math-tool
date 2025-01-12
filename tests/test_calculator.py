import pytest
from math_service.calculator import calculate

def test_basic_arithmetic():
    assert calculate("2 + 2") == 4.0
    assert calculate("3 * 4") == 12.0
    assert calculate("10 / 2") == 5.0
    assert calculate("2 ** 3") == 8.0

def test_math_functions():
    assert calculate("sqrt(16)") == 4.0
    assert calculate("abs(-5)") == 5.0
    assert calculate("max(2, 3, 4)") == 4.0

def test_invalid_expression():
    with pytest.raises(ValueError):
        calculate("import os")  # Should raise ValueError for security
    with pytest.raises(ValueError):
        calculate("os.system('ls')")  # Should raise ValueError for security