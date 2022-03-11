import numpy as np
from . import models


def sum(vect1: models.Vector, vect2: models.Vector) -> models.Vector:
    return models.Vector(np.array(vect1.get_vect()) + np.array(vect2.get_vect()))


def mul(vect1: models.Vector, vect2: models.Vector) -> models.Vector:
    return models.Vector(np.array(vect1.get_vect()) * np.array(vect2.get_vect()))


def len(vect1: models.Vector, vect2: models.Vector):
    return models.Vector(np.array([len(vect1.get_vect()), len(vect2.get_vect())]))
