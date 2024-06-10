import json
import sys

class JSONTokenManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(JSONTokenManager, cls).__new__(cls)
        return cls._instance

    def get_json_value(self, jsonfile, jsonkey="token1"):
        with open(jsonfile, 'r') as myfile:
            data = myfile.read()
        obj = json.loads(data)
        return obj.get(jsonkey, None)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python getJason.py <archivo_json> [clave]")
        sys.exit(1)

    jsonfile = sys.argv[1]
    jsonkey = sys.argv[2] if len(sys.argv) > 2 else "token1"
    manager = JSONTokenManager()
    value = manager.get_json_value(jsonfile, jsonkey)
    
    if value is not None:
        print(value)
    else:
        print(f"Clave '{jsonkey}' no encontrada en el archivo JSON.")
