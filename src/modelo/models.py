import enum
from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from .declarative_base import Base

#Clase Interprete
class Interprete(Base):
    __tablename__ = 'interprete'

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    texto_curiosidades = Column(String)
    cancion = Column(Integer, ForeignKey('cancion.id'))


#Clase Album
class Medio(enum.Enum):
    DISCO = 1
    CASETE = 2
    CD = 3


class Album(Base):
    __tablename__ = 'album'

    id = Column(Integer, primary_key=True)
    titulo = Column(String)
    ano = Column(Integer)
    descripcion = Column(String)
    medio = Column(Enum(Medio))
    canciones = relationship('Cancion', secondary='album_cancion', back_populates="albumes")

#Clase Cancion
class Cancion(Base):
    __tablename__ = 'cancion'

    id = Column(Integer, primary_key=True)
    titulo = Column(String)
    minutos = Column(Integer)
    segundos = Column(Integer)
    compositor = Column(String)
    albumes = relationship('Album', secondary='album_cancion', back_populates="canciones")
    interpretes = relationship('Interprete', cascade='all, delete, delete-orphan')

    def print_values(self):
        print("Titulo: " + self.titulo + " (00:" + str(self.minutos) + ":" +str(self.segundos) + ") Compositor: " + self.compositor)
        print("Interpretes:")
        for interprete in self.interpretes:
            print(" - " + interprete.nombre)

#Clase AlbumCancion
class AlbumCancion(Base):
    __tablename__ = 'album_cancion'

    cancion_id = Column(Integer,ForeignKey('cancion.id'),primary_key=True)
    album_id = Column(Integer,ForeignKey('album.id'),primary_key=True)
