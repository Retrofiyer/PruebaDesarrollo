import openai
from pydantic import BaseModel

class Document(BaseModel):
    prompt: str = ''

def inference(prompt: str) -> list:
    #token de organización
    openai.organization = 'org-8MmhiXp1RrZmBEsNt0XZEnjY'
    # Token de correo personal porque el correo de la UCE no me funcinó con las pruebas que hice al momento
    # de correr el API en el postman
    openai.api_key = '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'
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            #Asigna un rol a ChatGPT y lo entrena para responder a lo que se le pregunte
            {"role": "system", "content": """Eres un contador de vocales, cuenta las vocales de cualquier texto que se te proporcione
            E.G: Hola
            -tiene un total de 2 vocales"""},
            {"role": "user", "content": prompt}
        ]
    )
    content = completion.choices[0].message.content
    total_tokens = completion.usage.total_tokens
    return [content, total_tokens]
