import arcade
import Jugador
import os
import math

# --- Constantes ---

# SPRITE_SCALING_BOX = 0.5
# SPRITE_SCALING_PLAYER = 0.5

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 900

MOVEMENT_SPEED = 5

LARGO_MURO = 50
ANCHO_MURO = 10
TAM_SUELO = 50  # Tamaño de cada "cuadro" de suelo


class Room:
    """
    This class holds all the information about the
    different rooms.
    """

    def __init__(self):
        # You may want many lists. Lists for coins, monsters, etc.
        self.wall_list = None
        # self.floor_list = None

        # This holds the background images. If you don't want changing
        # background images, you can delete this part.
        # self.background = None


def setup_room_1():
    """
    Create and return room 1.
    """
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    # room.floor_list = arcade.SpriteList()

    # --- Set up the walls ---
    # Nota: 'muro' es vertical y 'muro2' es horizontal
    # Fila de abajo y arriba de pared
    for y in (0, SCREEN_HEIGHT - ANCHO_MURO):
        for x in range(0, SCREEN_WIDTH, LARGO_MURO):
            muro = arcade.Sprite("sprites_master" + os.path.sep + "Muro2.png")
            muro.left = x
            muro.bottom = y
            room.wall_list.append(muro)

    # Fila de la izquierda y la derecha
    for x in (0, SCREEN_WIDTH - ANCHO_MURO):
        for y in range(0, SCREEN_HEIGHT - ANCHO_MURO, LARGO_MURO):
            muro = arcade.Sprite("sprites_master" + os.path.sep + "Muro.png")
            if not (300 <= y <= 400) or x == 0:  # Agujero en la parte izquierda para pasar a la siguiente habitacion
                muro.left = x
                muro.bottom = y
                room.wall_list.append(muro)

    # Poner suelo
    # Con pequeños trozos de suelo
    # for x in range(ANCHO_MURO, SCREEN_WIDTH - TAM_SUELO, TAM_SUELO):  # NO cabe muy bien
    #    for y in range(ANCHO_MURO, SCREEN_HEIGHT - TAM_SUELO, TAM_SUELO):
    #        suelo = arcade.Sprite("sprites_master" + os.path.sep + "SueloPequeño.png")
    #        suelo.left = x
    #        suelo.bottom = y
    #        room.floor_list.append(suelo)

    # If you want coins or monsters in a level, then add that code here.
    # Load the background image for this level.
    # room.background = arcade.load_texture("ruta")

    return room


def setup_room_2():
    """
    Create and return room 2.
    """
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("test.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "ROCAS Y CAJAS")

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
        # Variables para el disparo del jugador
        self.velocidad_disparo = 10

    def setup(self):
        arcade.set_background_color(arcade.color.WOOD_BROWN)
        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        # Create the player
        self.jugador = Jugador.Jugador()  # OJO!
        self.jugador.center_x = 100
        self.jugador.center_y = 100
        self.player_list.append(self.jugador)

        # Rooms
        self.rooms = []  # lista de todas las habitaciones
        room = setup_room_1()  # convendria hacer un for cuando se pongan mas
        self.rooms.append(room)

        room = setup_room_2()
        self.rooms.append(room)
        self.current_room = 0  # habitacion inicial
        # Fisicas para la habitacion en la que estemos
        self.physics_engine = arcade.PhysicsEngineSimple(self.jugador, self.rooms[self.current_room].wall_list)

    def on_draw(self):
        arcade.start_render()
        self.rooms[self.current_room].wall_list.draw()
        # self.rooms[self.current_room].floor_list.draw()
        self.player_list.draw()
        self.bullet_list.draw()

    def on_update(self, delta_time: float = 1 / 60):
        # Actualizar todos los sprites
        self.physics_engine.update()
        self.jugador.update_animation()
        self.bullet_list.update()

        # Mirar en que habitación estamos y si necesitamos cambiar a otra
        if self.jugador.center_x > SCREEN_WIDTH and self.current_room == 0:
            self.current_room = 1
            self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                             self.rooms[self.current_room].wall_list)
            self.jugador.center_x = ANCHO_MURO + 1
            self.bullet_list = arcade.SpriteList()  # Resetear la lista de balas
        elif self.jugador.center_x < 0 and self.current_room == 1:
            self.current_room = 0
            self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                             self.rooms[self.current_room].wall_list)
            self.bullet_list = arcade.SpriteList()  # Resetear la lista de balas
            self.jugador.center_x = SCREEN_WIDTH

        # Actualizar balas jugador
        # Loop through each bullet
        for bala in self.bullet_list:
            # Mirar si ha chocado con una pared
            hit_list = arcade.check_for_collision_with_list(bala, self.rooms[self.current_room].wall_list)
            # Si choca contra una pared, eliminar la bala
            if len(hit_list) > 0:
                bala.remove_from_sprite_lists()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        # Movimiento
        if key == arcade.key.UP or key == arcade.key.W:
            self.jugador.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.jugador.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.jugador.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.jugador.change_x = MOVEMENT_SPEED

        # Disparo
        if key == arcade.key.Q:
            bala = self.jugador.disparar(self.jugador, self.velocidad_disparo)
            self.bullet_list.append(bala)

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """
        if key == arcade.key.UP or key == arcade.key.DOWN or key == arcade.key.W or key == arcade.key.S:
            self.jugador.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT or key == arcade.key.A or key == arcade.key.D:
            self.jugador.change_x = 0


def main():
    ventana = SteamPunkGame()
    ventana.setup()
    arcade.run()


if __name__ == "__main__":
    main()
