# cpu.py

from simpletron.memory import Memory
from simpletron.instructions import InstructionSet

class CPU:
    def __init__(self, memory_size=100):
        self.memory = Memory(memory_size)
        self.accumulator = 0
        self.instruction_counter = 0
        self.instruction_register = 0
        self.operation_code = 0
        self.operand = 0
        self.instruction_set = InstructionSet()

    def fetch(self):
        self.instruction_register = self.memory.load(self.instruction_counter)

    def decode(self):
        self.operation_code = abs(self.instruction_register) // 100
        self.operand = abs(self.instruction_register) % 100

    def execute(self):
        if self.operation_code in self.instruction_set.operations:
            self.instruction_set.operations[self.operation_code](self)
        else:
            raise Exception(f"Invalid operation code: {self.operation_code}")

    def run(self):
        try:
            while True:
                self.fetch()
                self.decode()
                self.instruction_counter += 1
                self.execute()
        except SystemExit:
            # Final result
            final_result = self.instruction_set.actions[-2]['value']  # Assuming the second-to-last action is the result
            print(f"\nWith the instructions you entered, the result is: {final_result}")
            print("\n*** Simpletron execution terminated normally ***")
        except Exception as e:
            print(f"\n*** Simpletron execution terminated with error: {e} ***")
            self.dump()


    def dump(self):
        print("\n*** Memory Dump ***")
        print(f"Accumulator:            {self.accumulator:+05}")
        print(f"Instruction Counter:    {self.instruction_counter:02}")
        print(f"Instruction Register:   {self.instruction_register:+05}")
        print(f"Operation Code:         {self.operation_code:02}")
        print(f"Operand:                {self.operand:02}")

        print("\nMEMORY:")
        for i in range(0, self.memory.size, 10):
            print(f"{i:02}: " + " ".join(f"{self.memory.memory[j]:+05}" for j in range(i, i+10)))
