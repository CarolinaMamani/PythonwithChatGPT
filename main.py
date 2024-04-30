import openai
import config
import typer
from rich import print # para mejorar lo visual
from rich.table import Table

def main():
    
    openai.api_key = config.api_key
    
    print('[bold green]ChatGPT API en Python[/bold green]')
    
    table = Table('Comando','Descripcion')
    table.add_row('exit','salir de la app')
    table.add_row('new','crear una nueva conversacion')
    
    print(table)

    context = {"role":"system",
                "content":"Eres un asistente muy util"}

    #contexto del asistente, es como guiarlo para donde quieres que vaya o su rol de lo que hara
    messages = [context]

    while True: # con esto podemos seguir hablando con el
        
        content = __prompt() #el usuario introduce la pregunta

        if  content == "new":
             print('Nueva Conversacion')
             messages = [context]
             content = __prompt()

        messages.append({"role":"user","content":content})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages)
        
        response_contect = response.choices[0].message.content 
        
        messages.append({"role":"assistant","content":response_contect}) #guarda la respuesta que no da
        #asi tendra contexto de todas las preguntas que le hacemos
        # y de todas las respuestas que nos da
        
        print(f"[bold green]>[/bold green] [green]{response_contect}[/green]")

#creamos una funcion privada, retorna un string
def __prompt() -> str:
    prompt =typer.prompt('\nsobre que quieres hablar?: ')
    
    if prompt == "exit": 
       exit = typer.confirm(" Estas seguro?")
       if exit:
            print("Hasta luego!")
            raise  typer.Abort() #typer maneja todo el programa entonces tambien lo puede parar
       return __prompt
    
    return prompt

if __name__ == "__main__":
    typer.run(main)
    
    
    #Funciona bien, pero no lo puedo usar porque no tengo chat pagado
    
    #https://www.youtube.com/watch?v=b8COygWdvmw&ab_channel=MoureDevbyBraisMoure