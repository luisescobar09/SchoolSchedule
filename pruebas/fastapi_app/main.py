"""coding=utf-8."""
 
from typing import List
 
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
 
from . import crud, models, schemas
from .database import SessionLocal, engine
 
models.Base.metadata.create_all(bind=engine)
 
app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

############################################ USUARIOS ######################################

#CONSULTAR 1 REGISTRO
@app.get("/usuarios/{email}", tags = ["usuarios"], status_code=status.HTTP_202_ACCEPTED)
async def read_user(email: str, db: Session = Depends(get_db)):
    db_user = crud.query_row_Usuarios(db=db, email=email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return db_user

#CONSULTAR N REGISTROS
@app.get("/usuarios/", tags=["usuarios"], response_model= List[schemas.UserBase], 
status_code=status.HTTP_202_ACCEPTED)
async def get_clientes(db: Session = Depends(get_db), offset: int = 0, limit: int = 10):
    db_user = crud.query_rows_usuarios(db= db, limit=limit, offset=offset)
    if db_user is not None:
        return db_user
    else:
        raise HTTPException(status_code= 404, detail="Consulta no valida")

#INSERTAR
@app.post("/usuarios/", tags = ["usuarios"], status_code=status.HTTP_202_ACCEPTED)
async def create_user(user: schemas.UserBase, db: Session = Depends(get_db)):
    if crud.insert_row_Usuarios(db=db, user_base=user) is True:
        return {"message": "Usuario agregado correctamente"}
    else:
        raise HTTPException(status_code=400, detail="Correo ya registrado")
#ACTUALIZAR
@app.put("/usuarios/", tags=["usuarios"], status_code=status.HTTP_202_ACCEPTED)
async def update_user(user: schemas.UserBase, db: Session = Depends(get_db)):
    if crud.update_row_Usuarios(db=db, user_base=user) is True:
        return {"message": "Usuario actualizado"}
    else:
        raise HTTPException(status_code=404, detail="No se actualizó correctamente")

#BORRAR
@app.delete("/usuarios/{email}", tags=["usuarios"], status_code=status.HTTP_202_ACCEPTED)
async def delete_user(email: str, db: Session = Depends(get_db)):
    if crud.delete_row_Usuarios(db=db, email=email) is True:
        return {"message": "Usuario eliminado"}
    else:
        raise HTTPException(status_code=404, detail="No se eliminó correctamente")

########################################################### CICLO ESCOLAR ############################

@app.post("/planestudios/", tags = ["plan de estudios"], status_code=status.HTTP_202_ACCEPTED)
async def create_plan_estudios(plan_estudios: List[schemas.PlanEstudiosBase], db: Session = Depends(get_db)):
    contador = 0
    for i in plan_estudios:
        if crud.insert_row_plan_estudios(db=db, user_plan=i) is True:
            contador+=1
        else:
            raise HTTPException(status_code=400, detail="No se agrego correctamente")
    if contador == len(plan_estudios):
        return {"message": "Plan de estudios agregado"}
    else:
        raise HTTPException(status_code=400, detail="No se agrego correctamente")


@app.get("/ciclo_escolar/{id_ciclo_escolar}", tags = ["ciclo_escolar"], status_code=status.HTTP_202_ACCEPTED,
response_model=schemas.CicloEscolarBase)
async def read_ciclo_escolar(id_ciclo_escolar: int, db: Session = Depends(get_db)):
    db_ciclo_escolar = crud.query_row_ciclo_escolar(db=db, id_ciclo_escolar=id_ciclo_escolar)
    if db_ciclo_escolar is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return db_ciclo_escolar