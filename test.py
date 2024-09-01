from unittest.mock import patch
from main import main

def test_simpletron():
    inputs = iter([
        '+1007', '+1008', '+2007', '+3008', '+2109',
        '+1109', '+4300', '-99999', '5', '6'
    ])
    
    with patch('builtins.input', lambda _: next(inputs)):
        main()

if __name__ == "__main__":
    test_simpletron()
