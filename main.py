from fastapi import FastAPI

# importacion de rutas
from rutas.usuarios import ruta_usuario

app = FastAPI()
app.title = "Glamping"
app.version = "0.0.1"
# uvicorn main:app --reload

app.include_router(ruta_usuario)


@app.get("/",tags=['Home'])
async def root():
    return {"message": "Hello glamping"}

