"""
Sistema de gestión de tokens y pagos
Propiedad de la compañía (copyright UADER-FCyT-IS2©2024 todos los derechos reservados)
Versión 1.2
"""

import json
import sys


class JSONTokenManager:
    """
    Clase Singleton para gestionar la recuperación de tokens de un archivo JSON.
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(JSONTokenManager, cls).__new__(cls)
        return cls._instance

    @staticmethod
    def get_json_value(jsonfile, jsonkey="token1"):
        """
        Recupera el valor asociado con la clave jsonkey en el archivo JSON jsonfile.

        Args:
            jsonfile (str): Ruta del archivo JSON.
            jsonkey (str): Clave dentro del archivo JSON.

        Returns:
            str: Valor asociado con la clave jsonkey.
        """
        try:
            with open(jsonfile, 'r') as myfile:
                data = myfile.read()
            obj = json.loads(data)
            return obj.get(jsonkey, None)
        except (IOError, json.JSONDecodeError) as error:
            print(f"Error al leer el archivo JSON: {error}")
            return None


class AccountManager:
    """
    Clase para gestionar las cuentas bancarias y realizar pagos balanceados.
    """

    def __init__(self, sitedata_file):
        self.sitedata_file = sitedata_file
        self.accounts = {}
        self.load_accounts()

    def load_accounts(self):
        """
        Carga la información de las cuentas desde un archivo JSON.
        """
        try:
            with open(self.sitedata_file, 'r') as file:
                data = json.load(file)
                self.accounts = data.get('accounts', {})
        except (IOError, json.JSONDecodeError) as error:
            print(f"Error al leer el archivo de datos del sitio: {error}")

    def process_payment(self, amount):
        """
        Procesa un pago de la cantidad especificada de forma balanceada entre las cuentas.

        Args:
            amount (float): Monto del pago a procesar.

        Returns:
            tuple: Número de cuenta y monto del pago realizado.
        """
        for account, balance in self.accounts.items():
            if balance >= amount:
                self.accounts[account] -= amount
                return account, amount
        return None, None

    def list_accounts(self):
        """
        Lista las cuentas y sus saldos actuales.
        """
        for account, balance in self.accounts.items():
            print(f"Cuenta: {account}, Saldo: {balance}")


def main():
    """
    Función principal que maneja la ejecución del script desde la línea de comandos.
    """
    if len(sys.argv) < 2:
        print("Uso: python getJason.py <archivo_json> [clave]")
        sys.exit(1)

    if sys.argv[1] == "-v":
        print("Versión 1.2")
        sys.exit(0)

    jsonfile = sys.argv[1]
    jsonkey = sys.argv[2] if len(sys.argv) > 2 else "token1"
    manager = JSONTokenManager()
    value = manager.get_json_value(jsonfile, jsonkey)

    if value is not None:
        print(value)
    else:
        print(f"Clave '{jsonkey}' no encontrada en el archivo JSON.")

    # Ejemplo de uso del AccountManager
    account_manager = AccountManager('sitedata.json')
    account_manager.list_accounts()
    account, amount = account_manager.process_payment(500)
    if account:
        print(f"Pago de {amount} procesado desde la cuenta {account}")
    else:
        print("No se pudo procesar el pago, saldo insuficiente")


if __name__ == "__main__":
    main()
