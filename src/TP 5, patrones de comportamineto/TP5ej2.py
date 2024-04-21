class CharIterator:
    def __init__(self, string):
        self._string = string
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._string):
            char = self._string[self._index]
            self._index += 1
            return char
        else:
            raise StopIteration


class ReverseCharIterator:
    def __init__(self, string):
        self._string = string
        self._index = len(string) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= 0:
            char = self._string[self._index]
            self._index -= 1
            return char
        else:
            raise StopIteration


class CharContainer:
    def __init__(self, string):
        self._string = string

    def __iter__(self):
        return CharIterator(self._string)

    def reverse_iter(self):
        return ReverseCharIterator(self._string)


# Ejemplo de uso:
if __name__ == "__main__":
    my_string = "Hola Mundo"
    
    # Recorriendo la cadena en sentido directo
    print("Recorriendo la cadena en sentido directo:")
    for char in CharContainer(my_string):
        print(char)
    
    # Recorriendo la cadena en sentido inverso
    print("\nRecorriendo la cadena en sentido inverso:")
    for char in CharContainer(my_string).reverse_iter():
        print(char)
