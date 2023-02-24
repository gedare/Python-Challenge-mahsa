"""A class to calculate the n'th Fibonacci number"""


class Fib:
    def __init__(self):
        pass

    def fibonacci(self, n):
        return n if n < 2 else (self.fibonacci(n - 1) + self.fibonacci(n - 2))
