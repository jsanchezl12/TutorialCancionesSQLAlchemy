from src.modelo.models import Cancion
from src.modelo.models import Interprete
from src.modelo.declarative_base import Session, engine, Base


if __name__ == '__main__':
    #Abre la Session
    session = Session()
    cancion = session.query(Cancion).get(2)
    #interpretes = session.query(Interprete).all()
    interprete = session.query(Interprete).get(4)
    # for interprete in interpretes:
    #     print( interprete.nombre + " | " + str(interprete.texto_curiosidades) + " | " + str(interprete.cancion))
    #     cancion = session.query(Cancion).get(interprete.cancion)
    #     print(cancion.titulo)

    cancion.minutos = 5
    cancion.segundos = 30
    cancion.compositor = "Pedro Pérez"
    cancion.interpretes.append(interprete)
    print(Cancion.print_values(cancion))
    
    session.add(cancion)
    session.commit()
    session.close()