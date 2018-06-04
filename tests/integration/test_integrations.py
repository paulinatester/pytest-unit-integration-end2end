import main

def test_add_integration():
    assert main.add(2, 3) == 5

def test_subtract_integration():
    assert main.subtract(5, 3) == 2

def test_multiply_integration():
    assert main.multiply(2, 4) == 8

def test_divide_integration():
    assert main.divide(6, 2) == 3

def test_divide_by_zero_integration():
    try:
        main.divide(5, 0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero"

def test_api_endpoint_integration(sample_data):
    data = sample_data
    result = main.api_endpoint(data)
    assert "Processed" in result
    assert data in result

