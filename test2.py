from unittest.mock import patch
from main import main

def test_simpletron_file_input():
    inputs = iter([
        '2',  # Select file input mode
        '5',  # Input for READ at address 07
        '6',  # Input for READ at address 08
    ])
    
    with patch('builtins.input', lambda _: next(inputs)):
        main()

if __name__ == "__main__":
    test_simpletron_file_input()
