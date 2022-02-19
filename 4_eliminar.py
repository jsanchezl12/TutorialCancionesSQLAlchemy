from src.modelo.models import Cancion
from src.modelo.models import Interprete
from src.modelo.models import Album, Medio
from src.modelo.declarative_base import Session, engine, Base


def fn_delete_all(type, session, list):
    if (type == "Cancion"):
        for cancion in list:
            session.delete(cancion)
        print("Canciones Eliminadas")
    elif(type == "Album"):
        for album in list:
            session.delete(album)
        print("Albumes Eliminados")
    elif(type == "Interprete"):
        for interprete in list:
            session.delete(interprete)
        print("Interpretes Eliminados")
    else:
        print("Tipo de dato no reconocido")            


if __name__ == '__main__':
    session = Session()
    
    #cancion2 = session.query(Cancion).get(2)
    #session.delete(cancion2)

    #DELETE ALL
    delete_all = 1
    canciones = session.query(Cancion).all()
    interpretes = session.query(Interprete).all()
    albumes = session.query(Album).all()
    if delete_all == 1:
        fn_delete_all("Cancion", session, canciones)
        fn_delete_all("Interprete", session, interpretes)
        fn_delete_all("Album", session, albumes)
    else:
        print("No se eliminaran datos porque la bandera de delete_all esta con 0")


    session.commit()
    session.close()