import arcade

RIGHT_FACING = 0
LEFT_FACING = 1
UP_FACING = 2
DOWN_FACING = 3

UPDATES_PER_FRAME = 10
NUM_TEXTURAS_ANDAR = 2

def load_texture_pair(filename,filename_arriba,filename_abajo):
    """
    Load a texture pair, with the second being a mirror image.
    """
    return [
        arcade.load_texture(filename),
        arcade.load_texture(filename, mirrored=True)
        arcade.load_texture(filename_arriba)
        arcade.load_texture(filename_abajo)
    ]

class Masked(arcade.sprite):
    def __init__(self, filename, sprite_scaling):

        super().__init__(filename, sprite_scaling)

        self.character_face_direction = RIGHT_FACING

        self.cur_texture = 0

        self.change_x = 0
        self.change_y = 0

        self.textura_quieto = load_texture_pair("sprites_master/MASKED1.png", "sprites_master/MASKED10.png",
                                                "sprites_master/MASKED7.png")

        self.textura_andar = []
        for i in range(11,12):
            texture = load_texture_pair(f"sprites_master/MASKED{i-6}.png",f"sprites_master/MASKED{i}.png",f"sprites_master/MASKED{i-3}.png")
            self.walk_textures.append(texture)

        self.texture = self.idle_texture_pair[0]

        self.set_hit_box(self.texture.hit_box_points)

    def actualizar_animacion(self, delta_time: float = 1 / 60):

        #Saber si hay que mirar hacia la derecha, izquierda, arriba o abajo.
        if self.change_x < 0 and self.character_face_direction == RIGHT_FACING or UP_FACING or DOWN_FACING:
            self.character_face_direction = LEFT_FACING
        elif self.change_x > 0 and self.character_face_direction == LEFT_FACING or UP_FACING or DOWN_FACING:
            self.character_face_direction = RIGHT_FACING
        elif self.change_y < 0 and self.character_face_direction == LEFT_FACING or RIGHT_FACING or UP_FACING:
            self.character_face_direction = DOWN_FACING
        elif self.change_y > 0 and self.character_face_direction == LEFT_FACING or RIGHT_FACING or DOWN_FACING:
            self.character_face_direction = UP_FACING

        if self.change_x == 0:
            self.texture = self.idle_texture_pair[self.character_face_direction]
            return

        self.cur_texture += 1
        if self.cur_texture >= NUM_TEXTURAS_ANDAR * UPDATES_PER_FRAME:
            self.cur_texture = 0
        self.texture = self.textura_andando[self.cur_texture // UPDATES_PER_FRAME][
            self.character_face_direction]

class Esqueleto(arcade.sprite):
    def __init__(self, filename, sprite_scaling):

        super().__init__(filename, sprite_scaling)

        self.character_face_direction = RIGHT_FACING

        self.cur_texture = 0

        self.change_x = 0
        self.change_y = 0

        self.textura_quieto = load_texture_pair("sprites_master/ESQUELETO1.png", "sprites_master/ESQUELETO10.png",
                                                "sprites_master/ESQUELETO7.png")

        self.textura_andar = []
        for i in range(11,12):
            texture = load_texture_pair(f"sprites_master/ESQUELETO{i-6}.png",f"sprites_master/ESQUELETO{i}.png",f"sprites_master/ESQUELETO{i-3}.png")
            self.walk_textures.append(texture)

        self.texture = self.idle_texture_pair[0]

        self.set_hit_box(self.texture.hit_box_points)

    def actualizar_animacion(self, delta_time: float = 1 / 60):

        #Saber si hay que mirar hacia la derecha, izquierda, arriba o abajo.
        if self.change_x < 0 and self.character_face_direction == RIGHT_FACING or UP_FACING or DOWN_FACING:
            self.character_face_direction = LEFT_FACING
        elif self.change_x > 0 and self.character_face_direction == LEFT_FACING or UP_FACING or DOWN_FACING:
            self.character_face_direction = RIGHT_FACING
        elif self.change_y < 0 and self.character_face_direction == LEFT_FACING or RIGHT_FACING or UP_FACING:
            self.character_face_direction = DOWN_FACING
        elif self.change_y > 0 and self.character_face_direction == LEFT_FACING or RIGHT_FACING or DOWN_FACING:
            self.character_face_direction = UP_FACING

        if self.change_x == 0:
            self.texture = self.idle_texture_pair[self.character_face_direction]
            return

        self.cur_texture += 1
        if self.cur_texture >= NUM_TEXTURAS_ANDAR * UPDATES_PER_FRAME:
            self.cur_texture = 0
        self.texture = self.textura_andando[self.cur_texture // UPDATES_PER_FRAME][
            self.character_face_direction]

class GasMask(arcade.sprite):

    def __init__(self, filename, sprite_scaling):

        super().__init__(filename, sprite_scaling)

        self.character_face_direction = RIGHT_FACING

        self.cur_texture = 0

        self.change_x = 0
        self.change_y = 0

        self.textura_quieto = load_texture_pair("sprites_master/GASMASK1.png", "sprites_master/GASMASK10.png",
                                                "sprites_master/GASMASK7.png")

        self.textura_andar = []
        for i in range(11,12):
            texture = load_texture_pair(f"sprites_master/GASMASK{i-6}.png",f"sprites_master/GASMASK{i}.png",f"sprites_master/GASMASK{i-3}.png")
            self.walk_textures.append(texture)

        self.texture = self.idle_texture_pair[0]

        self.set_hit_box(self.texture.hit_box_points)

    def gas(self, velocidad_proyectil, GasMask):

        proyectil_gaseoso = arcade.Sprite("sprites_master/GASATTACK.png")


    def actualizar_animacion(self, delta_time: float = 1 / 60):

        #Saber si hay que mirar hacia la derecha, izquierda, arriba o abajo.
        if self.change_x < 0 and self.character_face_direction == RIGHT_FACING or UP_FACING or DOWN_FACING:
            self.character_face_direction = LEFT_FACING
        elif self.change_x > 0 and self.character_face_direction == LEFT_FACING or UP_FACING or DOWN_FACING:
            self.character_face_direction = RIGHT_FACING
        elif self.change_y < 0 and self.character_face_direction == LEFT_FACING or RIGHT_FACING or UP_FACING:
            self.character_face_direction = DOWN_FACING
        elif self.change_y > 0 and self.character_face_direction == LEFT_FACING or RIGHT_FACING or DOWN_FACING:
            self.character_face_direction = UP_FACING

        if self.change_x == 0:
            self.texture = self.idle_texture_pair[self.character_face_direction]
            return

        self.cur_texture += 1
        if self.cur_texture >= NUM_TEXTURAS_ANDAR * UPDATES_PER_FRAME:
            self.cur_texture = 0
        self.texture = self.textura_andando[self.cur_texture // UPDATES_PER_FRAME][
            self.character_face_direction]






