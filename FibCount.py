"""A class to calculate the n'th Fibonacci number, while keeping track of how many calls are made to fibonacci"""
from Fib import Fib


class FibCount(Fib):
    def __init__(self):
        self.calls = 0
        pass

    def fibonacci(self, n):
        self.calls += 1
        return super().fibonacci(n)
