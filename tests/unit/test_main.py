import main

def test_add():
    assert main.add(2, 3) == 5

def test_subtract():
    assert main.subtract(5, 3) == 2

def test_multiply():
    assert main.multiply(2, 4) == 8

def test_divide():
    assert main.divide(6, 2) == 3

def test_divide_by_zero():
    try:
        main.divide(5, 0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero"
