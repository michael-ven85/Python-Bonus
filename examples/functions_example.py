# functions_example.py
def add(a, b):
    """Return the sum of a and b."""
    return a + b

def greet(name):
    """Return a greeting message."""
    return f"Hello, {name}!"

def main():
    sum_result = add(5, 7)
    greeting_message = greet("World")
    print("Sum:", sum_result)
    print(greeting_message)

if __name__ == "__main__":
    main()
