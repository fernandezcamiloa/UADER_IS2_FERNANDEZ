from openai import OpenAI
import sys

# Configura tu clave de API de OpenAI
client = OpenAI(api_key="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")

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

def handle_user_input():
    global last_query, buffer
    while True:
        try:
            user_input = input("Ingresa tu consulta ('q' para salir): ")
            
            if user_input.lower() == 'q':
                break
                
            if user_input == "" and last_query:
                user_input = last_query
                
            if user_input:
                try:
                    last_query = user_input
                    buffer.append({"role": "user", "content": user_input})
                    print("You:", user_input)
                    
                    messages = [{"role": "system", "content": "contexto"}] + buffer
                    response = chat_with_gpt(last_query)
                    
                    if response:
                        buffer.append({"role": "chatGPT", "content": response})
                        print("chatGPT:", response)
                except Exception as e:
                    print("Error en el tratamiento de la consulta:", e)
            else:
                print("Por favor, ingresa una consulta válida.")
        except KeyboardInterrupt:
            print("\nHas interrumpido la ejecución del programa.")
            break

def main():
    if "--convers" in sys.argv:
        convers_arg_index = sys.argv.index("--convers")
        sys.argv.pop(convers_arg_index)
        handle_user_input()
    else:
        print("El argumento '--convers' no fue especificado. Saliendo del programa.")

if __name__ == "__main__":
    main()
