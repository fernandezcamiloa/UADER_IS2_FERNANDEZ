class Observer:
    def update(self, id):
        pass

class Subject:
    def __init__(self):
        self._observers = []

    def subscribe(self, observer):
        self._observers.append(observer)

    def emit_id(self, id):
        for observer in self._observers:
            observer.update(id)


class SpecificObserver(Observer):
    def __init__(self, specific_id):
        self.specific_id = specific_id

    def update(self, id):
        if id == self.specific_id:
            print(f"El ID emitido coincide con el ID esperado: {id}")


# Crear el subject
subject = Subject()

# Crear las instancias de los observadores específicos
observer1 = SpecificObserver("ABCD")
observer2 = SpecificObserver("EFGH")
observer3 = SpecificObserver("WXYZ")
observer4 = SpecificObserver("1234")

# Suscribir los observadores al subject
subject.subscribe(observer1)
subject.subscribe(observer2)
subject.subscribe(observer3)
subject.subscribe(observer4)

# Emitir 8 IDs, asegurándose de que al menos 4 coincidan con los IDs de los observadores
ids = ["ABCD", "WXYZ", "1234", "EFGH", "5678", "9012", "3456", "XYZW"]
print("Emitiendo IDs:")
for id in ids:
    subject.emit_id(id)
