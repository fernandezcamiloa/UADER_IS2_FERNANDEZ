import os

class Ping:
    def __init__(self):
        pass
    
    def execute(self, ip_address):
        if ip_address.startswith("192."):
            for _ in range(10):
                response = os.system("ping -c 1 " + ip_address)
                if response == 0:
                    print(f"Ping exitoso a {ip_address}")
                else:
                    print(f"Fallo al hacer ping a {ip_address}")
        else:
            print("La dirección IP no comienza con '192.', no se puede realizar el ping.")

    def executefree(self, ip_address):
        for _ in range(10):
            response = os.system("ping -c 1 " + ip_address)
            if response == 0:
                print(f"Ping exitoso a {ip_address}")
            else:
                print(f"Fallo al hacer ping a {ip_address}")

class PingProxy:
    def __init__(self):
        self.ping = Ping()
    
    def execute(self, ip_address):
        if ip_address == "192.168.0.254":
            self.ping.executefree("www.google.com")
        else:
            self.ping.execute(ip_address)

# Ejemplo de uso:
proxy = PingProxy()
proxy.execute("192.168.0.1")  # Ejecutará ping a la dirección IP
proxy.execute("8.8.8.8")       # No comenzará con "192.", no se realizará ping
proxy.execute("192.168.0.254") # Realizará ping a www.google.com mediante Ping.executefree()
