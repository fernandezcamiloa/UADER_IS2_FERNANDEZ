from abc import ABC, abstractmethod

class Handler(ABC):
    @abstractmethod
    def handle(self, number):
        pass

    @abstractmethod
    def set_next(self, handler):
        pass

class PrimeHandler(Handler):
    def __init__(self):
        self.next_handler = None

    def set_next(self, handler):
        self.next_handler = handler

    def handle(self, number):
        if self.is_prime(number):
            print(f"El número {number} es primo y ha sido consumido.")
        elif self.next_handler:
            self.next_handler.handle(number)
        else:
            print(f"El número {number} no ha sido consumido.")

    def is_prime(self, number):
        if number <= 1:
            return False
        if number <= 3:
            return True
        if number % 2 == 0 or number % 3 == 0:
            return False
        i = 5
        while i * i <= number:
            if number % i == 0 or number % (i + 2) == 0:
                return False
            i += 6
        return True

class EvenHandler(Handler):
    def __init__(self):
        self.next_handler = None

    def set_next(self, handler):
        self.next_handler = handler

    def handle(self, number):
        if number % 2 == 0:
            print(f"El número {number} es par y ha sido consumido.")
        elif self.next_handler:
            self.next_handler.handle(number)
        else:
            print(f"El número {number} no ha sido consumido.")

if __name__ == "__main__":
    prime_handler = PrimeHandler()
    even_handler = EvenHandler()

    prime_handler.set_next(even_handler)

    for number in range(1, 101):
        prime_handler.handle(number)
