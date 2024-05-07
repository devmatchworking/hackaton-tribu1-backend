
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
#todo: prompt
def get_openai_response(prompt = ""):
    
    try: 
        completion = client.chat.completions.create(
        model=os.getenv("GPT_MODEL"),
        messages=[
                {
                    "role": "system", 
                    "content": "Eres un experto reclutador y especialista en recursos humanos, ayuda a los aspirantes a elaborar una carta de motivación corta, precisa y personalizada según su información personal para aumentar sus posibilidades de conseguir empleo. Si el aspirante no aporta su info personal, hazlo con información genérica."
                },
                {
                    "role": "user", 
                    "content": "Crea una carta de motivación de máximo tres párrafos tomando en cuenta la siguiente información:" + prompt
                }
            ]
        )    
        response = completion.choices[0].message.content
        
    except Exception as e:
        response = f"Error communicating with OpenAI: {str(e)}"

    return response