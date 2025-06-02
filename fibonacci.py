"""
Fibonacci sequence calculator using recursive method.

This module provides a function to calculate Fibonacci numbers using
a pure recursive approach as requested in the issue.
"""


def fibonacci(n):
    """
    Calculate the nth Fibonacci number using recursive method.
    
    Note: This implementation has exponential time complexity O(2^n).
    For larger inputs (n > 30), consider using memoization or an iterative
    approach for better performance.
    
    Args:
        n (int): The position in the Fibonacci sequence (0-indexed)
        
    Returns:
        int: The nth Fibonacci number
        
    Raises:
        ValueError: If n is negative
        
    Examples:
        >>> fibonacci(0)
        0
        >>> fibonacci(1)
        1
        >>> fibonacci(5)
        5
        >>> fibonacci(10)
        55
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def main():
    """Interactive demonstration of the Fibonacci sequence."""
    print("Fibonacci Sequence Calculator (Recursive Method)")
    print("=" * 45)
    
    print("\nFirst 10 Fibonacci numbers:")
    for i in range(10):
        print(f"F({i}) = {fibonacci(i)}")
    
    print("\nCalculate specific Fibonacci number:")
    try:
        n = int(input("Enter a non-negative integer: "))
        result = fibonacci(n)
        print(f"F({n}) = {result}")
    except ValueError as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("\nGoodbye!")


if __name__ == "__main__":
    main()