# error_handling_example.py
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    else:
        return result

def main():
    print("10 / 2 =", divide(10, 2))
    print("10 / 0 =", divide(10, 0))

if __name__ == "__main__":
    main()
