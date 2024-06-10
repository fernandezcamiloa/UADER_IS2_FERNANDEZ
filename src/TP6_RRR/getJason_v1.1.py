"""
getJason.py
Propiedad de la compañía (copyright UADER-FCyT-IS2©2024 todos los derechos reservados)
Versión 1.2

Este módulo proporciona funcionalidad para recuperar un valor de un archivo JSON dado una clave.
Incluye una clase Singleton para gestionar la recuperación de tokens de un archivo JSON.
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

if __name__ == "__main__":
    main()

