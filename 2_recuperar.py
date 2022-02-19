from src.modelo.models import Cancion
from src.modelo.models import Interprete
from src.modelo.models import Album, Medio
from src.modelo.declarative_base import Session, engine, Base


if __name__ == '__main__':
    #Abre la Session
    session = Session()
    canciones = session.query(Cancion).all()

    print('Las canciones almacenadas son:')
    for cancion in canciones:
        # Titulo: Ajiaco (00:3:1)
        if (len(str(cancion.minutos)) == 1):
            minutes = "0" + str(cancion.minutos)
        else:
            minutes = str(cancion.minutos)
        #print("Titulo: " + cancion.titulo + " (00:" + str(cancion.minutos) + ":" +str(cancion.segundos) + ")")
        print("Titulo: " + cancion.titulo + " (00:" + minutes + ":" +str(cancion.segundos) + ")")

        print("Intérpretes")
        for interprete in cancion.interpretes:
            print(" - " + interprete.nombre)

        for album in cancion.albumes:
            print(" -- Presente en el album: " + album.titulo)

        print("")


    print('Los álbumes almacenados en discos son:')
    albumes = session.query(Album).filter(Album.medio == Medio.DISCO).all()
    for album in albumes:
        print("Album: " + album.titulo)

    session.close()