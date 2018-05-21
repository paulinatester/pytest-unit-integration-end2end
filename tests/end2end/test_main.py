import main

def test_api_endpoint():
    data = "example_data"
    result = main.api_endpoint(data)
    assert "Processed" in result
    assert data in result
