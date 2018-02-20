# app/models.py

from app import db
from datetime import datetime
from sqlalchemy.dialects.postgresql import JSONB, BYTEA, FLOAT


class Country(db.Model):
    __tablename__ = 'countries'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    codigo = db.Column(db.String(50), nullable=False)
    codigo_telefonico = db.Column(db.String(50), nullable=False)
    his_estados = db.Column(JSONB, nullable=True)
    eliminado = db.Column(db.Boolean, default=False)
    fecha_creacion = db.Column(db.DateTime, default=datetime.now())
    fecha_actualizacion = db.Column(db.DateTime, default=datetime.now())


class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    codigo = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(100), nullable=False)
    icono = db.Column(db.String(100), nullable=False)
    data = db.Column(JSONB, nullable=True)
    his_estados = db.Column(JSONB, nullable=True)
    eliminado = db.Column(db.Boolean, default=False)
    fecha_creacion = db.Column(db.DateTime, default=datetime.now())
    fecha_actualizacion = db.Column(db.DateTime, default=datetime.now())


class City(db.Model):
    __tablename__ = 'cities'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    his_estados = db.Column(JSONB, nullable=True)
    eliminado = db.Column(db.Boolean, default=False)
    fecha_creacion = db.Column(db.DateTime, default=datetime.now())
    fecha_actualizacion = db.Column(db.DateTime, default=datetime.now())

    pais_id = db.Column(db.Integer, db.ForeignKey('countries.id'))
    pais = db.relationship("Country", foreign_keys=[pais_id])


class User(db.Model):

    ACTIVO = "A"
    INACTIVO = "I"
    FREELANCE = "FR"
    CLIENTE = "CL"

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(20), nullable=False)
    nombres = db.Column(db.String(50), nullable=False)
    apellidos = db.Column(db.String(50), nullable=False)
    correo = db.Column(db.String(30), nullable=False)
    clave = db.Column(db.String(200), nullable=False)
    foto = db.Column(BYTEA, nullable=True)
    tipo_usuario = db.Column(db.String(30), nullable=False)
    razon_social = db.Column(db.String(200), nullable=False)
    telefono = db.Column(db.String(200), nullable=False)
    direccion = db.Column(db.String(200), nullable=False)
    estado = db.Column(db.String(200), nullable=False, default=ACTIVO)
    requerimientos = db.Column(JSONB, nullable=True)
    usuarios_favoritos = db.Column(JSONB, nullable=True)
    descripcion = db.Column(db.Text, nullable=True)
    historial_laboral = db.Column(db.Text, nullable=True)
    idiomas = db.Column(JSONB, nullable=True)
    costo_hora = db.Column(FLOAT, nullable=True)
    his_estados = db.Column(JSONB, nullable=True)
    eliminado = db.Column(db.Boolean, default=False)
    fecha_creacion = db.Column(db.DateTime, default=datetime.now())
    fecha_actualizacion = db.Column(db.DateTime, default=datetime.now())

    pais_id = db.Column(db.Integer, db.ForeignKey('countries.id'))
    pais = db.relationship("Country", foreign_keys=[pais_id])
    ciudad_id = db.Column(db.Integer, db.ForeignKey('cities.id'))
    ciudad = db.relationship("City", foreign_keys=[ciudad_id])
    categoria_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    categoria = db.relationship("Category", foreign_keys=[categoria_id])
