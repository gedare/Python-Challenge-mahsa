"""A class to calculate the n'th Fibonacci number, while keeping track of how many calls are made to fibonacci"""
from Fib import Fib


class FibCount(Fib):
    def __init__(self):
        self.calls = 0
        pass

    def fibonacci(self, n):
        self.calls += 1
        return super().fibonacci(n)


class FibCache(FibCount):
    def __init__(self):
        self.calls = 0
        self.known_values = {}

    def fibonacci(self, n):
        self.calls += 1
        if n in self.known_values:
            return self.known_values[n]
        elif n < 2:
            self.known_values[n] = n
            return self.known_values[n]
        else:
            self.known_values[n] = self.fibonacci(n - 1) + self.fibonacci(n - 2)
            return self.known_values[n]
