#Cadyn Reger
class Ambulance:
    """A medical car that helps people.

    attributees: priority, speed, capacity."""

myHelp = Ambulance()

myHelp.priority = 1
myHelp.speed = 120
myHelp.capacity = 2


def formula():
    x = -10*(1-myHelp.priority)
    y = 2.37*(myHelp.speed/10)**3.98
    z = 30*(myHelp.capacity + 1.2)
    controlled_velocity = x + y + z
    print(controlled_velocity)

formula()
