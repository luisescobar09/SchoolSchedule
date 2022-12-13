from sqlalchemy import Column, Integer, String, SmallInteger, Date, ForeignKey, Time
from .database import Base

class Usuarios(Base):
    __tablename__ = 'usuarios'

    id_usuario = Column(Integer(), primary_key = True)
    nombre_usuario = Column(String(20), nullable = False)
    apellido_paterno = Column(String(15), nullable = False)
    apellido_materno = Column(String(15), nullable = False)
    email = Column(String(60), nullable = False, unique = True)
    tipo_usuario = Column(String(5), nullable = False)

class Carreras(Base):
    __tablename__ = 'carreras'

    id_carrera = Column(Integer(), primary_key = True)
    nombre_carrera = Column(String(60), nullable = False)
    coordinador_carrera = Column(Integer(), ForeignKey("usuarios.id_usuario", ondelete="CASCADE"), nullable = False) ### FOREIGN KEY USUARIOS(ID)

class PlanEstudios(Base):
    __tablename__ = 'plan_estudios'

    id_materia = Column(Integer(), primary_key = True)
    nombre_materia = Column(String(60), nullable = False)
    cuatrimestre = Column(SmallInteger(), nullable = False)
    total_horas = Column(SmallInteger(), nullable = False)
    total_horas_semana = Column(SmallInteger(), nullable = False)
    carrera = Column(SmallInteger(), ForeignKey("carreras.id_carrera", ondelete="CASCADE"), nullable = False) ### FOREIGN KEY CARRERAS(ID)

class CicloEscolar(Base):
    __tablename__ = 'ciclo_escolar'

    id_ciclo_escolar = Column(Integer(), primary_key = True)
    periodo = Column(String(1), nullable = False)
    anio = Column(SmallInteger())
    registro_grupos_inicio = Column(Date(), nullable = False)
    registro_grupos_termino = Column(Date(), nullable = False)
    registro_disponibilidad_inicio = Column(Date(), nullable = False)
    registro_disponibilidad_termino = Column(Date(), nullable = False)
    registro_contrataciones_inicio = Column(Date(), nullable = False)
    registro_contrataciones_termino = Column(Date(), nullable = False)
    registro_horarios_secretaria_inicio = Column(Date(), nullable = False)
    registro_horarios_secretaria_termino = Column(Date(), nullable = False)
    registro_aprobacion_coordi_docente_inicio = Column(Date(), nullable = False)
    registro_aprobacion_coordi_docente_termino = Column(Date(), nullable = False)

class Grupo(Base):
    __tablename__ = 'grupos'

    id_grupo = Column(Integer(), primary_key = True)
    cuatrimestre = Column(Integer(), nullable = False)
    no_grupo = Column(SmallInteger(), nullable = False)
    hora_entrada_minima = Column(Time(), nullable = False)
    hora_salida_maxima = Column(Time(), nullable = False)
    ciclo_escolar = Column(Integer(), ForeignKey("ciclo_escolar.id_ciclo_escolar", ondelete="CASCADE"), nullable = False) # FOREIGN KEY CiCLOESCOLAR(ID)
    carrera = Column(SmallInteger(), ForeignKey("carreras.id_carrera", ondelete="CASCADE"), nullable = False) ### FOREIGN KEY CARRERAS(ID)

class RegistroDocente(Base):
    __tablename__ ='docentes'

    id_docente = Column(Integer(), primary_key = True)
    nombre = Column(String(20), nullable = False)
    apellido_paterno = Column(String(15), nullable = False)
    apellido_materno = Column(String(15), nullable = False)
    email = Column(String(60), nullable = False, unique = True)
    tipo_docente = Column(String(1), nullable = False)
    carrera = Column(SmallInteger(), ForeignKey("carreras.id_carrera", ondelete="CASCADE"), nullable = False) ### FOREIGN KEY CARRERAS(ID)

class DisponibilidadDocentes(Base):
    __tablename__='disponibilidad_docentes'

    id_disponibilidad = Column(Integer(), primary_key = True, nullable = False)
    id_ciclo_escolar = Column(Integer(), ForeignKey("ciclo_escolar.id_ciclo_escolar", ondelete="CASCADE"), nullable = False)
    id_docente = Column(Integer(), ForeignKey("docentes.id_docente", ondelete="CASCADE"), nullable = False)
    lunes_entrada = Column(Time(), nullable = True)
    lunes_salida = Column(Time(), nullable = True)
    martes_entrada = Column(Time(), nullable = True)
    martes_salida = Column(Time(), nullable = True)
    miercoles_entrada = Column(Time(), nullable = True)
    miercoles_salida = Column(Time(), nullable = True)
    jueves_entrada = Column(Time(), nullable = True)
    jueves_salida = Column(Time(), nullable = True)
    viernes_entrada = Column(Time(), nullable = True)
    viernes_salida = Column(Time(), nullable = True)
    sabado_entrada = Column(Time(), nullable = True)
    sabado_salida = Column(Time(), nullable = True)

class ContratacionDocente(Base):
    __tablename__ = 'contratacion_docente'

    id_contratacion = Column(Integer(), primary_key=True, nullable=False)
    id_ciclo_escolar = Column(Integer(), ForeignKey("ciclo_escolar.id_ciclo_escolar", ondelete="CASCADE"), nullable = False)
    id_docente = Column(Integer(), ForeignKey("docentes.id_docente", ondelete="CASCADE"), nullable = False)
    id_grupo = Column(Integer(), ForeignKey("grupos.id_grupo", ondelete="CASCADE"), nullable=False)
    id_materia = Column(Integer(), ForeignKey("plan_estudios.id_materia", ondelete="CASCADE"), nullable=False)

class Horarios(Base):
    __tablename__ = 'horarios'

    id_horario = Column(Integer(), primary_key=True, nullable=False)
    id_ciclo_escolar = Column(Integer(), ForeignKey("ciclo_escolar.id_ciclo_escolar", ondelete="CASCADE"), nullable = False)
    id_docente = Column(Integer(), ForeignKey("docentes.id_docente", ondelete="CASCADE"), nullable = False)
    id_grupo = Column(Integer(), ForeignKey("grupos.id_grupo", ondelete="CASCADE"), nullable=False)
    id_materia = Column(Integer(), ForeignKey("plan_estudios.id_materia", ondelete="CASCADE"), nullable=False)
    dia_clases = Column(SmallInteger(), nullable = False)
    hora_entrada = Column(Time(), nullable = True)
    hora_salida = Column(Time(), nullable = True)