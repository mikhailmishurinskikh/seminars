from random import randint

gravitational_constant = 6.67408E-11

class Star():
    
    type = "star"
    """Признак объекта звезды"""

    m = 0
    """Масса звезды"""

    x = 0
    """Координата по оси **x**"""

    y = 0
    """Координата по оси **y**"""

    Vx = 0
    """Скорость по оси **x**"""

    Vy = 0
    """Скорость по оси **y**"""

    Fx = 0
    """Сила по оси **x**"""

    sectorial_v = 0

    Fy = 0
    """Сила по оси **y**"""

    R = 5
    """Радиус звезды"""

    color = "red"
    """Цвет звезды"""

    image = None
    """Изображение звезды"""


class Planet():

    type = "planet"
    """Признак объекта планеты"""

    m = 0
    """Масса планеты"""

    x = 0
    """Координата по оси **x**"""

    y = 0
    """Координата по оси **y**"""

    Vx = 0
    """Скорость по оси **x**"""

    Vy = 0
    """Скорость по оси **y**"""

    Fx = 0
    """Сила по оси **x**"""

    Fy = 0
    """Сила по оси **y**"""
    sectorial_v = 0

    R = 5
    """Радиус планеты"""

    color = "green"
    """Цвет планеты"""

    image = None
    """Изображение планеты"""
    
    
def calculate_force(body, space_objects):
    """Вычисляет силу, действующую на тело.

    Параметры:

    **body** — тело, для которого нужно вычислить дейстующую силу.

    **space_objects** — список объектов, которые воздействуют на тело.
    """

    body.Fx = 0
    body.Fy = 0
    for obj in space_objects:
        if body == obj:
            continue
        r = ((body.x - obj.x)**2 + (body.y - obj.y)**2)**0.5
        cos = (obj.x - body.x) / r
        sin = (obj.y - body.y) / r
        body.Fx += gravitational_constant * (body.m * obj.m / r**2) * cos
        body.Fy += gravitational_constant * (body.m * obj.m / r**2) * sin
        if obj.type == 'star' and body.type == 'planet':
            body.sectorial_v = r * (abs(sin) * abs(body.Vx) + abs(body.Vy) * abs(cos)) / 2


def move_space_object(body, dt):
    """Перемещает тело в соответствии с действующей на него силой.

    Параметры:

    **body** — тело, которое нужно переместить.
    """

    ax = body.Fx / body.m
    body.Vx += dt * ax
    body.x += body.Vx * dt
    ay = body.Fy / body.m 
    body.Vy += dt * ay
    body.y += body.Vy * dt
    
def recalculate_space_objects_positions(space_objects, dt):
    """Пересчитывает координаты объектов.

    Параметры:

    **space_objects** — список оьъектов, для которых нужно пересчитать координаты.

    **dt** — шаг по времени
    """

    for body in space_objects:
        calculate_force(body, space_objects)
    for body in space_objects:
        move_space_object(body, dt)


if __name__ == "__main__":
    print("This module is not for direct call!")
