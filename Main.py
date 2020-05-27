import arcade
import Jugador
import os
import HUD
import Enemigos
import math
import random

# --- Constantes ---

# SPRITE_SCALING_BOX = 0.5
# SPRITE_SCALING_PLAYER = 0.5

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 900
Velocidad_Disparo_Enemigos = 8


class Room:
    """
    This class holds all the information about the
    different rooms.
    """

    def __init__(self):
        # Todas las listas de las habitaciones
        self.wall_list = None
        self.background = None
        self.enemigos_list = None
        self.balas_list = None
        self.recargas_list = None


def setup_room_p1():
    """Crea y devuelve la habitacion prision 1"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "PRISION6.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "CAJAS Y OBJETOS")
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "PRISION6.png")

    esqueleto1 = Enemigos.Skeleton()
    esqueleto1.center_y = 300
    esqueleto1.center_x = 700
    room.enemigos_list.append(esqueleto1)

    # Definir muros
    room.wall_list = obstaculos
    return room


def setup_room_p2():
    """Crea y devuelve la habitacion prision 2"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "PRISION2.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "ROCAS Y CAJAS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "PRISION2.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_p3():
    """Crea y devuelve la habitacion prision 3"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "PRISION9.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "CAJAS Y ROCAS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "PRISION9.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_p4():
    """Crea y devuelve la habitacion prision 4"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "PRISION4.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "CAJAS Y ROCAS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "PRISION4.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_p5():
    """Crea y devuelve la habitacion prision 5"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "PRISION8.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "CAJAS Y ROCAS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "PRISION8.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_p6():
    """Crea y devuelve la habitacion prision 6"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "PRISION7.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "CAJAS Y ROCAS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "PRISION7.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_p7():
    """Crea y devuelve la habitacion prision 7
    Cambio de piso a las ruinas"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "PRISION1.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "ROCAS Y CAJAS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "PRISION1.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_r1():
    """Crea y devuelve la habitacion ruinas 1"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "RUINAS11.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "ROCAS Y CAJAS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "RUINAS11.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_r2():
    """Crea y devuelve la habitacion ruinas 2"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "RUINAS1.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "CAJAS Y ROCAS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "RUINAS1.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_r3():
    """Crea y devuelve la habitacion ruinas 3"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "RUINAS9.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "ROCAS Y CAJAS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "RUINAS9.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_r4():
    """Crea y devuelve la habitacion ruinas 4"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "RUINAS15.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "CAJAS Y ROCAS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "RUINAS15.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_r5():
    """Crea y devuelve la habitacion ruinas 5"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "RUINAS1.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "CAJAS Y ROCAS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "RUINAS1.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_r6():
    """Crea y devuelve la habitacion ruinas 6"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "RUINAS12.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "ROCAS Y CAJAS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "RUINAS12.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_r7():
    """Crea y devuelve la habitacion ruinas 7"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "RUINAS2.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "CAJAS Y ROCAS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "RUINAS2.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_r8():
    """Crea y devuelve la habitacion ruinas 8
    Cambio de piso al laboratorio"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "RUINAS13.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "ROCAS Y CAJAS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "RUINAS13.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_r9():
    """Crea y devuelve la habitacion ruinas 9"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "RUINAS14.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "ROCAS Y CAJAS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "RUINAS14.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_r10():
    """Crea y devuelve la habitacion ruinas 10"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "RUINAS4.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "CAJAS Y ROCAS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "RUINAS4.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_r11():
    """Crea y devuelve la habitacion ruinas 11"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "RUINAS2.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "CAJAS Y ROCAS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "RUINAS2.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_r12():
    """Crea y devuelve la habitacion ruinas 12"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "RUINAS9.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "ROCAS Y CAJAS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "RUINAS9.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_r13():
    """Crea y devuelve la habitacion ruinas 13"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "RUINAS5.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "CAJAS Y ROCAS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "RUINAS5.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_r14():
    """Crea y devuelve la habitacion ruinas 14"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "RUINAS14.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "ROCAS Y CAJAS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "RUINAS14.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_r15():
    """Crea y devuelve la habitacion ruinas 15"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "RUINAS4.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "CAJAS Y ROCAS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "RUINAS4.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l1():
    """Crea y devuelve la habitacion ruinas 15"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB10M.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB10.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l2():
    """Crea y devuelve la habitacion ruinas 15"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB6.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB6.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l3():
    """Crea y devuelve la habitacion ruinas 15"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB6.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB6.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l4():
    """Crea y devuelve la habitacion ruinas 15"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB14M.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB14.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l5():
    """Crea y devuelve la habitacion ruinas 15"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB5.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB5.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l6():
    """Crea y devuelve la habitacion ruinas 15"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB5.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB5.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l7():
    """Crea y devuelve la habitacion ruinas 15"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB9.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB9.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l8():
    """Crea y devuelve la habitacion ruinas 15"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB5.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB5.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l9():
    """Crea y devuelve la habitacion ruinas 15"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB9M.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB9.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l10():
    """Crea y devuelve la habitacion ruinas 15"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB6.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB6.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l11():
    """Crea y devuelve la habitacion ruinas 15"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB6M.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB6.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l12():
    """Crea y devuelve la habitacion ruinas 15"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB12M.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB12.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l13():
    """Crea y devuelve la habitacion ruinas 15"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB5.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB5.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l14():
    """Crea y devuelve la habitacion ruinas 15"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB5.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB5.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l15():
    """Crea y devuelve la habitacion ruinas 15"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB6.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB6.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l16():
    """Crea y devuelve la habitacion ruinas 15"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB10M.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB10.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l17():
    """Crea y devuelve la habitacion ruinas 15"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB13.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB13.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l18():
    """Crea y devuelve la habitacion ruinas 15"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB6.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB6.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l19():
    """Crea y devuelve la habitacion ruinas 15"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB12M.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB12.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l20():
    """Crea y devuelve la habitacion ruinas 15"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB5.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB5.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l21():
    """Crea y devuelve la habitacion ruinas 15"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB11M.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB11.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l22():
    """Crea y devuelve la habitacion ruinas 15"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB6M.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB6.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l23():
    """Crea y devuelve la habitacion ruinas 15"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB9M.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB9.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l24():
    """Crea y devuelve la habitacion ruinas 15"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB5M.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB5.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l25():
    """Crea y devuelve la habitacion ruinas 15"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB11.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB11.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l26():
    """Crea y devuelve la habitacion ruinas 15"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB7M.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB7.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l27():
    """Crea y devuelve la habitacion ruinas 15"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB14M.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB14.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l28():
    """Crea y devuelve la habitacion ruinas 15"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB5M.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB5.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l29():
    """Crea y devuelve la habitacion ruinas 15"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB15M.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB15.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l30():
    """Crea y devuelve la habitacion ruinas 15"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB5.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB5.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l31():
    """Crea y devuelve la habitacion ruinas 15"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB11M.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB11.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l32():
    """Crea y devuelve la habitacion ruinas 15"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB6M.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB6.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l33():
    """Crea y devuelve la habitacion ruinas 15"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB3.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB3.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l34():
    """Crea y devuelve la habitacion ruinas 15"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB6.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB6.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l35():
    """Crea y devuelve la habitacion ruinas 15"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB14M.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB14.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l36():
    """Crea y devuelve la habitacion ruinas 15"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB5M.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB5.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l37():
    """Crea y devuelve la habitacion ruinas 15"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB13.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB13.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l38():
    """Crea y devuelve la habitacion ruinas 15"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB6M.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB6.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l39():
    """Crea y devuelve la habitacion ruinas 15"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB6M.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB6.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l40():
    """Crea y devuelve la habitacion ruinas 15"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB6M.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB6.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l41():
    """Crea y devuelve la habitacion ruinas 15"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB6.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB6.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l42():
    """Crea y devuelve la habitacion ruinas 15"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB12M.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB12.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l43():
    """Crea y devuelve la habitacion ruinas 15"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB5M.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB5.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l44():
    """Crea y devuelve la habitacion ruinas 15"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB5M.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB5.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l45():
    """Crea y devuelve la habitacion ruinas 15"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB11M.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB11.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l46():
    """Crea y devuelve la habitacion ruinas 15"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB4.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB4.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


class SteamPunkGame(arcade.Window):
    """ Ventana principal del juego """

    def __init__(self):
        """ Constructor """
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Juego")  # Poner nombre del juego
        # Sprite lists
        self.player_list = None
        self.bullet_list = None
        # Habitacion
        self.current_room = 0
        self.rooms = None
        # Set up the player
        self.jugador = None
        self.physics_engine = None
        self.velocidad_jugador = 4
        self.vida_jugador = 10
        self.carga_fantasmal_jugador = 100
        # Atributos para el disparo del jugador
        self.velocidad_disparo = 10
        # Atributos para el manejo del comienzo del juego
        self.empezado = False
        self.mirando_controles = False
        # Pausar el juego
        self.pausado = False

        self.frame_count = 0

    def setup(self):
        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        # Create the player
        self.jugador = Jugador.Jugador()  # OJO!
        self.jugador.center_x = 350
        self.jugador.center_y = 350
        self.player_list.append(self.jugador)

        # Rooms
        self.rooms = []  # lista de todas las habitaciones

        # Prision:
        room = setup_room_p1()
        self.rooms.append(room)
        room = setup_room_p2()
        self.rooms.append(room)
        room = setup_room_p3()
        self.rooms.append(room)
        room = setup_room_p4()
        self.rooms.append(room)
        room = setup_room_p5()
        self.rooms.append(room)
        room = setup_room_p6()
        self.rooms.append(room)
        room = setup_room_p7()
        self.rooms.append(room)
        # Ruinas:
        room = setup_room_r1()
        self.rooms.append(room)
        room = setup_room_r2()
        self.rooms.append(room)
        room = setup_room_r3()
        self.rooms.append(room)
        room = setup_room_r4()
        self.rooms.append(room)
        room = setup_room_r5()
        self.rooms.append(room)
        room = setup_room_r6()
        self.rooms.append(room)
        room = setup_room_r7()
        self.rooms.append(room)
        room = setup_room_r8()
        self.rooms.append(room)
        room = setup_room_r9()
        self.rooms.append(room)
        room = setup_room_r10()
        self.rooms.append(room)
        room = setup_room_r11()
        self.rooms.append(room)
        room = setup_room_r12()
        self.rooms.append(room)
        room = setup_room_r13()
        self.rooms.append(room)
        room = setup_room_r14()
        self.rooms.append(room)
        room = setup_room_r15()
        self.rooms.append(room)
        # Laboratorio
        room = setup_room_l1()
        self.rooms.append(room)
        room = setup_room_l2()
        self.rooms.append(room)
        room = setup_room_l3()
        self.rooms.append(room)
        room = setup_room_l4()
        self.rooms.append(room)
        room = setup_room_l5()
        self.rooms.append(room)
        room = setup_room_l6()
        self.rooms.append(room)
        room = setup_room_l7()
        self.rooms.append(room)
        room = setup_room_l8()
        self.rooms.append(room)
        room = setup_room_l9()
        self.rooms.append(room)
        room = setup_room_l10()
        self.rooms.append(room)
        room = setup_room_l11()
        self.rooms.append(room)
        room = setup_room_l12()
        self.rooms.append(room)
        room = setup_room_l13()
        self.rooms.append(room)
        room = setup_room_l14()
        self.rooms.append(room)
        room = setup_room_l15()
        self.rooms.append(room)
        room = setup_room_l16()
        self.rooms.append(room)
        room = setup_room_l17()
        self.rooms.append(room)
        room = setup_room_l18()
        self.rooms.append(room)
        room = setup_room_l19()
        self.rooms.append(room)
        room = setup_room_l20()
        self.rooms.append(room)
        room = setup_room_l21()
        self.rooms.append(room)
        room = setup_room_l22()
        self.rooms.append(room)
        room = setup_room_l23()
        self.rooms.append(room)
        room = setup_room_l24()
        self.rooms.append(room)
        room = setup_room_l25()
        self.rooms.append(room)
        room = setup_room_l26()
        self.rooms.append(room)
        room = setup_room_l27()
        self.rooms.append(room)
        room = setup_room_l28()
        self.rooms.append(room)
        room = setup_room_l29()
        self.rooms.append(room)
        room = setup_room_l30()
        self.rooms.append(room)
        room = setup_room_l31()
        self.rooms.append(room)
        room = setup_room_l31()
        self.rooms.append(room)
        room = setup_room_l32()
        self.rooms.append(room)
        room = setup_room_l33()
        self.rooms.append(room)
        room = setup_room_l34()
        self.rooms.append(room)
        room = setup_room_l35()
        self.rooms.append(room)
        room = setup_room_l36()
        self.rooms.append(room)
        room = setup_room_l37()
        self.rooms.append(room)
        room = setup_room_l38()
        self.rooms.append(room)
        room = setup_room_l39()
        self.rooms.append(room)
        room = setup_room_l40()
        self.rooms.append(room)
        room = setup_room_l41()
        self.rooms.append(room)
        room = setup_room_l42()
        self.rooms.append(room)
        room = setup_room_l43()
        self.rooms.append(room)
        room = setup_room_l44()
        self.rooms.append(room)
        room = setup_room_l45()
        self.rooms.append(room)
        room = setup_room_l46()
        self.rooms.append(room)

        self.current_room = 21  # habitacion inicial (cambiar a 0)/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
        # Fisicas para la habitacion en la que estemos
        self.physics_engine = arcade.PhysicsEngineSimple(self.jugador, self.rooms[self.current_room].wall_list)

    def on_draw(self):
        arcade.start_render()
        if self.empezado:
            if self.pausado:
                HUD.dibujar_hud_pausado()
            elif self.jugador.muerto:
                HUD.dibujar_hud_gameover()
            else:
                # Draw the background texture
                arcade.draw_lrwh_rectangle_textured(0, 0,
                                                    SCREEN_WIDTH, SCREEN_HEIGHT,
                                                    self.rooms[self.current_room].background)
                HUD.dibujar_hud(self.vida_jugador, self.carga_fantasmal_jugador)
                if self.jugador.estado_fantasmal:
                    HUD.dibujar_contador_de_muerte(self.jugador.contador_de_muerte)
                self.rooms[self.current_room].wall_list.draw()
                self.player_list.draw()
                self.bullet_list.draw()
                self.rooms[self.current_room].enemigos_list.draw()
                self.rooms[self.current_room].balas_list.draw()
                self.rooms[self.current_room].recargas_list.draw()

        else:
            if self.mirando_controles:
                HUD.dibujar_controles()
            else:
                HUD.dibujar_pantalla_de_inicio()

    def on_update(self, delta_time: float = 1 / 60):
        if not self.pausado or self.jugador.muerto:
            # Actualizar todos los sprites
            self.physics_engine.update()
            self.jugador.update_animation()
            self.bullet_list.update()

            # Si estamos en modo fantasmal y matamos a todos los enemigos de la sala
            # --> reset de modo fantasmal (quitar buffs y demás)
            if len(self.rooms[self.current_room].enemigos_list) == 0 and self.jugador.estado_fantasmal:
                self.vida_jugador = 10
                self.jugador.desactivar_modo_fantasmal()
                # Quitamos los buffs
                self.velocidad_jugador /= 2
            # Si estamos en modo fantasamal y nos quedamos sin tiempo
            # --> game over
            if self.jugador.contador_de_muerte <= 0 and self.jugador.estado_fantasmal:
                # menor o igual que cero porque si ponemos igual a 0 puede que los updates no estén sincronizados
                # y nunca entremos a este if
                self.jugador.morir()
                return
            # Activar modo fantsamal (si podemos)
            if self.vida_jugador == 0 and not self.jugador.estado_fantasmal:
                if self.carga_fantasmal_jugador == 100:  # Aplicamos buffs modo fant.
                    self.jugador.activar_modo_fantasmal()
                    self.carga_fantasmal_jugador -= 100
                    # Buffs
                    self.velocidad_jugador *= 2  # doble velocidad
                else:  # morimos
                    self.jugador.morir()
                    return

            # Mirar en que habitación estamos y si necesitamos cambiar a otra
            # Prision: (0-6)

            if self.jugador.center_x > SCREEN_WIDTH - 90 and self.current_room == 0:  # 0-->1
                self.current_room = 1
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_x = 100
                self.bullet_list = arcade.SpriteList()  # Resetear la lista de balas
            elif self.jugador.center_x < 90 and self.current_room == 1:  # 1-->0
                self.current_room = 0
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.bullet_list = arcade.SpriteList()
                self.jugador.center_x = SCREEN_WIDTH - 110
            elif self.jugador.center_x > SCREEN_WIDTH - 90 and self.current_room == 1:  # 1-->2
                self.current_room = 2
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_x = 100
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_x < 90 and self.current_room == 2:  # 2-->1
                self.current_room = 1
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_x = SCREEN_WIDTH - 110
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_y > SCREEN_HEIGHT - 90 and self.current_room == 2:  # 2-->3
                self.current_room = 3
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_y = 100
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_y < 90 and self.current_room == 3:  # 3-->2
                self.current_room = 2
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_y = SCREEN_HEIGHT - 110
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_y < 90 and self.current_room == 2:  # 2-->4
                self.current_room = 4
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_y = SCREEN_HEIGHT - 110
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_y > SCREEN_HEIGHT - 90 and self.current_room == 4:  # 4-->2
                self.current_room = 2
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_y = 100
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_x > SCREEN_WIDTH - 90 and self.current_room == 4:  # 4-->5
                self.current_room = 5
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_x = 100
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_x < 90 and self.current_room == 5:  # 5-->4
                self.current_room = 4
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_x = SCREEN_WIDTH - 110
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_y < 90 and self.current_room == 4:  # 4-->6
                self.current_room = 6
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_y = SCREEN_HEIGHT - 110
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_y > SCREEN_HEIGHT - 90 and self.current_room == 6:  # 6-->4
                self.current_room = 4
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_y = 100
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_y < 90 and self.current_room == 6:  # 6-->Ruinas 7(r1)
                self.current_room = 7
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_y = 200  # emepzamos por la parte de abajo la primera sala de ruinas
                self.bullet_list = arcade.SpriteList()

            # Ruinas: (7-21)
            # Ruta principal:
            elif self.jugador.center_y > SCREEN_HEIGHT - 90 and self.current_room == 7:  # 7(r1)-->8(r2)
                self.current_room = 8
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_y = 100
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_y < 90 and self.current_room == 8:  # 8(r2)-->7(r1)
                self.current_room = 7
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_y = SCREEN_HEIGHT - 110
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_y > SCREEN_HEIGHT - 90 and self.current_room == 8:  # 8(r2)-->9(r3)
                self.current_room = 9
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_y = 100
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_y < 90 and self.current_room == 9:  # 9(r3)-->8(r2)
                self.current_room = 8
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_y = SCREEN_HEIGHT - 110
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_x > SCREEN_WIDTH - 90 and self.current_room == 9:  # 9(r3)-->10(r4)
                self.current_room = 10
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_x = 100
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_x < 90 and self.current_room == 10:  # 10(r4)-->9(r3)
                self.current_room = 9
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_x = SCREEN_WIDTH - 110
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_y > SCREEN_HEIGHT - 90 and self.current_room == 10:  # 10(r4)-->11(r5)
                self.current_room = 11
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_y = 100
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_y < 90 and self.current_room == 11:  # 11(r5)-->10(r4)
                self.current_room = 10
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_y = SCREEN_HEIGHT - 110
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_y > SCREEN_HEIGHT - 90 and self.current_room == 11:  # 11(r5)-->12(r6)
                self.current_room = 12
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_y = 100
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_y < 90 and self.current_room == 12:  # 12(r6)-->11(r5)
                self.current_room = 11
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_y = SCREEN_HEIGHT - 110
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_x > SCREEN_WIDTH - 90 and self.current_room == 12:  # 12(r6)-->13(r7)
                self.current_room = 13
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_x = 100
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_x < 90 and self.current_room == 13:  # 13(r7)-->12(r6)
                self.current_room = 12
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_x = SCREEN_WIDTH - 110
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_x > SCREEN_WIDTH - 90 and self.current_room == 13:  # 13(r7)-->14(r8)
                self.current_room = 14
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_x = 100
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_x < 90 and self.current_room == 14:  # 14(r8)-->13(r7)
                self.current_room = 13
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_x = SCREEN_WIDTH - 110
                self.bullet_list = arcade.SpriteList()
            # Desvío R3
            elif self.jugador.center_x < 90 and self.current_room == 9:  # 9(r3)-->15(r9)
                self.current_room = 15
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_x = SCREEN_WIDTH - 110
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_x > SCREEN_WIDTH - 90 and self.current_room == 15:  # 15(r9)-->9(r3)
                self.current_room = 9
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_x = 100
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_y > SCREEN_HEIGHT - 90 and self.current_room == 15:  # 15(r9)-->16(r10)
                self.current_room = 16
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_y = 100
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_y < 90 and self.current_room == 16:  # 16(r10)-->15(r9)
                self.current_room = 15
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_y = SCREEN_HEIGHT - 110
                self.bullet_list = arcade.SpriteList()
            # Desvío R1
            elif self.jugador.center_x < 90 and self.current_room == 7:  # 7(r1)-->17(r11)
                self.current_room = 17
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_x = SCREEN_WIDTH - 110
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_x > SCREEN_WIDTH - 90 and self.current_room == 17:  # 17(r11)-->7(r1)
                self.current_room = 7
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_x = 100
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_x < 90 and self.current_room == 17:  # 17(r11)-->18(r12)
                self.current_room = 18
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_x = SCREEN_WIDTH - 110
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_x > SCREEN_WIDTH - 90 and self.current_room == 18:  # 18(r12)-->17(r11)
                self.current_room = 17
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_x = 100
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_y < 90 and self.current_room == 18:  # 18(r12)-->19(r13)
                self.current_room = 19
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_y = SCREEN_HEIGHT - 110
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_y > SCREEN_HEIGHT - 90 and self.current_room == 19:  # 19(r13)-->18(r12)
                self.current_room = 18
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_y = 100
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_x < 90 and self.current_room == 18:  # 18(r12)-->20(r14)
                self.current_room = 20
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_x = SCREEN_WIDTH - 110
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_x > SCREEN_WIDTH - 90 and self.current_room == 20:  # 20(r14)-->18(r12)
                self.current_room = 18
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_x = 100
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_y > SCREEN_HEIGHT - 90 and self.current_room == 20:  # 20(r14)-->21(r15)
                self.current_room = 21
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_y = 100
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_y < 90 and self.current_room == 21:  # 21(r15)-->20(r14)
                self.current_room = 20
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_y = SCREEN_HEIGHT - 110
                self.bullet_list = arcade.SpriteList()

            # Laboratorio:
            elif self.jugador.center_y > SCREEN_HEIGHT - 90 and self.current_room == 22:  # 22(l1)-->23(l2)
                self.current_room = 23
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_y = 100
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_y < 90 and self.current_room == 23:  # 23(l2)-->22(l1)
                self.current_room = 22
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_y = SCREEN_HEIGHT - 110
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_y > SCREEN_HEIGHT - 90 and self.current_room == 23:  # 23(l2)-->24(l3)
                self.current_room = 24
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_y = 100
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_y < 90 and self.current_room == 24:  # 24(l3)-->23(l2)
                self.current_room = 23
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_y = SCREEN_HEIGHT - 110
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_y > SCREEN_HEIGHT - 90 and self.current_room == 24:  # 24(l3)-->25(l4)
                self.current_room = 25
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_y = 100
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_y < 90 and self.current_room == 25:  # 25(l4)-->24(l3)
                self.current_room = 24
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_y = SCREEN_HEIGHT - 110
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_x > SCREEN_WIDTH - 90 and self.current_room == 25:  # 25(l4)-->26(l5)
                self.current_room = 26
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_x = 100
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_x < 90 and self.current_room == 26:  # 26(l5)-->25(l4)
                self.current_room = 25
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_x = SCREEN_WIDTH - 110
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_x > SCREEN_WIDTH - 90 and self.current_room == 26:  # 26(l5)-->27(l6)
                self.current_room = 27
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_x = 100
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_x < 90 and self.current_room == 27:  # 27(l6)-->26(l5)
                self.current_room = 26
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_x = SCREEN_WIDTH - 110
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_x > SCREEN_WIDTH - 90 and self.current_room == 27:  # 27(l6)-->28(l7)
                self.current_room = 28
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_x = 100
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_x < 90 and self.current_room == 28:  # 28(l7)-->27(l6)
                self.current_room = 27
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_x = SCREEN_WIDTH - 110
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_x > SCREEN_WIDTH - 90 and self.current_room == 28:  # 28(l7)-->29(l8)
                self.current_room = 29
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_x = 100
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_x < 90 and self.current_room == 29:  # 29(l8)-->28(l7)
                self.current_room = 28
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_x = SCREEN_WIDTH - 110
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_x > SCREEN_WIDTH - 90 and self.current_room == 29:  # 29(l8)-->30(l9)
                self.current_room = 30
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_x = 100
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_x < 90 and self.current_room == 30:  # 30(l9)-->29(l8)
                self.current_room = 29
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_x = SCREEN_WIDTH - 110
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_y < 90 and self.current_room == 30:  # 30(l9)-->31(l10)
                self.current_room = 31
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_y = SCREEN_HEIGHT - 110
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_y > SCREEN_HEIGHT - 90 and self.current_room == 31:  # 31(l10)-->30(l9)
                self.current_room = 30
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_y = 100
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_y < 90 and self.current_room == 31:  # 31(l10)-->32(l11)
                self.current_room = 32
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_y = SCREEN_HEIGHT - 110
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_y > SCREEN_HEIGHT - 90 and self.current_room == 32:  # 32(l11)-->31(l10)
                self.current_room = 31
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_y = 100
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_y < 90 and self.current_room == 32:  # 32(l11)-->33(l12)
                self.current_room = 33
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_y = SCREEN_HEIGHT - 110
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_y > SCREEN_HEIGHT - 90 and self.current_room == 33:  # 33(l12)-->32(l11)
                self.current_room = 32
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_y = 100
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_x < 90 and self.current_room == 33:  # 33(l12)-->34(l13)
                self.current_room = 34
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_x = SCREEN_WIDTH - 110
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_x > SCREEN_WIDTH - 90 and self.current_room == 34:  # 34(l13)-->33(l12)
                self.current_room = 33
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_x = 100
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_x < 90 and self.current_room == 34:  # 34(l13)-->35(l14)
                self.current_room = 35
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_x = SCREEN_WIDTH - 110
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_x > SCREEN_WIDTH - 90 and self.current_room == 35:  # 35(l14)-->34(l13)
                self.current_room = 34
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_x = 100
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_x < 90 and self.current_room == 35:  # 35(l14)-->22(l1)
                self.current_room = 22
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_x = SCREEN_WIDTH - 110
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_x > SCREEN_WIDTH - 90 and self.current_room == 22:  # 22(l1)-->35(l14)
                self.current_room = 35
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_x = 100
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_y < 90 and self.current_room == 34:  # 34(l13)-->36(l15)
                self.current_room = 36
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_y = SCREEN_HEIGHT - 110
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_y > SCREEN_HEIGHT - 90 and self.current_room == 36:  # 36(l15)-->34(l13)
                self.current_room = 34
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_y = 100
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_y < 90 and self.current_room == 36:  # 36(l15)-->37(l16)
                self.current_room = 37
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_y = SCREEN_HEIGHT - 110
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_y > SCREEN_HEIGHT - 90 and self.current_room == 37:  # 37(l16)-->36(l15)
                self.current_room = 36
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_y = 100
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_x > SCREEN_WIDTH - 90 and self.current_room == 37:  # 37(l16)-->38(l17)
                self.current_room = 38
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_x = 100
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_x < 90 and self.current_room == 38:  # 38(l17)-->37(l16)
                self.current_room = 37
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_x = SCREEN_WIDTH - 110
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_y < 90 and self.current_room == 38:  # 38(l17)-->39(l18)
                self.current_room = 39
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_y = SCREEN_HEIGHT - 110
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_y > SCREEN_HEIGHT - 90 and self.current_room == 39:  # 39(l18)-->38(l17)
                self.current_room = 38
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_y = 100
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_y < 90 and self.current_room == 39:  # 39(l18)-->40(l19)
                self.current_room = 40
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_y = SCREEN_HEIGHT - 110
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_y > SCREEN_HEIGHT - 90 and self.current_room == 40:  # 40(l19)-->39(l18)
                self.current_room = 39
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_y = 100
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_x < 90 and self.current_room == 40:  # 40(l19)-->41(l20)
                self.current_room = 41
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_x = SCREEN_WIDTH - 110
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_x > SCREEN_WIDTH - 90 and self.current_room == 41:  # 41(l20)-->40(l19)
                self.current_room = 40
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_x = 100
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_x < 90 and self.current_room == 41:  # 41(l20)-->42(l21)
                self.current_room = 42
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_x = SCREEN_WIDTH - 110
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_x > SCREEN_WIDTH - 90 and self.current_room == 42:  # 42(l21)-->41(l20)
                self.current_room = 41
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_x = 100
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_y > SCREEN_HEIGHT - 90 and self.current_room == 42:  # 42(l21)-->43(l22)
                self.current_room = 43
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_y = 100
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_y < 90 and self.current_room == 43:  # 43(l22)-->42(l21)
                self.current_room = 42
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_y = SCREEN_HEIGHT - 110
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_y > SCREEN_HEIGHT - 90 and self.current_room == 43:  # 43(l22)-->44(l23)
                self.current_room = 44
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_y = 100
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_y < 90 and self.current_room == 44:  # 44(l23)-->43(l22)
                self.current_room = 43
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_y = SCREEN_HEIGHT - 110
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_x < 90 and self.current_room == 44:  # 44(l23)-->45(l24)
                self.current_room = 45
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_x = SCREEN_WIDTH - 110
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_x > SCREEN_WIDTH - 90 and self.current_room == 45:  # 45(l24)-->44(l23)
                self.current_room = 44
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_x = 100
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_x > SCREEN_WIDTH - 90 and self.current_room == 44:  # 44(l23)-->37(l16)
                self.current_room = 37
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_x = 100
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_x < 90 and self.current_room == 37:  # 37(l16)-->44(l23)
                self.current_room = 44
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_x = SCREEN_WIDTH - 110
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_x < 90 and self.current_room == 45:  # 45(l24)-->46(l25)
                self.current_room = 46
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_x = SCREEN_WIDTH - 110
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_x > SCREEN_WIDTH - 90 and self.current_room == 46:  # 46(l25)-->45(l24)
                self.current_room = 45
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_x = 100
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_y > SCREEN_HEIGHT - 90 and self.current_room == 46:  # 46(l25)-->47(l26)
                self.current_room = 47
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_y = 100
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_y < 90 and self.current_room == 47:  # 47(l26)-->46(l25)
                self.current_room = 46
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_y = SCREEN_HEIGHT - 110
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_y > SCREEN_HEIGHT - 90 and self.current_room == 47:  # 47(l26)-->48(l27)
                self.current_room = 48
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_y = 100
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_y < 90 and self.current_room == 48:  # 48(l27)-->47(l26)
                self.current_room = 47
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_y = SCREEN_HEIGHT - 110
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_x > SCREEN_WIDTH - 90 and self.current_room == 48:  # 48(l27)-->22(l1)
                self.current_room = 22
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_x = 100
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_x < 90 and self.current_room == 22:  # 22(l1)-->48(l27)
                self.current_room = 48
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_x = SCREEN_WIDTH - 110
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_x < 90 and self.current_room == 47:  # 47(l26)-->49(l28)
                self.current_room = 49
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_x = SCREEN_WIDTH - 110
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_x > SCREEN_WIDTH - 90 and self.current_room == 49:  # 49(l28)-->47(l26)
                self.current_room = 47
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_x = 100
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_x < 90 and self.current_room == 49:  # 49(l28)-->50(l29)
                self.current_room = 50
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_x = SCREEN_WIDTH - 110
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_x > SCREEN_WIDTH - 90 and self.current_room == 50:  # 50(l29)-->49(l28)
                self.current_room = 49
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_x = 100
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_x < 90 and self.current_room == 50:  # 50(l29)-->51(l30)
                self.current_room = 51
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_x = SCREEN_WIDTH - 110
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_x > SCREEN_WIDTH - 90 and self.current_room == 51:  # 51(l30)-->50(l29)
                self.current_room = 50
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_x = 100
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_x < 90 and self.current_room == 51:  # 51(l30)-->52(l31)
                self.current_room = 52
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_x = SCREEN_WIDTH - 110
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_x > SCREEN_WIDTH - 90 and self.current_room == 52:  # 52(l31)-->51(l30)
                self.current_room = 51
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_x = 100
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_y > SCREEN_HEIGHT - 90 and self.current_room == 52:  # 52(l31)-->53(l32)
                self.current_room = 53
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_y = 100
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_y < 90 and self.current_room == 53:  # 53(l32)-->52(l31)
                self.current_room = 52
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_y = SCREEN_HEIGHT - 110
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_x < 90 and self.current_room == 53:  # 53(l32)-->54(l33)
                self.current_room = 54
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_x = SCREEN_WIDTH - 110
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_x > SCREEN_WIDTH - 90 and self.current_room == 54:  # 54(l33)-->53(l32)
                self.current_room = 53
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_x = 100
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_y > SCREEN_HEIGHT - 90 and self.current_room == 53:  # 53(l32)-->55(l34)
                self.current_room = 55
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_y = 100
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_y < 90 and self.current_room == 55:  # 55(l34)-->53(l32)
                self.current_room = 53
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_y = SCREEN_HEIGHT - 110
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_y > SCREEN_HEIGHT - 90 and self.current_room == 55:  # 55(l34)-->56(l35)
                self.current_room = 56
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_y = 100
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_y < 90 and self.current_room == 56:  # 56(l35)-->55(l34)
                self.current_room = 55
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_y = SCREEN_HEIGHT - 110
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_x > SCREEN_WIDTH - 90 and self.current_room == 56:  # 56(l35)-->57(l36)
                self.current_room = 57
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_x = 100
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_x < 90 and self.current_room == 57:  # 57(l36)-->56(l35)
                self.current_room = 56
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_x = SCREEN_WIDTH - 110
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_x > SCREEN_WIDTH - 90 and self.current_room == 57:  # 57(l36)-->58(l37)
                self.current_room = 58
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_x = 100
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_x < 90 and self.current_room == 58:  # 58(l37)-->57(l36)
                self.current_room = 57
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_x = SCREEN_WIDTH - 110
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_y < 90 and self.current_room == 58:  # 58(l37)-->59(l38)
                self.current_room = 59
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_y = SCREEN_HEIGHT - 110
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_y > SCREEN_HEIGHT - 90 and self.current_room == 59:  # 59(l38)-->58(l37)
                self.current_room = 58
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_y = 100
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_y < 90 and self.current_room == 59:  # 59(l38)-->60(l39)
                self.current_room = 60
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_y = SCREEN_HEIGHT - 110
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_y > SCREEN_HEIGHT - 90 and self.current_room == 60:  # 60(l39)-->59(l38)
                self.current_room = 59
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_y = 100
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_y < 90 and self.current_room == 60:  # 60(l39)-->50(l29)
                self.current_room = 50
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_y = SCREEN_HEIGHT - 110
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_y > SCREEN_HEIGHT - 90 and self.current_room == 50:  # 50(l29)-->60(l39)
                self.current_room = 60
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_y = 100
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_y < 90 and self.current_room == 50:  # 50(l29)-->61(l40)
                self.current_room = 61
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_y = SCREEN_HEIGHT - 110
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_y > SCREEN_HEIGHT - 90 and self.current_room == 61:  # 61(l40)-->50(l29)
                self.current_room = 50
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_y = 100
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_y < 90 and self.current_room == 61:  # 61(l40)-->62(l41)
                self.current_room = 62
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_y = SCREEN_HEIGHT - 110
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_y > SCREEN_HEIGHT - 90 and self.current_room == 62:  # 62(l41)-->61(l40)
                self.current_room = 61
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_y = 100
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_y < 90 and self.current_room == 62:  # 62(l41)-->63(l42)
                self.current_room = 63
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_y = SCREEN_HEIGHT - 110
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_y > SCREEN_HEIGHT - 90 and self.current_room == 63:  # 63(l42)-->62(l41)
                self.current_room = 62
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_y = 100
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_x < 90 and self.current_room == 63:  # 63(l42)-->64(l43)
                self.current_room = 64
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_x = SCREEN_WIDTH - 110
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_x > SCREEN_WIDTH - 90 and self.current_room == 64:  # 64(l43)-->63(l42)
                self.current_room = 63
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_x = 100
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_x < 90 and self.current_room == 64:  # 64(l43)-->65(l44)
                self.current_room = 65
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_x = SCREEN_WIDTH - 110
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_x > SCREEN_WIDTH - 90 and self.current_room == 65:  # 65(l44)-->64(l43)
                self.current_room = 64
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_x = 100
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_x < 90 and self.current_room == 65:  # 65(l44)-->66(l45)
                self.current_room = 66
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_x = SCREEN_WIDTH - 110
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_x > SCREEN_WIDTH - 90 and self.current_room == 66:  # 66(l45)-->65(l44)
                self.current_room = 65
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_x = 100
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_x > SCREEN_WIDTH - 90 and self.current_room == 30:  # 30(l9)-->67(l46)
                self.current_room = 67
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_x = 100
                self.bullet_list = arcade.SpriteList()
            elif self.jugador.center_x < 90 and self.current_room == 67:  # 67(46)-->30(l9)
                self.current_room = 30
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_x = SCREEN_WIDTH - 110
                self.bullet_list = arcade.SpriteList()
            # Pasar a la sala del boss final (no se puede volver)
            elif self.jugador.center_y > SCREEN_HEIGHT - 90 and self.current_room == 66:  # 66(l45)-->67(boss)
                self.current_room = 67
                self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                 self.rooms[self.current_room].wall_list)
                self.jugador.center_y = 100
                self.bullet_list = arcade.SpriteList()

            # Actualizar balas jugador
            # Loop through each bullet
            for bala in self.bullet_list:
                # Mirar si ha chocado con una pared
                hit_list = arcade.check_for_collision_with_list(bala, self.rooms[self.current_room].wall_list)
                # Si choca contra una pared, eliminar la bala
                if len(hit_list) > 0:
                    bala.remove_from_sprite_lists()
                # Mirar si choca contra un enemigo
                hit_list2 = arcade.check_for_collision_with_list(bala, self.rooms[self.current_room].enemigos_list)
                if len(hit_list2) > 0:
                    # Vamos a identificar el enemigo que ha sido golpeado:
                    for enemigo in self.rooms[self.current_room].enemigos_list:
                        if enemigo in hit_list2:
                            enemigo.recibir_damage(1)  # Pendiente de implementar poder hacer más daño?
                            # Muerte de enemigos
                            if enemigo.vida <= 0:
                                # (por si les hacemos más daño de la vida que tienen y se queda con vida negativa)
                                # Dropeos
                                n = random.randint(0, 10)
                                if n == 10 or n == 9:  # 20 % de drop
                                    # Dropeo exitoso:
                                    recarga = arcade.Sprite("sprites_master" + os.path.sep + "DISPOSITIVOFANTASMA.png")
                                    recarga.center_x = enemigo.center_x
                                    recarga.center_y = enemigo.center_y
                                    self.rooms[self.current_room].recargas_list.append(recarga)

                                # Eliminamos al enemigo sin vida
                                enemigo.remove_from_sprite_lists()

                    bala.remove_from_sprite_lists()

            for enemigos in self.rooms[self.current_room].enemigos_list:
                enemigos.disparar(enemigos, Velocidad_Disparo_Enemigos, self.jugador)

            # Mirar si hemos cogido alguna recarga
            hit_list3 = arcade.check_for_collision_with_list(self.jugador, self.rooms[self.current_room].recargas_list)
            for recarga in hit_list3:
                recarga.remove_from_sprite_lists()
                self.carga_fantasmal_jugador += 10

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        # Comienzo del juego
        if not self.empezado:
            if key == arcade.key.ENTER:
                self.empezado = True
            elif key == arcade.key.C:
                self.mirando_controles = True
            elif key == arcade.key.BACKSPACE:
                self.mirando_controles = False
            return  # no necesitamos comprbar más controles
        if self.jugador.muerto:
            # Reiniciar el juego desde el principio:
            if key == arcade.key.R:  # Potencialmente puede dar problemas más adelante!!! REVISAR /\/\/\/\/\/\/\/\/\/\
                self.setup()
                self.jugador.muerto = False
                self.jugador.estado_fantasmal = False  # por si morimos en modo fontasmal
                self.vida_jugador = 10
                self.carga_fantasmal_jugador = 100
        # Pausar el juego
        if key == arcade.key.P and not self.pausado:
            self.pausado = True
        elif key == arcade.key.P and self.pausado:
            self.pausado = False
        # Movimiento
        if key == arcade.key.UP or key == arcade.key.W:
            self.jugador.change_y = self.velocidad_jugador
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.jugador.change_y = -self.velocidad_jugador
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.jugador.change_x = -self.velocidad_jugador
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.jugador.change_x = self.velocidad_jugador
        # Disparo
        if key == arcade.key.Q:
            bala = self.jugador.disparar(self.jugador, self.velocidad_disparo)
            self.bullet_list.append(bala)
        # Bloquear direccion a la que mira el personaje (hay que mantener)
        if key == arcade.key.SPACE:
            self.jugador.bloquear_direccion()
        # Hacerse daño a sí mismo (PROVISIONAL, PARA PRUEBAS)/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
        if key == arcade.key.Z:
            self.vida_jugador -= 5

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """
        if key == arcade.key.UP or key == arcade.key.DOWN or key == arcade.key.W or key == arcade.key.S:
            self.jugador.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT or key == arcade.key.A or key == arcade.key.D:
            self.jugador.change_x = 0
        # Desbloquear direccion a la que mira el personaje
        if key == arcade.key.SPACE:
            self.jugador.desbloquear_direccion()


def main():
    ventana = SteamPunkGame()
    ventana.setup()
    arcade.run()


if __name__ == "__main__":
    main()
