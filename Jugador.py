import arcade

# Constantes para mirar a que lado mira
RIGHT_FACING = 0
LEFT_FACING = 1

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


class Jugador(arcade.Sprite):
    def __init__(self):
        super().__init__()

        # Dirección a la que mira por defecto
        self.character_face_direction = RIGHT_FACING

        # Used for flipping between image sequences
        self.cur_texture_lados = 0
        self.cur_texture_up = 0
        self.cur_texture_down = 0

        # ---Cargar texturas---
        self.textura_quieto = load_texture_pair("sprites_master/PERSONAJE10.png")

        self.textura_andando_lados = []
        for i in (11, 12):
            # Cargamos texturas 11 y 12 (derecha moviendo los pies), al cargar la pareja tenemos también la izquierda
            self.textura_andando_lados.append(load_texture_pair("sprites_master/PERSONAJE{}.png".format(i)))
        self.textura_andando_up = []
        for i in (8, 9):
            # Cargamos texturas 8 y 9 (arriba moviendo los pies)
            self.textura_andando_up.append(load_texture_pair("sprites_master/PERSONAJE{}.png".format(i)))
        self.textura_andando_down = []
        for i in (5, 6):
            # Cargamos texturas 8 y 9 (abajo moviendo los pies)
            self.textura_andando_down.append(load_texture_pair("sprites_master/PERSONAJE{}.png".format(i)))

    def update_animation(self, delta_time: float = 1 / 60):

        # Vemos adonde tenemos que mirar
        if self.change_x < 0 and self.character_face_direction == RIGHT_FACING:
            self.character_face_direction = LEFT_FACING
        elif self.change_x > 0 and self.character_face_direction == LEFT_FACING:
            self.character_face_direction = RIGHT_FACING

        # Animación estando quieto
        if self.change_x == 0 and self.change_y == 0:
            self.texture = self.textura_quieto[self.character_face_direction]
            return  # si entramos en este if no debemos mirar nada más de actualizar texturas

        # Walking animation
        if self.change_y == 0:  # IZQ/DER
            self.cur_texture_lados += 1
            if self.cur_texture_lados >= NUM_TEXTURAS_ANDAR * UPDATES_PER_FRAME:
                self.cur_texture_lados = 0
            self.texture = self.textura_andando_lados[self.cur_texture_lados // UPDATES_PER_FRAME][
                self.character_face_direction]
        else:  # UP/DOWN
            if self.change_y > 0:
                self.cur_texture_up += 1
                if self.cur_texture_up >= NUM_TEXTURAS_ANDAR * UPDATES_PER_FRAME:
                    self.cur_texture_up = 0
                self.texture = self.textura_andando_up[self.cur_texture_up // UPDATES_PER_FRAME][
                    self.character_face_direction]
            else:
                self.cur_texture_down += 1
                if self.cur_texture_down >= NUM_TEXTURAS_ANDAR * UPDATES_PER_FRAME:
                    self.cur_texture_down = 0
                self.texture = self.textura_andando_down[self.cur_texture_down // UPDATES_PER_FRAME][
                    self.character_face_direction]
