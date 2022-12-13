from sqlalchemy import Column, Integer, String, SmallInteger, Date, Time, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

#engine = create_engine("postgresql://postgres:12345678@localhost:5432/pruebas_horarios")

engine = create_engine("postgresql://postgres:26Ti9228twc8!d3@db.svhulthwokfuuwlasvul.supabase.co:5432/postgres")

'''class TipoUsuario(enum.Enum):
    administrador = 1
    secretario_academico = 2
    coordinador_academico = 3
    coordinador_idiomas = 4
    docente = 5'''

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


#################################################### DOCENTES  ########################################

class RegistroDocente(Base):
    __tablename__ ='docentes'
    id_docente = Column(Integer(), primary_key = True)
    nombre = Column(String(20), nullable = False)
    apellido_paterno = Column(String(15), nullable = False)
    apellido_materno = Column(String(15), nullable = False)
    email = Column(String(60), nullable = False, unique = True)
    tipo_docente = Column(String(1), nullable = False)
    carrera = Column(SmallInteger(), ForeignKey("carreras.id_carrera", ondelete="CASCADE"), nullable = False) ### FOREIGN KEY CARRERAS(ID)

#################################################### DISPONIBILIDAD DOCENTES ######################################################

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

################################################ CONTRATACIÓN DOCENTE ######################################################

class ContratacionDocente(Base):
    __tablename__ = 'contratacion_docente'
    id_contratacion = Column(Integer(), primary_key=True, nullable=False)
    id_ciclo_escolar = Column(Integer(), ForeignKey("ciclo_escolar.id_ciclo_escolar", ondelete="CASCADE"), nullable = False)
    id_docente = Column(Integer(), ForeignKey("docentes.id_docente", ondelete="CASCADE"), nullable = False)
    id_grupo = Column(Integer(), ForeignKey("grupos.id_grupo", ondelete="CASCADE"), nullable=False)
    id_materia = Column(Integer(), ForeignKey("plan_estudios.id_materia", ondelete="CASCADE"), nullable=False)

################################################ HORARIOS ######################################################

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


Session = sessionmaker(engine)
session = Session()

def insert_row_Usuarios(nombre_usuario, apellido_paterno, apellido_materno, email, tipo_usuario):
        try:
            user = Usuarios(nombre_usuario = nombre_usuario, apellido_paterno = apellido_paterno,
                apellido_materno = apellido_materno, email = email, tipo_usuario = tipo_usuario)
            session.add(user)
            session.commit()
            return True
        except Exception as error:
            print(error)
            return False

#Consultar
def query_row_Usuarios(email: str):
    try:
        user = session.query(Usuarios.id_usuario,Usuarios.nombre_usuario, Usuarios.apellido_paterno, Usuarios.apellido_materno, Usuarios.email, Usuarios.tipo_usuario).filter(
            Usuarios.email == email
        ).first()
        if user:
                return dict(user)
        else:
                return None
    except Exception as error:
        print(error)
        return None

#Eliminar
def delete_row_Usuarios(email: str):
    try:
        session.query(Usuarios).filter(
                Usuarios.email == email
        ).delete()
        session.commit()
        return True
    except Exception as error:
        print(error)
        return False


######################################################## CARRERAS #####################################

def insert_row_carreras(nombre_carrera : str, coordinador_carrera : int):
        try:
            carrera = Carreras(nombre_carrera = nombre_carrera, coordinador_carrera = coordinador_carrera)
            session.add(carrera)
            session.commit()
            return True
        except Exception as error:
            print(error)
            return False
#Consultar
def query_row_carreras(id_carrera: int):
    try:
        carrera = session.query(Carreras.id_carrera, Carreras.nombre_carrera, Usuarios.id_usuario, Usuarios.nombre_usuario, Usuarios.apellido_paterno, Usuarios.apellido_materno).join(
           Usuarios, Carreras.id_carrera == id_carrera
        ).first()
        if carrera:
                return dict(carrera)
        else:
                return None
    except Exception as error:
        print(error)
        return None
#Eliminar
def delete_row_carreras(id_carrera: int):
    try:
        session.query(Carreras).filter(
                Carreras.id_carrera == id_carrera
        ).delete()
        session.commit()
        return True
    except Exception as error:
        print(error)
        return False

################################################# PLANES DE ESTUDIOS

# INSERTAR
def insert_row_plan_estudios(nombre_materia : str, cuatrimestre : int, total_horas: int, total_horas_semana: int, carrera: int):
        try:
            plan_estudios = PlanEstudios(nombre_materia = nombre_materia, cuatrimestre = cuatrimestre, total_horas = total_horas,
            total_horas_semana = total_horas_semana, carrera = carrera)
            session.add(plan_estudios)
            session.commit()
            return True
        except Exception as error:
            print(error)
            return False

#Consultar
def query_row_plan_estudios(carrera: int):
    try:
        plan_estudios = session.query(PlanEstudios.id_materia, PlanEstudios.nombre_materia, PlanEstudios.cuatrimestre, 
        PlanEstudios.total_horas, PlanEstudios.total_horas_semana, PlanEstudios.carrera, Carreras.nombre_carrera).order_by(
            PlanEstudios.id_materia.asc()
        ).join(
           Carreras, PlanEstudios.carrera == carrera
        )
        if plan_estudios:
                return [ dict(i) for i in plan_estudios ]
        else:
                return None
    except Exception as error:
        print(error)
        return None


################################### GRUPOS
#INSERTAR
def insert_row_grupos(cuatrimestre, no_grupo, hora_entrada_minima, hora_salida_maxima, ciclo_escolar, carrera):
    try:
        grupo = Grupo(cuatrimestre=cuatrimestre, no_grupo=no_grupo, hora_entrada_minima=hora_entrada_minima,
        hora_salida_maxima=hora_salida_maxima, ciclo_escolar=ciclo_escolar, carrera=carrera)
        session.add(grupo)
        session.commit()
        session.refresh(grupo)
        return True
    except Exception as error:
        print(error)
        return False
def query_rows_grupos(ciclo_escolar, carrera):
    try:
        grupo = session.query(Grupo.id_grupo, Grupo.cuatrimestre, Grupo.no_grupo, Grupo.hora_entrada_minima, Grupo.hora_salida_maxima,
        Grupo.ciclo_escolar, Grupo.carrera).filter(
            Grupo.ciclo_escolar == ciclo_escolar and Grupo.cuatrimestre == carrera
        ).order_by(Grupo.id_grupo.asc()).all()
        if grupo:
                return [ dict(i) for i in grupo ]
        else:
                return None

    except Exception as error:
        print(error)
        return None
#Actualizar
def update_row_grupos(id_grupo, cuatrimestre, no_grupo, hora_entrada_minima, hora_salida_maxima, ciclo_escolar, carrera):
    try:
        session.query(Grupo).filter(
                Grupo.id_grupo == id_grupo 
        ).update(
                {
                    Grupo.cuatrimestre : cuatrimestre,
                    Grupo.no_grupo : no_grupo,
                    Grupo.hora_entrada_minima : hora_entrada_minima,
                    Grupo.hora_salida_maxima : hora_salida_maxima,
                    Grupo.ciclo_escolar : ciclo_escolar,
                    Grupo.carrera : carrera
                }
        )
        session.commit()
        return True
    except Exception as error:
        print(error)
        return False

#Eliminar
def delete_row_Usuarios(id_grupo: int):
    try:
        session.query(Grupo).filter(
                Grupo.id_grupo == id_grupo
        ).delete()
        session.commit()
        return True
    except Exception as error:
        print(error)
        return False

def insert_row_ciclo_escolar(periodo, anio, registro_grupos_inicio, registro_grupos_termino, registro_disponibilidad_inicio,
registro_disponibilidad_termino, registro_contrataciones_inicio, registro_contrataciones_termino, registro_horarios_secretaria_inicio,
registro_horarios_secretaria_termino, registro_aprobacion_coordi_docente_inicio, registro_aprobacion_coordi_docente_termino):
    try:
        ciclo_escolar = CicloEscolar(periodo = periodo, anio = anio, registro_grupos_inicio = registro_grupos_inicio, 
        registro_grupos_termino = registro_grupos_termino, registro_disponibilidad_inicio = registro_disponibilidad_inicio, 
        registro_disponibilidad_termino = registro_disponibilidad_termino, registro_contrataciones_inicio = registro_contrataciones_inicio, 
        registro_contrataciones_termino = registro_contrataciones_termino, registro_horarios_secretaria_inicio = registro_horarios_secretaria_inicio, 
        registro_horarios_secretaria_termino = registro_horarios_secretaria_termino, registro_aprobacion_coordi_docente_inicio = registro_aprobacion_coordi_docente_inicio, 
        registro_aprobacion_coordi_docente_termino = registro_aprobacion_coordi_docente_termino)
        session.add(ciclo_escolar)
        session.commit()
        return True
    except Exception as error:
        print(error)
        return False

#Consultar
def query_row_ciclo_escolar(id_ciclo_escolar: int):
    try:
        ciclo_escolar = session.query(CicloEscolar.id_ciclo_escolar, CicloEscolar.periodo, CicloEscolar.anio, CicloEscolar.registro_grupos_inicio,
        CicloEscolar.registro_grupos_termino, CicloEscolar.registro_disponibilidad_inicio, CicloEscolar.registro_disponibilidad_termino,
        CicloEscolar.registro_contrataciones_inicio, CicloEscolar.registro_contrataciones_termino, CicloEscolar.registro_horarios_secretaria_inicio,
        CicloEscolar.registro_horarios_secretaria_termino, CicloEscolar.registro_aprobacion_coordi_docente_inicio,
        CicloEscolar.registro_aprobacion_coordi_docente_termino).filter(
            CicloEscolar.id_ciclo_escolar == id_ciclo_escolar
        ).first()
        if ciclo_escolar:
                return dict(ciclo_escolar)
        else:
                return None
    except Exception as error:
        print(error)
        return None

#Eliminar
def delete_row_ciclo_escolar(id_ciclo_escolar: int):
    try:
        session.query(CicloEscolar).filter(
                CicloEscolar.id_ciclo_escolar == id_ciclo_escolar
        ).delete()
        session.commit()
        return True
    except Exception as error:
        print(error)
        return False


if __name__=='__main__':
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    print("Insertar Usuario:",insert_row_Usuarios(nombre_usuario="José Luis", apellido_paterno="Escobar", apellido_materno="Pérez", email="1719110043@utectulancingo.edu.mx", tipo_usuario="1"))
    print(query_row_Usuarios(email="1719110043@utectulancingo.edu.mx"))
    print("Insertar carrera:",insert_row_carreras(nombre_carrera = "Ingeniería en Desarrollo y Gestión de Software", coordinador_carrera = 1))
    #print(query_row_carreras(id_carrera = 1))
    print("Insertar materias:")
    print(insert_row_plan_estudios(nombre_materia = 'Programación I.', cuatrimestre = 1, total_horas = 200, total_horas_semana = 5, carrera = 1))
    print(insert_row_plan_estudios(nombre_materia = 'Bases de Datos I.', cuatrimestre = 2, total_horas = 250, total_horas_semana = 6, carrera = 1))
    print(insert_row_plan_estudios(nombre_materia = 'Desarrollo Web', cuatrimestre = 3, total_horas = 300, total_horas_semana = 7, carrera = 1))
    print(query_row_plan_estudios(carrera = 1))

    print("Insertar ciclo escolar", insert_row_ciclo_escolar(periodo = '3', anio = 2022, registro_grupos_inicio = '2022-10-02', registro_grupos_termino = '2022-10-09', registro_disponibilidad_inicio = '2022-10-10',
    registro_disponibilidad_termino = '2022-10-16', registro_contrataciones_inicio = '2022-10-17', registro_contrataciones_termino = '2022-10-23', registro_horarios_secretaria_inicio = '2022-10-24',
    registro_horarios_secretaria_termino = '2022-10-30', registro_aprobacion_coordi_docente_inicio = '2022-10-31', registro_aprobacion_coordi_docente_termino = '2022-11-06'))
    print(query_row_ciclo_escolar(id_ciclo_escolar=1))
    print("Insertar grupo:", insert_row_grupos(
        cuatrimestre= 1, no_grupo=1, hora_entrada_minima='07:00', hora_salida_maxima='14:00',
        ciclo_escolar= 1, carrera= 1
    ))
    print("Insertar grupo:", insert_row_grupos(
        cuatrimestre= 4, no_grupo=2, hora_entrada_minima='07:00', hora_salida_maxima='14:00',
        ciclo_escolar= 1, carrera= 1
    ))
    print("Insertar grupo:", insert_row_grupos(
        cuatrimestre= 9, no_grupo=1, hora_entrada_minima='14:00', hora_salida_maxima='21:00',
        ciclo_escolar= 1, carrera= 1
    ))
    print(query_rows_grupos(ciclo_escolar=1, carrera=1))

    '''if delete_row_Usuarios(email="1719110043@utectulancingo.edu.mx") is True:
        print("Usuario eliminado correctamente")
    else:
        print("No lo hizo")'''
    '''if delete_row_carreras(id_carrera= 1) is True:
        print("Carrera eliminada correctamente")
    else:
        print("No lo hizo")'''
    '''if delete_row_ciclo_escolar(id_ciclo_escolar=1) is True:
        print("Ciclo escolar eliminado correctamente")
    else:
        print("No lo hizo")'''