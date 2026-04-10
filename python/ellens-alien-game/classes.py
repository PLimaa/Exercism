"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Number of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """
    health = 3
    total_aliens_created=0

    def __init__(self,x_coordinate,y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        Alien.total_aliens_created +=1

    def hit(self):
        self.health -= 1

    def is_alive(self):
        if self.health >= 1 :
            return True
        else: return False

    def teleport(self,x_new,y_new):
        self.x_coordinate = x_new
        self.y_coordinate = y_new

    def collision_detection(self,other_object):
        pass

def new_aliens_collection (alien_start_positions):
    aliens = []
    for position in alien_start_positions:
        aliens.append(Alien(position[0],position[1]))
    return aliens

