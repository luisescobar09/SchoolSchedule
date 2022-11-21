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

############################################ USUARIOS #################################################

#INSERTAR
@app.post("/usuarios/", tags = ["usuarios"], status_code=status.HTTP_202_ACCEPTED)
async def create_user(user: schemas.UserBase, db: Session = Depends(get_db)):
    if crud.insert_row_Usuarios(db=db, user_base=user) is True:
        return {"message": "Usuario agregado correctamente"}
    else:
        raise HTTPException(status_code=400, detail="Correo ya registrado")

#CONSULTAR 1 REGISTRO
@app.get("/usuarios/{email}", tags = ["usuarios"], status_code=status.HTTP_202_ACCEPTED,
response_model=schemas.UserBase)
async def read_user(email: str, db: Session = Depends(get_db)):
    db_user = crud.query_row_Usuarios(db=db, email=email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return db_user

#CONSULTAR N REGISTROS
@app.get("/usuarios/", tags=["usuarios"], response_model= List[schemas.UserBase], 
status_code=status.HTTP_202_ACCEPTED)
async def read_user(db: Session = Depends(get_db), offset: int = 0, limit: int = 10):
    db_user = crud.query_rows_usuarios(db= db, limit=limit, offset=offset)
    if db_user is not None:
        return db_user
    else:
        raise HTTPException(status_code= 404, detail="Consulta no valida")

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
        return {"message": "Usuario eliminado correctamente"}
    else:
        raise HTTPException(status_code=404, detail="No se eliminó correctamente")


############################################ CARRERAS #################################################

#INSERTAR
@app.post("/carreras/", tags = ["carreras"], status_code=status.HTTP_202_ACCEPTED)
async def create_carrera(carrera: schemas.CarrerasBase, db: Session = Depends(get_db)):
    if crud.insert_row_carreras(db=db, user_carrera= carrera) is True:
        return {"message": "Carrera agregada correctamente"}
    else:
        raise HTTPException(status_code=400, detail="No se agregó correctamente")

#CONSULTAR 1 REGISTRO
@app.get("/carreras/{id_carrera}", tags = ["carreras"], status_code=status.HTTP_202_ACCEPTED, 
response_model=schemas.CarrerasResponseBase)
async def read_carrera(id_carrera: int, db: Session = Depends(get_db)):
    db_carreras = crud.query_row_carrera(db= db, id_carrera= id_carrera)
    if db_carreras is None:
        raise HTTPException(status_code=404, detail="Carrera no encontrada")
    return db_carreras

#CONSULTAR N REGISTROS
@app.get("/carreras/", tags = ["carreras"], status_code=status.HTTP_202_ACCEPTED, 
response_model= List[schemas.CarrerasResponseBase])
async def read_carreras(db: Session = Depends(get_db)):
    db_carreras = crud.query_row_carreras(db= db)
    if db_carreras is None:
        raise HTTPException(status_code=404, detail="Elementos no encontrados")
    return db_carreras

#ACTUALIZAR
@app.put("/carreras/", tags=["carreras"], status_code=status.HTTP_202_ACCEPTED)
async def update_carrera(carrera: schemas.CarrerasBase, db: Session = Depends(get_db)):
    if crud.update_row_carreras(db=db, carrera=carrera) is True:
        return {"message": "Carrera actualizada correctamente"}
    else:
        raise HTTPException(status_code=404, detail="No se actualizó correctamente")

#BORRAR
@app.delete("/carreras/{id_carrera}", tags=["carreras"], status_code=status.HTTP_202_ACCEPTED)
async def delete_carrera(id_carrera: int, db: Session = Depends(get_db)):
    if crud.delete_row_carreras(db=db, id_carrera=id_carrera) is True:
        return {"message": "Carrera eliminada correctamente"}
    else:
        raise HTTPException(status_code=404, detail="No se eliminó correctamente")

########################################################### CICLO ESCOLAR ############################

#INSERTAR
@app.post("/ciclo_escolar/", tags = ["ciclo escolar"], status_code=status.HTTP_202_ACCEPTED)
async def create_ciclo_escolar(ciclo_escolar: schemas.CicloEscolarBase, db: Session = Depends(get_db)):
    if crud.insert_row_ciclo_escolar(db=db, cicloUser= ciclo_escolar) is True:
        return { "message" : "Ciclo escolar agregado" }        
    else:
        raise HTTPException(status_code=400, detail="No se agrego correctamente")

@app.get("/ciclo_escolar/{id_ciclo_escolar}", tags = ["ciclo escolar"], status_code=status.HTTP_202_ACCEPTED,
response_model=schemas.CicloEscolarBase)
async def read_ciclo_escolar(id_ciclo_escolar: int, db: Session = Depends(get_db)):
    db_ciclo_escolar = crud.query_row_ciclo_escolar(db=db, id_ciclo_escolar= id_ciclo_escolar)
    if db_ciclo_escolar is None:
        raise HTTPException(status_code=404, detail="Ciclo escolar no encontrado")
    else:
        return db_ciclo_escolar

#ACTUALIZAR
@app.put("/ciclo_escolar/", tags=["ciclo escolar"], status_code=status.HTTP_202_ACCEPTED)
async def update_ciclo_escolar(user: schemas.CicloEscolarBase, db: Session = Depends(get_db)):
    if crud.update_row_ciclo_escolar(db=db, ciclo_escolar=user) is True:
        return {"message": "Ciclo escolar actualizado correctamente"}
    else:
        raise HTTPException(status_code=404, detail="No se actualizó correctamente")

#BORRAR
@app.delete("/ciclo_escolar/{id_ciclo_escolar}", tags=["ciclo escolar"], status_code=status.HTTP_202_ACCEPTED)
async def delete_user(id_ciclo_escolar: int, db: Session = Depends(get_db)):
    if crud.delete_row_ciclo_escolar(db=db, id_ciclo_escolar= id_ciclo_escolar) is True:
        return {"message": "Ciclo escolar eliminado correctamente"}
    else:
        raise HTTPException(status_code=404, detail="No se eliminó correctamente")

########################################################### PLAN DE ESTUDIOS ############################

@app.post("/plan_estudios/", tags = ["plan estudios"], status_code=status.HTTP_202_ACCEPTED)
async def create_plan_estudios(plan_estudios: List[schemas.PlanEstudiosBase], db: Session = Depends(get_db)):
    contador = 0
    for i in plan_estudios:
        if crud.insert_row_plan_estudios(db=db, user_plan=i) is True:
            contador+=1
        else:
            raise HTTPException(status_code=400, detail="No se agrego correctamente")
    if contador == len(plan_estudios):
        contador = 0
        return {"message": "Plan de estudios agregado"}
    else:
        raise HTTPException(status_code=400, detail="No se agrego correctamente")

@app.get("/plan_estudios/{id_plan_estudios}", tags = ["plan estudios"], status_code=status.HTTP_202_ACCEPTED,
response_model=schemas.PlanEstudiosBase)
async def read_plan_estudios(id_plan_estudios: int, db: Session = Depends(get_db)):
    db_plan_estudios = crud.query_row_plan_estudios(db=db, id_plan_estudios= id_plan_estudios)
    if db_plan_estudios is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    else:
        return db_plan_estudios

@app.get("/plan_estudios/", tags = ["plan estudios"], status_code=status.HTTP_202_ACCEPTED,
response_model=List[schemas.PlanEstudiosBase])
async def read_plan_estudios_completo(carrera: int, db: Session = Depends(get_db)):
    db_plan_estudios = crud.query_rows_plan_estudios(db=db, carrera= carrera)
    if db_plan_estudios is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    else:
        return db_plan_estudios

#ACTUALIZAR
@app.put("/plan_estudios/", tags=["plan estudios"], status_code=status.HTTP_202_ACCEPTED)
async def update_plan_estudios(plan_estudios: List[schemas.PlanEstudiosBase], db: Session = Depends(get_db)):
    contador = 0
    for i in plan_estudios:
        if crud.update_row_plan_estudios(db=db, id_plan_estudios= i) is True:
            contador+=1
        else:
            raise HTTPException(status_code=400, detail="No se agrego correctamente")
    if contador == len(plan_estudios):
        contador = 0
        return {"message": "Plan de estudios actualizado correctamente"}
    else:
        raise HTTPException(status_code=400, detail="No se agrego correctamente")

#BORRAR
@app.delete("/plan_estudios/{id_plan_estudios}", tags=["plan estudios"], status_code=status.HTTP_202_ACCEPTED)
async def delete_plan_estudios(id_plan_estudios: int, db: Session = Depends(get_db)):
    if crud.delete_row_plan_estudios(db=db, id_plan_estudios= id_plan_estudios) is True:
        return {"message": "Materia eliminada correctamente"}
    else:
        raise HTTPException(status_code=404, detail="No se eliminó correctamente")

########################################################### GRUPOS ###################################

#INSERTAR
@app.post("/grupos/", tags = ["grupos"], status_code=status.HTTP_202_ACCEPTED)
async def create_grupo(grupo: schemas.GruposBase, db: Session = Depends(get_db)):
    if crud.insert_row_grupos(db=db, grupo_base= grupo) is True:
        return { "message" : "Grupo agregado correctamente" }        
    else:
        raise HTTPException(status_code=400, detail="No se agrego correctamente")

@app.get("/grupos/", tags = ["grupos"], status_code=status.HTTP_202_ACCEPTED,
response_model= List[schemas.GruposBase])
async def read_grupos(ciclo_escolar: int, carrera: int, db: Session = Depends(get_db)):
    db_grupos = crud.query_rows_grupos(db=db, ciclo_escolar= ciclo_escolar, carrera= carrera)
    if db_grupos is None:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    else:
        return db_grupos

#ACTUALIZAR
@app.put("/grupos/", tags=["grupos"], status_code=status.HTTP_202_ACCEPTED)
async def update_grupos(grupo: schemas.GruposBase, db: Session = Depends(get_db)):
    if crud.update_row_grupos(db=db, grupo_base= grupo) is True:
        return {"message": "Grupo actualizado correctamente"}
    else:
        raise HTTPException(status_code=404, detail="No se actualizó correctamente")

#BORRAR
@app.delete("/grupos/{id_grupo}", tags=["grupos"], status_code=status.HTTP_202_ACCEPTED)
async def delete_user(id_grupo: int, db: Session = Depends(get_db)):
    if crud.delete_row_grupos(db=db, id_grupo= id_grupo) is True:
        return {"message": "Grupo eliminado correctamente"}
    else:
        raise HTTPException(status_code=404, detail="No se eliminó correctamente")