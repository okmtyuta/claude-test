"""
Comprehensive test suite for the Fibonacci sequence calculator.

This module contains unit tests for the recursive Fibonacci implementation,
covering edge cases, error conditions, and correctness verification.
"""

import unittest
from fibonacci import fibonacci


class TestFibonacci(unittest.TestCase):
    """Test cases for the fibonacci function."""

    def test_base_cases(self):
        """Test the base cases of the Fibonacci sequence."""
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)

    def test_small_values(self):
        """Test small Fibonacci numbers."""
        expected_values = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        for i, expected in enumerate(expected_values):
            with self.subTest(n=i):
                self.assertEqual(fibonacci(i), expected)

    def test_medium_values(self):
        """Test medium-sized Fibonacci numbers."""
        test_cases = [
            (10, 55),
            (12, 144),
            (15, 610),
            (20, 6765)
        ]
        for n, expected in test_cases:
            with self.subTest(n=n):
                self.assertEqual(fibonacci(n), expected)

    def test_negative_input_raises_error(self):
        """Test that negative inputs raise ValueError."""
        negative_values = [-1, -5, -10, -100]
        for n in negative_values:
            with self.subTest(n=n):
                with self.assertRaises(ValueError):
                    fibonacci(n)

    def test_error_message(self):
        """Test that the error message is correct."""
        with self.assertRaises(ValueError) as context:
            fibonacci(-1)
        self.assertEqual(str(context.exception), "n must be non-negative")

    def test_type_consistency(self):
        """Test that the function returns integers."""
        for i in range(10):
            with self.subTest(n=i):
                result = fibonacci(i)
                self.assertIsInstance(result, int)

    def test_mathematical_property(self):
        """Test the mathematical property: F(n) = F(n-1) + F(n-2)."""
        for n in range(2, 15):
            with self.subTest(n=n):
                self.assertEqual(
                    fibonacci(n),
                    fibonacci(n - 1) + fibonacci(n - 2)
                )

    def test_golden_ratio_property(self):
        """Test the golden ratio approximation for larger values."""
        # For large n, F(n+1)/F(n) should approximate the golden ratio (1.618...)
        n = 15
        golden_ratio_approx = fibonacci(n + 1) / fibonacci(n)
        golden_ratio = (1 + 5 ** 0.5) / 2
        self.assertAlmostEqual(golden_ratio_approx, golden_ratio, places=1)

    def test_sequence_ordering(self):
        """Test that the sequence is monotonically increasing for positive values."""
        for n in range(1, 20):
            with self.subTest(n=n):
                self.assertLessEqual(fibonacci(n - 1), fibonacci(n))

    def test_parity_pattern(self):
        """Test the pattern of even/odd Fibonacci numbers."""
        # Every third Fibonacci number is even
        for i in range(0, 15, 3):
            with self.subTest(n=i):
                self.assertEqual(fibonacci(i) % 2, 0)


class TestFibonacciEdgeCases(unittest.TestCase):
    """Test edge cases and boundary conditions."""

    def test_large_negative_number(self):
        """Test very large negative number."""
        with self.assertRaises(ValueError):
            fibonacci(-1000)


class TestFibonacciPerformance(unittest.TestCase):
    """Test performance characteristics (within reasonable limits)."""

    def test_reasonable_performance(self):
        """Test that the function completes for moderately large inputs."""
        # Note: Recursive Fibonacci is inefficient for large n,
        # but should complete for n=25 in reasonable time
        import time
        start_time = time.time()
        result = fibonacci(25)
        end_time = time.time()
        
        self.assertEqual(result, 75025)  # Known value for F(25)
        # This is generous - should complete much faster on modern hardware
        self.assertLess(end_time - start_time, 10.0)


def run_tests():
    """Run all tests and display results."""
    unittest.main(verbosity=2)


if __name__ == "__main__":
    run_tests()