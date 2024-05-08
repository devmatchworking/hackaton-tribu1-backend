import os
from fastapi import APIRouter
from models.letter import Letter
from models.user_info import UserInfo
from models.enterprise_info import EnterpriseInfo
from openai import OpenAI
from docx import Document
from fastapi.responses import FileResponse


router = APIRouter(
    tags=["Letter Routes"]
)
client = OpenAI()

letter_created = ""


@router.post("/letter", response_model=Letter, status_code=201)
async def create_letter(user_info: UserInfo, enterprise_info: EnterpriseInfo) -> Letter:
    name = user_info.name
    vacant = enterprise_info.vacant
    enterprise = enterprise_info.name
    experience = user_info.experience

    promt = f"Crea una carta de intencion para la empresa {enterprise} que tiene disponible una vacante de {
        vacant}, ten en cuenta que tengo experiencia en {experience} y mi nombre es {name}, la carta debe tener minimo 350 caracteres"
    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": promt}
        ]
    )
    letter = response.choices[0].message.content
    global letter_created
    letter_created = letter
    return Letter(content=letter_created)


@router.get('/save-letter')
async def save_letter():
    if letter_created:
        documento = Document()
        documento.add_paragraph(letter_created)
        ruta_descargas = os.path.expanduser('~/Descargas')
        if not os.path.exists(ruta_descargas):
            os.makedirs(ruta_descargas)

        ruta_archivo = os.path.join(ruta_descargas, 'Carta_Matchworking.docx')
        documento.save(ruta_archivo)
        return FileResponse(ruta_archivo, media_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document', filename='Carta_Matchworking.docx')
    else:
        return {"message": "La carta aun no ha sido generada"}
