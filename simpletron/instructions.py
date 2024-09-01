# instructions.py

class SimpletronError(Exception):
    """Custom exception class for Simpletron errors."""
    pass

class InstructionSet:
    def __init__(self):
        self.operations = {
            10: self.read,
            11: self.write,
            20: self.load,
            21: self.store,
            30: self.add,
            31: self.subtract,
            32: self.divide,
            33: self.multiply,  # Ensure this line is present
            34: self.mod,       # Ensure other operations are present if needed
            35: self.exp,
            36: self.newline,
            40: self.branch,
            41: self.branch_if_zero,
            42: self.branch_if_negative,
            43: self.halt
        }
        self.actions = []  # to store actions

    # Define the multiply method
    def multiply(self, cpu):
        cpu.accumulator *= cpu.memory.load(cpu.operand)
        self.actions.append({'type': 'multiply', 'address': cpu.operand, 'value': cpu.accumulator})


    def write(self, cpu):
        value = cpu.memory.load(cpu.operand)
        print(f"Result is: {value}, at output address {cpu.operand}")
        self.actions.append({'type': 'write', 'address': cpu.operand, 'value': value})

    def store(self, cpu):
        cpu.memory.store(cpu.operand, cpu.accumulator)
        self.actions.append({'type': 'store', 'address': cpu.operand, 'value': cpu.accumulator})

    def add(self, cpu):
        cpu.accumulator += cpu.memory.load(cpu.operand)
        self.actions.append({'type': 'add', 'address': cpu.operand, 'value': cpu.accumulator})

    def subtract(self, cpu):
        cpu.accumulator -= cpu.memory.load(cpu.operand)
        self.actions.append({'type': 'subtract', 'address': cpu.operand, 'value': cpu.accumulator})

    def divide(self, cpu):
        divisor = cpu.memory.load(cpu.operand)
        if divisor == 0:
            raise SimpletronError("Attempt to divide by zero.")
        cpu.accumulator //= divisor
        self.actions.append({'type': 'divide', 'address': cpu.operand, 'value': cpu.accumulator})

    def exp(self, cpu):
        exponent = cpu.memory.load(cpu.operand)
        cpu.accumulator **= exponent
        self.actions.append({'type': 'exp', 'address': cpu.operand, 'value': cpu.accumulator})

    def newline(self, cpu):
        print("\n", end="")
        self.actions.append({'type': 'newline'})

    def branch(self, cpu):
        cpu.instruction_counter = cpu.operand
        self.actions.append({'type': 'branch', 'address': cpu.operand})

    def branch_if_zero(self, cpu):
        if cpu.accumulator == 0:
            cpu.instruction_counter = cpu.operand
            self.actions.append({'type': 'branch_if_zero', 'address': cpu.operand})

    def branch_if_negative(self, cpu):
        if cpu.accumulator < 0:
            cpu.instruction_counter = cpu.operand
            self.actions.append({'type': 'branch_if_negative', 'address': cpu.operand})

    def halt(self, cpu):
        self.actions.append({'type': 'halt'})
        raise SystemExit


    def load(self, cpu):
        cpu.accumulator = cpu.memory.load(cpu.operand)
        self.actions.append({'type': 'load', 'address': cpu.operand, 'value': cpu.accumulator})
           
           
    def mod(self, cpu):
        divisor = cpu.memory.load(cpu.operand)
        if divisor == 0:
            raise SimpletronError("Attempt to modulo by zero.")
        cpu.accumulator %= divisor
        self.actions.append({'type': 'mod', 'address': cpu.operand, 'value': cpu.accumulator})
        
        # Increment the instruction counter to move to the next instruction
        cpu.instruction_counter += 1
        
        # Fetch the next instruction
        next_instruction = cpu.memory.load(cpu.instruction_counter)
        
        # Extract the opcode
        opcode = next_instruction // 100
        
        # Validate the opcode
        if opcode == 0 or opcode not in self.operations:
            raise SimpletronError(f"Invalid operation code: {opcode} at address {cpu.instruction_counter}")
        

    def read(self, cpu):
        value = int(input(f"Enter a number for address {cpu.operand}: "))
        cpu.memory.store(cpu.operand, value)
        self.actions.append({'type': 'read', 'address': cpu.operand, 'value': value})
