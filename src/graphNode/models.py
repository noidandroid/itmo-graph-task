from django.db import models

# Create your models here.

class Node(models.Model):
    """Base graph node model"""
    #id = models.IntegerField("Node id")

    class Meta:
        db_table = 'node'

class Vector(Node):
    """Vector node model"""
   # valueList = models.JSONField("Vector container")

class Operation(Node):
    """Operation node model"""
    name = models.CharField("Operation name", max_length=250)