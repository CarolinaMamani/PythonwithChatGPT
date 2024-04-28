import openai
import config

openai.api_key = config.api_key

#contexto del asistente, es como guiarlo para donde quieres que vaya o su rol de lo que hara
messages = [{"role":"system",
             "content":"Eres un asistente muy util"}]

while True: # con esto podemos seguir hablando con el
    content = input('sobre que quieres hablar?') #el usuario introduce la pregunta

    if content is "exit": #para poder parar el programa
        break

    messages.append({"role":"user","content":content})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages)
    
    response_contect = response.choices[0].message.content 
    
    messages.append({"role":"assistant","content":response_contect}) #guarda la respuesta que no da
    #asi tendra contexto de todas las preguntas que le hacemos
    # y de todas las respuestas que nos da
    
    print(response_contect)
