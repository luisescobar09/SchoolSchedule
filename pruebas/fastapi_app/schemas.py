"""coding=utf-8."""
 
from datetime import date, time
from typing import Optional
from pydantic import BaseModel


################################################### USUARIOS ########################################
class UserBase(BaseModel):
    id_usuario : Optional[int]
    nombre_usuario : str
    apellido_paterno : str
    apellido_materno : str
    email : str
    tipo_usuario : str


#################################################### CARRERAS  ########################################
class CarrerasBase(BaseModel):
    id_carrera : Optional[int]
    nombre_carrera : str
    coordinador_carrera : int
class CarrerasResponseBase(BaseModel):
    id_carrera : int
    nombre_carrera : str
    id_usuario : int
    nombre_usuario : str
    apellido_paterno : str
    apellido_materno : str


################################################ CICLO ESCOLAR  ########################################
class CicloEscolarBase(BaseModel):
    id_ciclo_escolar : Optional[int]
    periodo : str
    anio : int
    registro_grupos_inicio : date
    registro_grupos_termino : date
    registro_disponibilidad_inicio : date
    registro_disponibilidad_termino : date
    registro_contrataciones_inicio : date
    registro_contrataciones_termino : date
    registro_horarios_secretaria_inicio : date
    registro_horarios_secretaria_termino : date
    registro_aprobacion_coordi_docente_inicio : date
    registro_aprobacion_coordi_docente_termino : date


############################################### PLAN ESTUDIOS  ########################################
class PlanEstudiosBase(BaseModel):
    id_materia : Optional[int]
    nombre_materia : str
    cuatrimestre : int
    total_horas : int
    total_horas_semana : int
    carrera : int

#################################################### GRUPOS  ##########################################

class GruposBase(BaseModel):
    id_grupo : Optional[int]
    cuatrimestre : int
    no_grupo : int
    hora_entrada_minima : time
    hora_salida_maxima : time
    ciclo_escolar : int
    carrera : int