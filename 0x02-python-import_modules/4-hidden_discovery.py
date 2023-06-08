import dis

def print_module_names():
    # Load the compiled module
    import hidden_4

    # Disassemble the bytecode of the module
    bytecode = dis.Bytecode(hidden_4)

    # Extract the names of the defined objects
    names = {instr.argval for instr in bytecode if instr.opname == "LOAD_NAME" and not instr.argval.startswith("__")}

    # Print the names in alphabetical order
    for name in sorted(names):
        print(name)

if __name__ == "__main__":
    print_module_names()
