from simpletron.cpu import CPU
from simpletron.simpletron_helpers import summarize_instructions

def show_help():
    with open('help.txt', 'r') as help_file:
            help_text = help_file.read()
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

def load_program_from_file(cpu, filename='program2.txt'):
    try:
        with open(filename, 'r') as file:
            for line_number, line in enumerate(file):
                line = line.strip()
                if not line:
                    continue  # Skip empty lines
                try:
                    instruction = int(line)
                    if instruction == -99999:
                        break  # Stop reading further instructions
                    if not -9999 <= instruction <= 9999:
                        raise ValueError(f"Instruction out of range: {instruction} at line {line_number + 1}")
                    cpu.memory.store(line_number, instruction)
                except ValueError as ve:
                    print(f"Error parsing line {line_number + 1}: '{line}' - {ve}")
                    return
        print("\n*** Program loading completed from file ***")
        print("*** Program execution begins ***\n")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except ValueError:
        print(f"Error: Invalid instruction in file '{filename}'.")

def main():
    cpu = CPU()

    # Ask user whether to enter instructions manually, load from a file, or load a specific file for test3
    mode = input("Would you like to (1) enter the program manually, (2) load 'program2.txt', or (3) load 'program3.txt'? Enter 1, 2, 3 or help: ").strip()

    if mode == '1':
        load_program(cpu)
    elif mode == '2':
        load_program_from_file(cpu, 'program2.txt')
    elif mode == '3':
        load_program_from_file(cpu, 'program3.txt')
    elif mode =='help':
        show_help()
        return
    else:
        print("Invalid option. Exiting.")
        show_help()
        return

    # Run the program
    cpu.run()

    # Summarize the actions
    summarize_instructions(cpu, cpu.instruction_set.actions)
    
    # Perform a memory dump after execution
    cpu.memory.dump()
    
if __name__ == "__main__":
    main()
