from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from turing import turing

app = FastAPI(title="Turing Machine API")

# Configurar CORS para permitir que un frontend se conecte
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # En producción cambiar esto por el dominio real
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TuringRequest(BaseModel):
    cadena_texto: str

@app.post("/api/turing")
def execute_turing(request: TuringRequest):
    """
    Recibe una cadena de texto desde el frontend, la procesa por la máquina de Turing 
    y devuelve el resultado.
    """
    resultado = turing(request.cadena_texto)
    return {
        "status": "success",
        "data": resultado
    }

@app.get("/")
def read_root():
    return {"message": "API de Máquina de Turing funcionando. Usa POST /api/turing para procesar texto."}

# Para ejecutar localmente, usarías en la terminal:
# uvicorn main:app --reload
