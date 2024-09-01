# main.py

from simpletron.cpu import CPU
from simpletron.simpletron_helpers import summarize_instructions

def show_help():
    help_text = """
*** Simpletron Help ***

The Simpletron is a hypothetical computer that runs programs written in Simpletron Machine Language (SML). 
You can enter SML instructions to create programs that the Simpletron will execute.

Basic Instructions:
- Each instruction must be a signed 4-digit integer.
- The first two digits represent the operation code (opcode).
- The last two digits represent the operand (memory address to operate on).

Special Commands:
- Enter -99999 to stop entering your program and start execution.
- Enter 'help' at any time to display this help message.

Example Program to Add Two Numbers:
00 ? +1007  (READ input into address 07)
01 ? +1008  (READ input into address 08)
02 ? +2007  (LOAD from address 07)
03 ? +3008  (ADD value at address 08)
04 ? +2109  (STORE result in address 09)
05 ? +1109  (WRITE value at address 09)
06 ? +4300  (HALT the program)

To test the program, you will be prompted to enter numbers after the program is loaded.

Enjoy using Simpletron!
"""
    print(help_text)

def load_program(cpu):
    print("*** Welcome to Simpletron! ***")
    print("*** Please enter your program one instruction ***")
    print("*** (or data word) at a time into the input ***")
    print("*** Enter -99999 to stop entering your program. ***")
    print("*** Enter 'help' for more information. ***")

    instruction_counter = 0

    while True:
        user_input = input(f"{instruction_counter:02} ? ").strip()

        if user_input.lower() == 'help':
            show_help()
            continue

        try:
            instruction = int(user_input)
            if instruction == -99999:
                break
            if not -9999 <= instruction <= 9999:
                print("Instruction must be a 4-digit signed integer between -9999 and +9999.")
                continue
            cpu.memory.store(instruction_counter, instruction)
            instruction_counter += 1
        except ValueError:
            print("Invalid input. Please enter a 4-digit signed integer or 'help'.")

    print("\n*** Program loading completed ***")
    print("*** Program execution begins ***\n")

def main():
    cpu = CPU()

    # Load and run the program
    load_program(cpu)
    cpu.run()

    # Summarize the actions
    summarize_instructions(cpu, cpu.instruction_set.actions)
    
if __name__ == "__main__":
    main()
