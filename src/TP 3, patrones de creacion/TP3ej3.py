class Hamburguesa:
    def entrega_en_mostrador(self):
        print("La hamburguesa está lista para ser retirada en mostrador.")

    def retiro_por_cliente(self):
        print("La hamburguesa está lista para ser retirada por el cliente.")

    def entrega_por_delivery(self):
        print("La hamburguesa será entregada por delivery.")


# Ejemplo de uso:
hamburguesa = Hamburguesa()

# Entrega en mostrador
hamburguesa.entrega_en_mostrador()

# Retiro por cliente
hamburguesa.retiro_por_cliente()

# Entrega por delivery
hamburguesa.entrega_por_delivery()
