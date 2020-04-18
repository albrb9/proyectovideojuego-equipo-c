import arcade

# Constantes para mirar a que lado mira
RIGHT_FACING = 0
LEFT_FACING = 1
UP_FACING = 2
DOWN_FACING = 3

# Veces que se actualizan las texturas por segundo
UPDATES_PER_FRAME = 10
NUM_TEXTURAS_ANDAR = 2


def load_texture_pair(filename):
    """
    Load a texture pair, with the second being a mirror image.
    (El espejo no hace nada para sprites de mirar arriba o abajo)
    """
    return [
        arcade.load_texture(filename),
        arcade.load_texture(filename, mirrored=True)
    ]


def load_texture_4dir(filename_lados, filename_up, filename_down):
    """
    Load a texture pair, with the second being a mirror image.
    (El espejo no hace nada para sprites de mirar arriba o abajo)
    """
    return [
        arcade.load_texture(filename_lados),
        arcade.load_texture(filename_lados, mirrored=True),
        arcade.load_texture(filename_up),
        arcade.load_texture(filename_down)
    ]


class Jugador(arcade.Sprite):
    def __init__(self):
        super().__init__()

        # Dirección a la que mira por defecto
        self.character_face_direction = RIGHT_FACING  # tiene valores del 0 al 3

        # Used for flipping between image sequences
        self.cur_texture = 0

        # ---Cargar texturas---
        self.textura_quieto = load_texture_4dir("sprites_master/PERSONAJE10.png", "sprites_master/PERSONAJE7.png",
                                                "sprites_master/PERSONAJE4.png")
        self.textura_andando = []
        for i in (11, 12):
            # Cargamos texturas 11 y 12 (derecha moviendo los pies)
            # 8 y 9 (arriba moviendo los pies)
            # 5 y 6 (abajo moviendo los pies)
            self.textura_andando.append(load_texture_4dir("sprites_master/PERSONAJE{}.png".format(i),
                                                          "sprites_master/PERSONAJE{}.png".format(i - 3),
                                                          "sprites_master/PERSONAJE{}.png".format(i - 6)))

    def update_animation(self, delta_time: float = 1 / 60):

        # Vemos adonde tenemos que mirar
        if self.change_x < 0 and (self.character_face_direction == RIGHT_FACING or UP_FACING or DOWN_FACING):
            self.character_face_direction = LEFT_FACING
        elif self.change_x > 0 and (self.character_face_direction == LEFT_FACING or UP_FACING or DOWN_FACING):
            self.character_face_direction = RIGHT_FACING
        elif self.change_y < 0 and (self.character_face_direction == RIGHT_FACING or LEFT_FACING or UP_FACING):
            self.character_face_direction = DOWN_FACING
        elif self.change_y > 0 and (self.character_face_direction == RIGHT_FACING or LEFT_FACING or DOWN_FACING):
            self.character_face_direction = UP_FACING

        # Animación estando quieto
        if self.change_x == 0 and self.change_y == 0:
            self.texture = self.textura_quieto[self.character_face_direction]
            return  # si entramos en este if no debemos mirar nada más de actualizar texturas

        # Walking animation
        self.cur_texture += 1
        if self.cur_texture >= NUM_TEXTURAS_ANDAR * UPDATES_PER_FRAME:
            self.cur_texture = 0
        self.texture = self.textura_andando[self.cur_texture // UPDATES_PER_FRAME][
            self.character_face_direction]
