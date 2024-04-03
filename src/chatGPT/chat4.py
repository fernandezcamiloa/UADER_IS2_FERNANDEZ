#Corresponde al punto 4 del TP

from openai import OpenAI
#import readline  # Necesario para leer la entrada del usuario con "cursor Up"
import sys

# Configura tu clave de API de OpenAI
client = OpenAI(
    api_key=("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")
)

last_query = ""  # Variable para almacenar la última consulta realizada
buffer = []  # Buffer para almacenar las consultas y respuestas

def chat_with_gpt(query):
    global last_query
    try:
        # Llamada a la API de OpenAI para generar una completación de chat
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages=[
                {"role": "system", "content": "contexto"},
                {"role": "user", "content": query}
            ],
            temperature=1,
            max_tokens=4096,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        # Devuelve el contenido de la respuesta generada
        return response.choices[0].message.content
    except Exception as e:
        # Imprime un mensaje de error si hay algún problema con la llamada a la API
        print("Error en la llamada a la API de OpenAI:", e)
        return None

def main():
    global last_query, buffer
    # Verifica si se ha pasado el argumento "--convers"
    if "--convers" in sys.argv:
        convers_arg_index = sys.argv.index("--convers")
        sys.argv.pop(convers_arg_index)  # Elimina el argumento "--convers" de la lista de argumentos
        while True:
            try:
                # Bucle para aceptar la consulta del usuario
                user_input = input("Ingresa tu consulta ('q' para salir): ")
                
                if user_input.lower() == 'q':
                    break  # Sale del bucle si el usuario ingresa 'q'
                
                # Si el usuario presiona "cursor Up", recuperar la última consulta realizada
                if user_input == "" and last_query:
                    user_input = last_query
                
                # Verifica si la consulta tiene texto
                if user_input:
                    try:
                        # Almacena la consulta actual como última consulta
                        last_query = user_input
                        
                        # Agrega la consulta al buffer
                        buffer.append({"role": "user", "content": user_input})
                        
                        # Agrega "You:" al contenido de la consulta antes de imprimirlo y enviarlo
                        print("You:", user_input)
                        
                        # Construye los mensajes a enviar a la API, utilizando la última consulta realizada
                        messages = [{"role": "system", "content": "contexto"}] + buffer
                        
                        # Invoca la función para chatear con GPT-3 y obtiene la respuesta
                        response = chat_with_gpt(last_query)
                        
                        if response:
                            # Agrega la respuesta al buffer para ser reenviada en las próximas consultas
                            buffer.append({"role": "chatGPT", "content": response})
                            
                            # Agrega "chatGPT:" a la respuesta antes de imprimirlo
                            print("chatGPT:", response)
                    except Exception as e:
                        # Imprime un mensaje de error si hay algún problema con el tratamiento de la consulta
                        print("Error en el tratamiento de la consulta:", e)
                else:
                    print("Por favor, ingresa una consulta válida.")
            except KeyboardInterrupt:
                # Maneja la interrupción del usuario (Ctrl+C)
                print("\nHas interrumpido la ejecución del programa.")
                break
    else:
        print("El argumento '--convers' no fue especificado. Saliendo del programa.")

if __name__ == "__main__":
    main()

