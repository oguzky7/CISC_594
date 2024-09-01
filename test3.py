from unittest.mock import patch
from main import main

def test_simpletron():
    # Mock the input to automatically select option 3 (program3.txt) and provide inputs
    inputs = iter(['3', '5', '10'])  # Example inputs: 5 and 10

    with patch('builtins.input', lambda _: next(inputs)):
        main()

if __name__ == "__main__":
    test_simpletron()
