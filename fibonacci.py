def fibonacci(n):
    """
    Calculate the nth Fibonacci number using recursive method.
    
    Args:
        n (int): The position in the Fibonacci sequence (0-indexed)
        
    Returns:
        int: The nth Fibonacci number
        
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    
    if n <= 1:
        return n
    
    return fibonacci(n - 1) + fibonacci(n - 2)


def main():
    """Demonstrate the Fibonacci function with some example values."""
    print("Fibonacci Sequence Calculator (Recursive Method)")
    print("=" * 50)
    
    # Calculate and display first 10 Fibonacci numbers
    for i in range(10):
        result = fibonacci(i)
        print(f"fibonacci({i}) = {result}")
    
    print("\nTry calculating a specific number:")
    try:
        n = int(input("Enter a non-negative integer: "))
        result = fibonacci(n)
        print(f"fibonacci({n}) = {result}")
    except ValueError as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("\nProgram interrupted.")


if __name__ == "__main__":
    main()