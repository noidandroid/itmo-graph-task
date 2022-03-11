from collections import defaultdict

from django.db import models
from django.contrib.postgres.fields import JSONField
import numpy as np

# Create your models here.


class Graph(models.Model):
    """Base graph model"""

    def __init__(self, connections, directed=False):
        self._graph = defaultdict(set)
        self._directed = directed
        self.add_connections(connections)

    def add_connections(self, connections):
        """ Add connections (list of tuple pairs) to graph """

        for node1, node2 in connections:
            self.add(node1, node2)

    def add(self, node1, node2):
        """ Add connection between node1 and node2 """

        self._graph[node1].add(node2)
        if not self._directed:
            self._graph[node2].add(node1)

    def remove(self, node):
        """ Remove all references to node """

        for n, cxns in self._graph.items():
            try:
                cxns.remove(node)
            except KeyError:
                pass
        try:
            del self._graph[node]
        except KeyError:
            pass

    def is_connected(self, node1, node2):
        """ Is node1 directly connected to node2 """
        return node1 in self._graph and node2 in self._graph[node1]

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self._graph))


class Node(models.Model):
    """Base graph node model"""
    node_id = models.IntegerField("Node id")


class Vector(Node):
    """Vector node model"""

    def __init__(self, value_list, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._value_list = []

    def get_vect(self):
        return self._value_list

    def expand(self, num):
        self._value_list.append(num)


class Operation(Node):
    """Operation node model"""
    name = models.CharField("Operation name", max_length=250)

    def sum(self, vect1: Vector, vect2: Vector) -> Vector:
        return Vector(np.array(vect1.get_vect()) + np.array(vect2.get_vect()))

    def mul(self, vect1: Vector, vect2: Vector) -> Vector:
        return Vector(np.array(vect1.get_vect()) * np.array(vect2.get_vect()))

    def len(self, vect1: Vector, vect2: Vector):
        return Vector(np.array([len(vect1.get_vect()), len(vect2.get_vect())]))

