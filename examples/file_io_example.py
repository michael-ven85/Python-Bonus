# file_io_example.py
def write_message(filename, message):
    with open(filename, 'w') as file:
        file.write(message)

def read_message(filename):
    with open(filename, 'r') as file:
        return file.read()

def main():
    filename = "sample.txt"
    message = "This is a sample file created for the Python book bonus."
    
    write_message(filename, message)
    read_back = read_message(filename)
    print("File Content:", read_back)

if __name__ == "__main__":
    main()
