"""coding=utf-8."""
from sqlalchemy.orm import Session 
from . import models, schemas

#################################################### USUARIOS ##########################################

#Insertar
def insert_row_Usuarios(db: Session, user_base: schemas.UserBase):
        try:
            db_user = models.Usuarios(nombre_usuario = user_base.nombre_usuario, apellido_paterno = user_base.apellido_paterno,
                apellido_materno = user_base.apellido_materno, email = user_base.email, tipo_usuario = user_base.tipo_usuario)
            db.add(db_user)
            db.commit()
            db.refresh(db_user)
            return True
        except Exception as error:
            print(error)
            return False

#Consultar 1 registro
def query_row_Usuarios(db: Session, email: str):
    try:
        user = db.query(models.Usuarios.id_usuario, models.Usuarios.nombre_usuario, models.Usuarios.apellido_paterno, 
        models.Usuarios.apellido_materno, models.Usuarios.email, models.Usuarios.tipo_usuario).filter(
            models.Usuarios.email == email
        ).first()
        if user:
                return dict(user)
        else:
                return None
    except Exception as error:
        print(error)
        return None
#Consultar N registros
def query_rows_usuarios(db: Session, limit, offset):
    users = db.query(models.Usuarios.id_usuario, models.Usuarios.nombre_usuario,
    models.Usuarios.apellido_paterno, models.Usuarios.apellido_materno, models.Usuarios.email, models.Usuarios.tipo_usuario).order_by(models.Usuarios.id_usuario.asc()).limit(limit).offset(offset)
    if users:
        return [dict(i) for i in users]
    else:
        return None

#Actualizar
def update_row_Usuarios(db: Session, user_base: schemas.UserBase):
    try:
        db.query(models.Usuarios).filter(
                models.Usuarios.id_usuario == user_base.id_usuario 
        ).update(
                {
                    models.Usuarios.nombre_usuario : user_base.nombre_usuario,
                    models.Usuarios.apellido_paterno : user_base.apellido_paterno,
                    models.Usuarios.apellido_materno : user_base.apellido_materno,
                    models.Usuarios.email : user_base.email,
                    models.Usuarios.tipo_usuario : user_base.tipo_usuario,
                }
        )
        db.commit()
        return True
    except Exception as error:
        print(error)
        return False

#Eliminar
def delete_row_Usuarios(db: Session, email: str):
    try:
        db.query(models.Usuarios).filter(
                models.Usuarios.email == email
        ).delete()
        db.commit()
        return True
    except Exception as error:
        print(error)
        return False

########################################################### CARRERAS ############################

def insert_row_carreras(db:Session, user_carrera:schemas.CarrerasBase):
        try:
            carrera = models.Carreras(nombre_carrera = user_carrera.nombre_carrera, coordinador_carrera = user_carrera.coordinador_carrera)
            db.add(carrera)
            db.commit()
            return True
        except Exception as error:
            print(error)
            return False
        
#Consultar
def query_row_carreras(db: Session, id_carrera: int):
    try:
        carrera = db.query(models.Carreras.id_carrera, models.Carreras.nombre_carrera, 
        models.Usuarios.id_usuario, models.Usuarios.nombre_usuario, models.Usuarios.apellido_paterno, 
        models.Usuarios.apellido_materno).join(models.Usuarios).filter(models.Carreras.id_carrera == id_carrera).first()
        if carrera:
                return dict(carrera)
        else:
                return None
    except Exception as error:
        print(error)
        return None

#Actualizar
def update_row_carreras(db:Session, carrera:schemas.CarrerasBase):
    try:
        db.query(models.Carreras).filter(
                models.Carreras.id_carrera == carrera.id_carrera 
        ).update(
                {
                    models.Carreras.nombre_carrera : carrera.nombre_carrera,
                    models.Carreras.coordinador_carrera : carrera.coordinador_carrera
                }
        )
        db.commit()
        return True
    except Exception as error:
        print(error)
        return False

#Eliminar
def delete_row_carreras(db:Session, id_carrera: int):
    try:
        db.query(models.Carreras).filter(
                models.Carreras.id_carrera == id_carrera
        ).delete()
        db.commit()
        return True
    except Exception as error:
        print(error)
        return False

########################################################### CICLO ESCOLAR ############################

#Insertar
def insert_row_ciclo_escolar(db: Session, cicloUser: schemas.CicloEscolarBase):
    try:
        ciclo = models.CicloEscolar( 
        periodo= cicloUser.periodo,
        anio = cicloUser.anio,
        registro_grupos_inicio = cicloUser.registro_grupos_inicio,
        registro_grupos_termino = cicloUser.registro_grupos_termino, 
        registro_disponibilidad_inicio = cicloUser.registro_disponibilidad_inicio,
        registro_disponibilidad_termino = cicloUser.registro_disponibilidad_termino,
        registro_contrataciones_inicio =  cicloUser.registro_contrataciones_inicio,
        registro_contrataciones_termino = cicloUser.registro_contrataciones_termino,
        registro_horarios_secretaria_inicio = cicloUser.registro_horarios_secretaria_inicio,
        registro_horarios_secretaria_termino = cicloUser.registro_horarios_secretaria_termino,
        registro_aprobacion_coordi_docente_inicio = cicloUser.registro_aprobacion_coordi_docente_inicio,
        registro_aprobacion_coordi_docente_termino = cicloUser.registro_aprobacion_coordi_docente_termino)       
        db.add(ciclo)
        db.commit()
        db.refresh(ciclo)
        return True
    except Exception as error:       
        print(error)
        return False

def query_row_ciclo_escolar(db: Session, id_ciclo_escolar: int):
    try:
        ciclo_escolar = db.query(models.CicloEscolar.id_ciclo_escolar, models.CicloEscolar.periodo, models.CicloEscolar.anio, models.CicloEscolar.registro_grupos_inicio,
        models.CicloEscolar.registro_grupos_termino, models.CicloEscolar.registro_disponibilidad_inicio, models.CicloEscolar.registro_disponibilidad_termino,
        models.CicloEscolar.registro_contrataciones_inicio, models.CicloEscolar.registro_contrataciones_termino, models.CicloEscolar.registro_horarios_secretaria_inicio,
        models.CicloEscolar.registro_horarios_secretaria_termino, models.CicloEscolar.registro_aprobacion_coordi_docente_inicio,
        models.CicloEscolar.registro_aprobacion_coordi_docente_termino).filter(
            models.CicloEscolar.id_ciclo_escolar == id_ciclo_escolar
        ).first()
        if ciclo_escolar:
                return dict(ciclo_escolar)
        else:
                return None
    except Exception as error:
        print(error)
        return 

#Actualizar
def update_row_ciclo_escolar(db: Session, ciclo_escolar: schemas.CicloEscolarBase):
    try:
        db.query(models.CicloEscolar).filter(
                models.CicloEscolar.id_ciclo_escolar == ciclo_escolar.id_ciclo_escolar 
        ).update(
                {
                    models.CicloEscolar.periodo : ciclo_escolar.periodo,
                    models.CicloEscolar.anio : ciclo_escolar.anio,
                    models.CicloEscolar.registro_grupos_inicio : ciclo_escolar.registro_grupos_inicio,
                    models.CicloEscolar.registro_grupos_termino : ciclo_escolar.registro_grupos_termino,
                    models.CicloEscolar.registro_disponibilidad_inicio : ciclo_escolar.registro_disponibilidad_inicio,
                    models.CicloEscolar.registro_disponibilidad_termino : ciclo_escolar.registro_disponibilidad_termino,
                    models.CicloEscolar.registro_contrataciones_inicio : ciclo_escolar.registro_contrataciones_inicio,
                    models.CicloEscolar.registro_contrataciones_termino : ciclo_escolar.registro_contrataciones_termino,
                    models.CicloEscolar.registro_horarios_secretaria_inicio : ciclo_escolar.registro_horarios_secretaria_inicio,
                    models.CicloEscolar.registro_horarios_secretaria_termino : ciclo_escolar.registro_horarios_secretaria_termino,
                    models.CicloEscolar.registro_aprobacion_coordi_docente_inicio : ciclo_escolar.registro_aprobacion_coordi_docente_inicio,
                    models.CicloEscolar.registro_aprobacion_coordi_docente_termino : ciclo_escolar.registro_aprobacion_coordi_docente_termino,
                }
        )
        db.commit()
        return True
    except Exception as error:
        print(error)
        return False

#Eliminar
def delete_row_ciclo_escolar(db: Session, id_ciclo_escolar: int):
    try:
        db.query(models.CicloEscolar).filter(
                models.CicloEscolar.id_ciclo_escolar == id_ciclo_escolar
        ).delete()
        db.commit()
        return True
    except Exception as error:
        print(error)
        return False

########################################################### PLAN DE ESTUDIOS ############################

# INSERTAR
def insert_row_plan_estudios(db:Session, user_plan:schemas.PlanEstudiosBase):
        try:
            plan_estudios = models.PlanEstudios(nombre_materia = user_plan.nombre_materia, cuatrimestre = user_plan.cuatrimestre, total_horas = user_plan.total_horas,
            total_horas_semana = user_plan.total_horas_semana, carrera = user_plan.carrera)
            db.add(plan_estudios)
            db.commit()
            db.refresh(plan_estudios)
            return True
        except Exception as error:
            print(error)
            return False

#Consultar
def query_row_plan_estudios(db:Session, id_plan_estudios: int):
    try:
        plan_estudios = db.query(
        models.PlanEstudios.id_materia,
        models.PlanEstudios.nombre_materia, 
        models.PlanEstudios.cuatrimestre, 
        models.PlanEstudios.total_horas, 
        models.PlanEstudios.total_horas_semana, 
        models.PlanEstudios.carrera).filter(
            models.PlanEstudios.id_materia == id_plan_estudios
        ).first()
        if plan_estudios:
            return dict(plan_estudios)
        else:
            return None
    except Exception as error:
        print(error)
        return None

#Consultar N registros
def query_rows_plan_estudios(db: Session, carrera):
    plan_estudios_completo = db.query(
        models.PlanEstudios.id_materia,
        models.PlanEstudios.nombre_materia, 
        models.PlanEstudios.cuatrimestre, 
        models.PlanEstudios.total_horas, 
        models.PlanEstudios.total_horas_semana, 
        models.PlanEstudios.carrera
    ).filter(models.PlanEstudios.carrera == carrera).order_by(models.PlanEstudios.id_materia.asc())
    if plan_estudios_completo:
        return [dict(i) for i in plan_estudios_completo]
    else:
        return None

#Actualizar
def update_row_plan_estudios(db:Session, id_plan_estudios: schemas.PlanEstudiosBase):
    try:
        db.query(models.PlanEstudios).filter(
                models.PlanEstudios.id_materia == id_plan_estudios.id_materia 
        ).update(
                {
                    models.PlanEstudios.nombre_materia : id_plan_estudios.nombre_materia,
                    models.PlanEstudios.cuatrimestre : id_plan_estudios.cuatrimestre,
                    models.PlanEstudios.total_horas : id_plan_estudios.total_horas,
                    models.PlanEstudios.total_horas_semana : id_plan_estudios.total_horas_semana,
                    models.PlanEstudios.carrera : id_plan_estudios.carrera
                }
        )
        db.commit()
        return True
    except Exception as error:
        print(error)
        return False

#Eliminar
def delete_row_plan_estudios(db: Session, id_plan_estudios: int):
    try:
        db.query(models.PlanEstudios).filter(
                models.PlanEstudios.id_materia == id_plan_estudios
        ).delete()
        db.commit()
        return True
    except Exception as error:
        print(error)
        return False

########################################################### GRUPOS ###################################

#INSERTAR
def insert_row_grupos(db: Session, grupo_base: schemas.GruposBase):
    try:
        grupo = models.Grupo(cuatrimestre=grupo_base.cuatrimestre, no_grupo=grupo_base.no_grupo, 
        hora_entrada_minima= grupo_base.hora_entrada_minima, hora_salida_maxima= grupo_base.hora_salida_maxima, 
        ciclo_escolar= grupo_base.ciclo_escolar, carrera= grupo_base.carrera)
        db.add(grupo)
        db.commit()
        db.refresh(grupo)
        return True
    except Exception as error:
        print(error)
        return False

def query_rows_grupos(db: Session, ciclo_escolar : int, carrera: int):
    try:
        grupo = db.query(models.Grupo.id_grupo, models.Grupo.cuatrimestre, models.Grupo.no_grupo, 
        models.Grupo.hora_entrada_minima, models.Grupo.hora_salida_maxima,
        models.Grupo.ciclo_escolar, models.Grupo.carrera).filter(
            models.Grupo.ciclo_escolar == ciclo_escolar and models.Grupo.carrera == carrera
        ).order_by(models.Grupo.id_grupo.asc())
        if grupo:
            return [ dict(i) for i in grupo ]
        else:
            return None
    except Exception as error:
        print(error)
        return None

#Actualizar
def update_row_grupos(db: Session, grupo_base= schemas.GruposBase):
    try:
        db.query(models.Grupo).filter(
                models.Grupo.id_grupo == grupo_base.id_grupo 
        ).update(
                {
                    models.Grupo.cuatrimestre : grupo_base.cuatrimestre,
                    models.Grupo.no_grupo : grupo_base.no_grupo,
                    models.Grupo.hora_entrada_minima : grupo_base.hora_entrada_minima,
                    models.Grupo.hora_salida_maxima : grupo_base.hora_salida_maxima,
                    models.Grupo.ciclo_escolar : grupo_base.ciclo_escolar,
                    models.Grupo.carrera : grupo_base.carrera
                }
        )
        db.commit()
        return True
    except Exception as error:
        print(error)
        return 
        
#Eliminar
def delete_row_grupos(db: Session, id_grupo: int):
    try:
        db.query(models.Grupo).filter(
                models.Grupo.id_grupo == id_grupo
        ).delete()
        db.commit()
        return True
    except Exception as error:
        print(error)
        return False