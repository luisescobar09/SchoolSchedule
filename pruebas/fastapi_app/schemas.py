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

############################################### REGISTRO DOCENTE #######################################

class RegistroDocenteBase(BaseModel):
    id_registro_docente : Optional[int]
    nombre : str
    apellido_paterno : str
    apellido_materno : str
    email : str
    tipo_docente : int
    carrera : int

################################################## DISPONIBILIDAD DOCENTES #################################################

class DisponibilidadDocentesBase(BaseModel):
    id_disponibilidad  : Optional[int]
    id_ciclo_escolar : int
    id_docente : int
    lunes_entrada : Optional[time]
    lunes_salida: Optional[time] 
    martes_entrada : Optional[time]
    martes_salida : Optional[time]
    miercoles_entrada : Optional[time]
    miercoles_salida : Optional[time]
    jueves_entrada : Optional[time]
    jueves_salida : Optional[time]
    viernes_entrada : Optional[time]
    viernes_salida : Optional[time]
    sabado_entrada : Optional[time]
    sabado_salida : Optional[time]

################################################ CONTRATACIÓN DOCENTE ######################################################

class ContratacionDocenteBase(BaseModel):
    id_contratacion : Optional[int]
    id_ciclo_escolar : int
    id_docente : int
    id_grupo : int
    id_materia : int

################################################ HORARIOS ######################################################

class HorariosBase(BaseModel):
    id_horario : Optional[int]
    id_ciclo_escolar : int
    id_docente : int
    id_grupo : int
    id_materia : int
    dia_clases : int
    hora_entrada : int
    hora_salida : int