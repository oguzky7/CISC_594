def summarize_instructions(cpu, actions):
    print("\n*** Instruction Summary ***")
    
    if not actions:
        print("No actions were recorded. Ensure the program was entered correctly and try again.")
        return

    for action in actions:
        if action['type'] == 'read':
            print(f"Stored {action['value']} at memory address {action['address']:02}.")
        elif action['type'] == 'load':
            print(f"Loaded {action['value']} from memory address {action['address']:02} into the accumulator.")
        elif action['type'] == 'add':
            print(f"Added the value {action['value']} from memory address {action['address']:02} to the accumulator.")
        elif action['type'] == 'store':
            print(f"Stored the result '{action['value']}' in memory address {action['address']:02}.")
        elif action['type'] == 'write':
            print(f"Printed the result stored in memory address {action['address']:02}.")

    print("\n")
