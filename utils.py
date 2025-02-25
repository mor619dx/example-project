def read_file(filename):
    with open(filename, "r") as file:
        return file.read()  # Will crash if file doesn't exist