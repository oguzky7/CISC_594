# memory.py

class Memory:
    def __init__(self, size=100):
        self.size = size
        self.memory = [0] * self.size

    def load(self, address):
        if 0 <= address < self.size:
            return self.memory[address]
        else:
            raise ValueError(f"Invalid memory address: {address}")

    def store(self, address, value):
        if 0 <= address < self.size:
            if -9999 <= value <= 9999:
                self.memory[address] = value
            else:
                raise ValueError(f"Value out of range: {value}")
        else:
            raise ValueError(f"Invalid memory address: {address}")

    def dump(self):
        print("\n*** Memory Dump ***")
        for i in range(0, self.size, 10):
            print(f"{i:02} - {i + 9:02}: {' '.join(f'{x:05}' for x in self.memory[i:i + 10])}")