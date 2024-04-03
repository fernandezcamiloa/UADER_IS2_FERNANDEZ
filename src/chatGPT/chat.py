from openai import OpenAI

# Configura tu clave de API de OpenAI

client = OpenAI(
    api_key=("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")
)

def chat_with_gpt(query):
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
    while True:
        try:
            # Bucle para aceptar la consulta del usuario
            user_query = input("Ingresa tu consulta ('q' para salir): ")
            
            if user_query.lower() == 'q':
                break  # Sale del bucle si el usuario ingresa 'q'
            
            # Verifica si la consulta tiene texto
            if user_query:
                try:
                    # Agrega "You:" al contenido de la consulta antes de imprimirlo y enviarlo
                    print("You:", user_query)
                    
                    # Invoca la función para chatear con GPT-3 y obtiene la respuesta
                    response = chat_with_gpt(user_query)
                    
                    if response:
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

if __name__ == "__main__":
    main()

